#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_cors import CORS

from api.conf.config import (SQLALCHEMY_DATABASE_URI,
                             PORT,COMPILED_CONTRACT_ABI,
                             MAIL_SERVER,MAIL_PORT,MAIL_USERNAME,
                             MAIL_PASSWORD,MAIL_USE_TLS,MAIL_USE_SSL)
from api.conf.routes import generate_routes
from api.handlers.LonaContractHandler import LONAContract
from api.email.email import mail
# from api.crontab.crontab import crontab
from api.crontab.scheduled_jobs import repayLoanAlert
from api.database.database import db
from api.db_initializer.db_initializer import (create_admin_user,
                                               create_super_admin,
                                               create_test_user)


def create_app():
    # Instance to interact with the Smart contract
    LONA_Contract = LONAContract(COMPILED_CONTRACT_ABI)
    print("\n=> "+LONA_Contract.isReady()+"\n")
    
    # Create a flask app.
    app = Flask(__name__)

    #CORS
    # cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app)
     
    # Set debug true for catching the errors.
    app.config['DEBUG'] = True

    # Set database url.
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Set mail configs
    app.config['MAIL_SERVER'] = MAIL_SERVER
    app.config['MAIL_PORT'] = MAIL_PORT
    app.config['MAIL_USERNAME'] = MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
    app.config['MAIL_DEFAULT_SENDER'] = MAIL_USERNAME
    app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
    
    # Generate routes.
    generate_routes(app)

    # Database initialize with app.
    db.init_app(app)
    
    # Mail initalize with app
    mail.init_app(app)
    
    # Crontab initalize with app
    # crontab.init_app(app)

    # Check if there is no database.
    if not os.path.exists(SQLALCHEMY_DATABASE_URI):

        # New db app if no database.
        db.app = app

        # Create all database tables.
        db.create_all()

        # Create default super admin user in database.
        create_super_admin()

        # Create default admin user in database.
        create_admin_user()

        # Create default test user in database.
        create_test_user()

    # # notificaton cron tab
    # @crontab.job(minute="0.1", hour="0")
    # def my_scheduled_job():
    # repayLoanAlert()
    
    # Return app.
    return app


if __name__ == '__main__':

    # Create app.
    app = create_app()

    # Run app. For production use another web server.
    # Set debug and use_reloader parameters as False.
    app.run(port=PORT, debug=False, use_reloader=False)