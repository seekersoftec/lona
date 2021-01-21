#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(basedir, ".env"))

# Create a database in project and get it's path.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
# SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_DB_URL")
# PORT = os.getenv("PORT")
PORT = 8000
# JWT_SECRET = os.getenv("JWT_SECRET")
JWT_SECRET='lonadevsamplesecret'

# Convert to seconds
# JWT_ACCESS_EXPIRATION_MINUTES = int(os.getenv("JWT_ACCESS_EXPIRATION_MINUTES"))*60
JWT_ACCESS_EXPIRATION_MINUTES=60*60
# JWT_REFRESH_EXPIRATION_DAYS = int(os.getenv("JWT_REFRESH_EXPIRATION_DAYS"))*24*60*60 
JWT_REFRESH_EXPIRATION_DAYS=30*24*60*60
# Blockchain 
# BLOCKCHAIN_WEB_ADDRESS = 'http://127.0.0.1:9545'
BLOCKCHAIN_WEB_ADDRESS = 'https://ropsten.infura.io/v3/40462918cb0b45aab9abfb422aaa0f3c'
COMPILED_CONTRACT_ABI = os.path.join(basedir, "smart_contract/lona.json")
# CONTRACT_ADDRESS = '0x5b7778D0ef3Ca98554dA3dDFE1b6708D6D6c403e'
CONTRACT_ADDRESS = '0x8145bC99355198AE4324E0e0Ac7480Fc7cC7faE8'
# FROM_ADDRESS = '0x577C24aB6C97F22f1eaEb0510150b8A4Ecf425a1'
FROM_ADDRESS = '0x2a2Af8bdcACD5136ab504E33268f9aFE72C12007'
FROM_ADDRESS_KEY = '7249937e83295c27b5db549ed22f61cc503c78324023862c441fd5330995891a'

# Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_DEBUG = app.debug
MAIL_USERNAME = 'josephgmunoz145@gmail.com'
MAIL_PASSWORD = 'joseph145'
# MAIL_DEFAULT_SENDER = MAIL_USERNAME
# MAIL_MAX_EMAILS = None
# MAIL_SUPPRESS_SEND = app.testing
# MAIL_ASCII_ATTACHMENTS = False