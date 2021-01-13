#!/usr/bin/python
# -*- coding: utf-8 -*-

SERVER_ERROR_500 = ({"message": "An error occured."}, 500)
NOT_FOUND_404 = ({"message": "Resource could not be found."}, 404)
NO_INPUT_400 = ({"message": "No input data provided."}, 400)
INVALID_INPUT_422 = ({"message": "One or more field(s) are wrong."}, 422)
ALREADY_EXIST = ({"message": "Already exists."}, 409)
UNAUTHORIZED = ({"message": "Wrong credentials."}, 401)

DOES_NOT_EXIST = ({"message": "Does not exists."}, 409)
NOT_ADMIN = ({"message": "Admin permission denied."}, 999)
HEADER_NOT_FOUND = ({"message": "Header does not exists."}, 999)
USER_BLACKLISTED = ({"message": "User blacklisted."}, 1404)
USER_NOT_VERIFIED = ({"message": "User not verified."}, 1405)
PASSWORDS_NOT_MATCH = ({"message": "passwords are not the same"}, 1405)
TIME_NOT_WITHIN_RANGE = ({"message": "time not within range"}, 1406)
