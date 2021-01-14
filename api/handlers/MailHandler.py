#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.email.email import mail
from flask_mail import Message
  

# 
class SendMail:
    def __init__(self,recipients):
        self.recipients = recipients
    
    # 
    def forgotPassword(self,reset_code):
         msg = Message('Hello', recipients = ['someone1@gmail.com'])
         msg.body = "Lona Reset code: {}".format(reset_code)
         mail.send(msg)
         return "Sent"
    
    # 
    def loanRepayment(self):
         msg = Message('Hello', recipients = ['someone1@gmail.com'])
         msg.body = "Your Lona loan payment is due, please goto the platform and pay up your debts"
         mail.send(msg)
         return "Sent"
     # 
    def collateralPayment(self,amount,collateral_amount,interest_rate,time_due,time_requested):
         msg = Message('Hello', recipients = ['someone1@gmail.com'])
         msg.body = "Collateral received. Your Lona loan has been sent"
         mail.send(msg)
         return "Sent"
     
    def requestLoan(self,amount,collateral_amount,interest_rate,time_due,time_requested):
         msg = Message('Hello', recipients = ['someone1@gmail.com'])
         msg.body = "Your Lona loan payment is due, please goto the platform and pay up your debts"
         mail.send(msg)
         return "Sent"



