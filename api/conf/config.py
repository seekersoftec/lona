#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(basedir, ".env"))

# Create a database in project and get it's path.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
# SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_DB_URL")
PORT = os.getenv("PORT")
JWT_SECRET = os.getenv("JWT_SECRET")

# Convert to seconds
JWT_ACCESS_EXPIRATION_MINUTES = int(os.getenv("JWT_ACCESS_EXPIRATION_MINUTES"))*60
JWT_REFRESH_EXPIRATION_DAYS = int(os.getenv("JWT_REFRESH_EXPIRATION_DAYS"))*24*60*60 

# Blockchain 
BLOCKCHAIN_WEB_ADDRESS = 'http://127.0.0.1:9545'
COMPILED_CONTRACT_ABI = os.path.join(basedir, "smart_contract/build/contracts/lona.json")
CONTRACT_ADDRESS = '0x804318520FD6Bf0a44f8b4Ce7f5021B3e1C0F9AE'

# Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_DEBUG = app.debug
MAIL_USERNAME = 'yourId@gmail.com'
MAIL_PASSWORD = '*****'
# MAIL_DEFAULT_SENDER = MAIL_USERNAME
# MAIL_MAX_EMAILS = None
# MAIL_SUPPRESS_SEND = app.testing
# MAIL_ASCII_ATTACHMENTS = False