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

    """
    User schema returns only firstname, lastname, email, NIN, BVN, Bank Name, Bank Account Number, Ethereum Address, Business Information and creation time. This was used in user handlers.
    """

    # Schema parameters.

    firstname = fields.Str()
    # lastname = fields.Str()
    email = fields.Str()
    # nin_number = fields.Int()
    # bvn_number = fields.Int()
    # user_bank_name = fields.Str()
    # bank_account_number = fields.Int()
    # eth_address = fields.Str()
    # business_info = fields.Str()
    # details_verified = fields.Bool()
    # transaction_hashes = fields.Str()
    # created = fields.Str()
