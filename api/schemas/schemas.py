#!/usr/bin/python
# -*- coding: utf-8 -*-

from marshmallow import Schema, fields


class BaseUserSchema(Schema):

    """
    Base user schema returns all fields but this was not used in user handlers.
    """

    # Schema parameters.

    id = fields.Int(dump_only=True)
    firstname = fields.Str()
    lastname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    created = fields.Str()


class UserSchema(Schema):
<<<<<<< HEAD
    class Meta:
        # Fields to expose
        fields = ("lastname", "firstname")
=======
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249

    """
    User schema returns only firstname, lastname, email, NIN, BVN, Bank Name, Bank Account Number, Ethereum Address, Business Information and creation time. This was used in user handlers.
    """

    # Schema parameters.

<<<<<<< HEAD
    # firstname = fields.Str()
    # lastname = fields.Str()
    # email = fields.Str()
=======
    firstname = fields.Str()
    # lastname = fields.Str()
    email = fields.Str()
>>>>>>> 44372833b2e689f10e4261cca465dce4e4d8c249
    # nin_number = fields.Int()
    # bvn_number = fields.Int()
    # user_bank_name = fields.Str()
    # bank_account_number = fields.Int()
    # eth_address = fields.Str()
    # business_info = fields.Str()
    # details_verified = fields.Bool()
    # transaction_hashes = fields.Str()
    # created = fields.Str()
