#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Api

from api.handlers.UserHandlers import (
    DataAdminRequired,
    DataUserRequired,
    Index,
    Login,
    Logout,
    RefreshToken,
    Register,
    ResetPassword,
    ForgotPassword,
    UsersData,
    DataSuperAdminRequired,
    RequestLoan,
    RepayLoan,
    PayCollateral,
    UserVerification)


def generate_routes(app):

    # Create api.
    api = Api(app)

    # Add all routes resources.
    # Index page.
    api.add_resource(Index, "/")

    # Register page.
    api.add_resource(Register, "/v1/auth/register")

    # Login page.
    api.add_resource(Login, "/v1/auth/login")

    # Logout page.
    api.add_resource(Logout, "/v1/auth/logout")

    # Refresh page.
    api.add_resource(RefreshToken, "/v1/auth/refresh")

    # Password reset page. 
    api.add_resource(ResetPassword, "/v1/auth/password_reset")
    
    # Password forgot page
    api.add_resource(ForgotPassword, "/v1/auth/forgot_password")

    # Example user handler for user permission.
    api.add_resource(DataUserRequired, "/v1/profile")

    # Example admin handler for admin permission.
    api.add_resource(DataAdminRequired, "/v1/data_admin")

    # Example user handler for user permission.
    api.add_resource(DataSuperAdminRequired, "/v1/data_super_admin")

    # Get users page with super admin permissions.
    api.add_resource(UsersData, "/v1/users")
    
    # Get users page with super admin permissions.
    api.add_resource(UserVerification, "/v1/verify_user")
    
    # Request Loan page
    api.add_resource(RequestLoan, "/v1/request_loan")

    # Repay loan page
    api.add_resource(RepayLoan, "/v1/repay_loan")
    
    # Pay collateral page
    api.add_resource(PayCollateral, "/v1/pay_collateral")
