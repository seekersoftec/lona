#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JsonWebToken
from .config import JWT_SECRET,JWT_ACCESS_EXPIRATION_MINUTES,JWT_REFRESH_EXPIRATION_DAYS

# JWT creation.
jwt = JsonWebToken(JWT_SECRET, expires_in=JWT_ACCESS_EXPIRATION_MINUTES)

# Refresh token creation.
refresh_jwt = JsonWebToken(JWT_SECRET, expires_in=JWT_REFRESH_EXPIRATION_DAYS)

# Auth object creation.
auth = HTTPTokenAuth("Bearer")
