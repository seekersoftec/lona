#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from api.database.database import db
from api.models.models import User


def create_super_admin(email="sa_email@example.com"):

    # Check if admin is existed in db.
    user = User.query.filter_by(email=email).first()

    # If user is none.
    if user is None:

        # Create admin user if it does not existed.
        user = User(
            firstname="sa_firstname",
            lastname="sa_lastname",
            password="sa_password",
            email=email,
            user_role="sa",
        )

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Print admin user status.
        logging.info("Super admin was set.")

    else:

        # Print admin user status.
        logging.info("Super admin already set.")


def create_admin_user(email="admin_email@example.com"):

    # Check if admin is existed in db.
    user = User.query.filter_by(email=email).first()

    # If user is none.
    if user is None:

        # Create admin user if it does not existed.
        user = User(
            firstname="admin_firstname",
            lastname="admin_lastname",
            password="admin_password",
            email=email,
            user_role="admin",
        )

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Print admin user status.
        logging.info("Admin was set.")

    else:
        # Print admin user status.
        logging.info("Admin already set.")


def create_test_user(
    firstname="test_firstname",
    lastname="test_lastname",
    password="test_password",
    email="test_email@example.com",
    nin_number="", 
    bvn_number="", 
    user_bank_name="", 
    bank_account_number="", 
    eth_address="", 
    business_info="",
    user_role="user",
):

    # Check if admin is existed in db.
    user = User.query.filter_by(email=email).first()

    # If user is none.
    if user is None:

        # Create admin user if it does not existed.
        # user = User()
        user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            nin_number=nin_number, 
            bvn_number=bvn_number, 
            user_bank_name=user_bank_name, 
            bank_account_number=bank_account_number, 
            eth_address=eth_address, 
            business_info=business_info,
            user_role=user_role,
        )

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Print admin user status.
        logging.info("Test user was set.")

        # Return user.
        return user

    else:

        # Print admin user status.
        logging.info("User already set.")
