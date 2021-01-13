#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import random
from datetime import datetime

from flask import g, request
from flask_restful import Resource

import api.error.errors as error
from api.conf.auth import auth, refresh_jwt
from api.conf.utils import max_time, send_loan_to_User, verify_payment_details
from api.database.database import db
from api.models.models import Blacklist, User
from api.roles import role_required
from api.schemas.schemas import UserSchema
from api.handlers.MailHandler import SendMail
from api.handlers.LonaContractHandler import LONAContract
from api.conf.config import COMPILED_CONTRACT_ABI


#LONA contract 
LONA_Contract = LONAContract(COMPILED_CONTRACT_ABI)
 
 
 
class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to Lona - A Blockchain Based Collateral Loan Management Service"


class Register(Resource):
    @staticmethod
    def post():

        try:
            # Get
            # Name[firstname, lastname], NIN number, BVN number, business info
            # eth address, bank account details, email, password
            firstname, lastname, email, password_1, password_2, nin_number, bvn_number, user_bank_name, bank_account_number, eth_address, business_info = (
                request.json.get("firstname").strip(),
                request.json.get("lastname").strip(),
                request.json.get("email").strip(),
                request.json.get("password_1").strip(),
                request.json.get("password_2").strip(),
                request.json.get("nin_number").strip(),
                request.json.get("bvn_number").strip(),
                request.json.get("user_bank_name").strip(),
                request.json.get("bank_account_number").strip(),
                request.json.get("eth_address").strip(),
                request.json.get("business_info").strip(),
            )
        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("one or more field(s) is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422

        # Check if any field is none.
        if (
            firstname is None or firstname == '' or 
            lastname is None or lastname == '' or
            email is None or email == '' or
            password_1 is None or password_1 == '' or
            password_2 is None or password_2 == '' or
            nin_number is None or nin_number == '' or
            bvn_number is None or bvn_number == '' or
            user_bank_name is None or user_bank_name == '' or
            bank_account_number is None or bank_account_number == '' or
            eth_address is None or eth_address == ''
            ):
            return error.INVALID_INPUT_422

        if (password_1 != password_2):
            return error.PASSWORDS_NOT_MATCH
        
        # Get user if it is existed.
        user = User.query.filter_by(email=email).first()

        # Check if user is existed.
        if user is not None:
            return error.ALREADY_EXIST
        
        # Create a new user.
        user = User(firstname=firstname, lastname=lastname, email=email, 
                    password=password_1, nin_number=nin_number, bvn_number=bvn_number,
                    user_bank_name=user_bank_name, bank_account_number=bank_account_number,
                    eth_address=eth_address, business_info=business_info
                    )

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Return success if registration is completed.
        return {"status": "registration completed."}


class Login(Resource):
    @staticmethod
    def post():

        try:
            # Get user email and password.
            email, password = (
                request.json.get("email").strip(),
                request.json.get("password").strip(),
            )

        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Email or password is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422

        # Check if user information is none.
        if email is None or password is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        user = User.query.filter_by(email=email, password=password).first()
        
        # Check if user is not existed.
        if user is None:
            return error.UNAUTHORIZED
        
        # 
        if user.user_role == "user":

            # Generate access token. This method takes boolean value for checking admin or normal user. Admin: 1 or 0.
            access_token = user.generate_auth_token(0)

        # If user is admin.
        elif user.user_role == "admin":

            # Generate access token. This method takes boolean value for checking admin or normal user. Admin: 1 or 0.
            access_token = user.generate_auth_token(1)

        # If user is super admin.
        elif user.user_role == "sa":

            # Generate access token. This method takes boolean value for checking admin or normal user. Admin: 2, 1, 0.
            access_token = user.generate_auth_token(2)

        else:
            return error.INVALID_INPUT_422

        # Generate refresh token.
        refresh_token = refresh_jwt.dumps({"email": email})

        # Return access token and refresh token.
        return {
            "access_token": access_token.decode(),
            "refresh_token": refresh_token.decode(),
        }


class Logout(Resource):
    @staticmethod
    @auth.login_required
    def post():

        # Get refresh token.
        refresh_token = request.json.get("refresh_token")

        # Get if the refresh token is in blacklist
        ref = Blacklist.query.filter_by(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if ref is not None:
            return {"status": "already invalidated", "refresh_token": refresh_token}

        # Create a blacklist refresh token.
        blacklist_refresh_token = Blacklist(refresh_token=refresh_token)

        # Add refresh token to session.
        db.session.add(blacklist_refresh_token)

        # Commit session.
        db.session.commit()

        # Return status of refresh token.
        return {"status": "invalidated", "refresh_token": refresh_token}


class RefreshToken(Resource):
    @staticmethod
    def post():

        # Get refresh token.
        refresh_token = request.json.get("refresh_token")

        # Get if the refresh token is in blacklist.
        ref = Blacklist.query.filter_by(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if ref is not None:

            # Return invalidated token.
            return {"status": "invalidated"}

        try:
            # Generate new token.
            data = refresh_jwt.loads(refresh_token)

        except Exception as why:
            # Log the error.
            logging.error(why)

            # If it does not generated return false.
            return False

        # Create user not to add db. For generating token.
        user = User(email=data["email"])

        # New token generate.
        token = user.generate_auth_token(False)

        # Return new access token.
        return {"access_token": token}


class ForgotPassword(Resource):
    def post(self):
        try:
            # Get user email.
            email = request.json.get("email").strip()

        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Email is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422
        

        # Check if user information is none.
        if email is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        user = User.query.filter_by(email=email).first()
        
        # Check if user is not existed.
        if user is None:
            return error.UNAUTHORIZED

        # generate password reset code and update the user password with it
        generated_reset_code = random.random()*(10**8)
        
        # Update password.
        user.password = generated_reset_code

        # Commit session.
        db.session.commit()
        
        # Send Forgot Password Mail
        SendMail([user.email]).forgotPassword(generated_reset_code)

        # Return success status.
        return {"status": "Forgot password mail sent"}



class ResetPassword(Resource):
    def post(self):

        # Get old and new passwords.
        email, reset_code, new_password = (
                                            request.json.get("email"), 
                                            request.json.get("reset_code"), 
                                            request.json.get("new_password")
                                        )

        # Get user.
        user = User.query.filter_by(email=email).first()

        # Check if user password does not match with reset_code.
        if user.password != reset_code:

            # Return does not match status.
            return {"status": "reset code does not match."}

        # Update password.
        user.password = new_password

        # Commit session.
        db.session.commit()

        # Return success status.
        return {"status": "password changed."}


class UsersData(Resource):
    @auth.login_required
    @role_required.permission(2)
    def get(self):
        try:

            # Get firstnames.
            firstnames = (
                []
                if request.args.get("firstnames") is None
                else request.args.get("firstnames").split(",")
            )

            # Get emails.
            emails = (
                []
                if request.args.get("emails") is None
                else request.args.get("emails").split(",")
            )

            # Get start date.
            start_date = datetime.strptime(request.args.get("start_date"), "%d.%m.%Y")

            # Get end date.
            end_date = datetime.strptime(request.args.get("end_date"), "%d.%m.%Y")

            print(firstnames, emails, start_date, end_date)

            # Filter users by firstnames, emails and range of date.
            users = (
                User.query.filter(User.firstname.in_(firstnames))
                .filter(User.email.in_(emails))
                .filter(User.created.between(start_date, end_date))
                .all()
            )

            # Create user schema for serializing.
            user_schema = UserSchema(many=True)

            # Get json data
            data, errors = user_schema.dump(users)

            # Return json data from db.
            return data

        except Exception as why:

            # Log the error.
            logging.error(why)

            # Return error.
            return error.INVALID_INPUT_422


# auth.login_required: Auth is necessary for this handler.
# role_required.permission: Role required user=0, admin=1 and super admin=2.


class DataUserRequired(Resource):
    @auth.login_required
    def get(self):
        # Get user
        user = User.query.filter_by(email=g.user).first()
        
        # print(user)
        # Create user schema for serializing.
        user_schema = UserSchema()
        
        # Get json data
        data, errors = user_schema.dump(user)
        
        # Return json data from db.
        return data


class DataAdminRequired(Resource):
    @auth.login_required
    @role_required.permission(1)
    def get(self):
        # Get user
        user = User.query.filter_by(email=g.user).first()
        
        # Create user schema for serializing.
        user_schema = UserSchema(many=True)
        
        # Get json data
        data, errors = user_schema.dump(user)
        
        # Return json data from db.
        return data


class DataSuperAdminRequired(Resource):
    @auth.login_required
    @role_required.permission(2)
    def get(self):
        # Get user
        user = User.query.filter_by(email=g.user).first()
        
        # Create user schema for serializing.
        user_schema = UserSchema()
        
        # Get json data
        data, errors = user_schema.dump(user)
        
        # Return json data from db.
        return data


class UserVerification(Resource):
    @auth.login_required
    @role_required.permission(2)
    def post(self):
        # 
        user_email = request.json.get("user_email")
        
        # Get user
        user = User.query.filter_by(email=user_email).first()
        
        # Check if user is verified.
        if user.details_verified is not True:
            user.details_verified = True
            # Commit session.
            db.session.commit()

        return {
            'status':'user verified'
        }
        
        
    
class RequestLoan(Resource):
    @auth.login_required
    def post(self):
        print('Requested loan')
        # Get loan request amount
        amount, loan_expire_date = request.json.get("amount"),request.json.get("loan_expire_date")

        # Get user
        user = User.query.filter_by(email=g.user).first()
        
        # Check if user is verified.
        if user.details_verified is not True:
            # Return user not verified
            return error.USER_NOT_VERIFIED
        
        # 
        num_of_marks = LONA_Contract.MarkAmount(user.eth_address)
        collateral_amount = 0
        interest_rate = 0
        
        # Check if user is blacklisted
        if user.blacklisted is True or num_of_marks <= 0:
            return error.USER_BLACKLISTED
        
        # Check range of time due
        if max_time(amount,loan_expire_date) is False:
            return error.TIME_NOT_WITHIN_RANGE
        
        # Check if it's user first time
        if len(user.transactions) > 0:
            # []
            collateral_amount = int(amount)/num_of_marks #
            interest_rate = 1/num_of_marks # 
        
        else:
            # [standard] [if it's the user first time]
            collateral_amount = (25/100)*amount # 25% 
            interest_rate = (2/100)*amount # 2%
          
        # Update loan details
        user.amount_loaned = amount
        user.collateral_amount = collateral_amount
        user.interest_rate = interest_rate
        user.loan_expire_date = loan_expire_date
        
        # Commit session.
        db.session.commit()
        
        # Send a mail to the user 
        SendMail([user.email]).requestLoan(amount,collateral_amount,interest_rate,time_requested=datetime.now())
        
        return {
            'amount':amount,
            'collateral': collateral_amount,
            'interest rate': interest_rate,
            'time due':loan_expire_date
        }



# 
class PayCollateral(Resource):
    @auth.login_required
    def post(self):
        # user pays collateral
        # Get user
        payment_details = request.json.get("payment_details")

        # verify payment details through the payment gateway
        verify_payment = verify_payment_details(payment_details)
        
        # if details is not verified or authentic or any error
        if (verify_payment is False):
            return {'message':'Collateral payment details cannot be verified'}
        
        # Get user
        user = User.query.filter_by(email=g.user).first()
        
        # LOA|MARK token is created
        LONA_Contract.addLOA(user.eth_address,user.collateral_amount)
        LONA_Contract.addMARK(user.eth_address,user.collateral_amount)
        
        # send loan
        send_loan = send_loan_to_User(user.bvn_number,user.user_bank_name,user.bank_account_number)
        
        # 
        if send_loan is False:
            return {'message':'Loan not sent to bank account'}
        
        # Loan sent to the users bank account
        user.loan_sent_date =  send_loan #
        # save the day the loan was sent to the users bank account
        
        # Commit session.
        db.session.commit()
        
        # Send a mail to the user 
        SendMail([user.email]).collateralPayment(payment_details,time_requested=datetime.now())
        
        # 
        return {
            'status': 'collateral payment successful',
            'message': 'Loan Sent'
        }


# 
class RepayLoan(Resource): 
    @auth.login_required
    def post(self):
        # user repays loan
        
        # Get user payment details through the payment gateway
        payment_details = request.json.get("payment_details")

        # verify payment details through the payment gateway
        verify_payment = verify_payment_details(payment_details)
        
        # if details is not verified or authentic or any error
        if (verify_payment is False):
            return {'message':'Loan payment details cannot be verified'}
        
        # 
        return {
            'status': 'Loan Repayed',
            'message': 'Collateral Sent'
        }

 
