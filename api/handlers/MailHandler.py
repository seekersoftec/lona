#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.email.email import mail
from flask_mail import Message
  

# 
class SendMail:
    def __init__(self,recipients):
        self.recipients = recipients
    
    # 
    def login(self,profile_data):
         msg = Message('Lona', recipients = self.recipients)
         msg.body = "Your just logged in: {}".format(profile_data)
         mail.send(msg)
         return "Sent"
     
    def forgotPassword(self,reset_code):
         msg = Message('Lona', recipients = ['someone1@gmail.com'])
         msg.body = "Lona Reset code: {}".format(reset_code)
         mail.send(msg)
         return "Sent"
    
    # 
    def loanRepayment(self):
         msg = Message('Lona', recipients = self.recipients)
         msg.body = "Your Lona loan payment is due, please goto the platform and pay up your debts"
         mail.send(msg)
         return "Sent"
     # 
    def collateralPayment(self,collateral_amount,interest_rate,paid, mark_amount, loa_amount):
         msg = Message('Lona', recipients = self.recipients)
         msg.body = """
                    \b\rNGN {} Collateral received. Your loan has been sent.
                    \bMARK Tokens: {}
                    \bLOA Tokens: {} 
                    """.format(collateral_amount,mark_amount,loa_amount)
         mail.send(msg)
         return "Sent"
     
    def requestLoan(self,amount,collateral_amount,interest_rate,time_due):
         msg = Message('Lona', recipients = self.recipients)
         msg.body = """
                    \b\rYou just requested for a NGN {} loan today to expire at {} \n collateral: NGN {} \n interest rate: NGN {} \nplease goto the platform and pay your collateral
                    """.format(amount,time_due,collateral_amount,interest_rate)
         mail.send(msg)
         return "Sent"



