
# 
# 
# Using Queues[Monitoring the database]:
# check if their is any user in the database with expired loan date
# send mail to user
# if user does not pay reduce mark token (ahead of the given time) [check if user has repaid loan: if not and the time is 5 days] ,
# reduce the mark tokens by half [if mark tokens <= 0: blacklist the user]
# destroy the lOA tokens
# 
# 
# 
# 
# event emitter for any user that has to repay the loan
# 
# notificaton cron tab

def repayLoanAlert():
    """
        Repay loan alert
    """
    print('loan alert')
    # try:
    #     # Get end date.
    #     end_date = datetime.strptime('', "%d.%m.%Y")
            
    #     # Get today's date and time
    #     # Filter users by loan time due
    #     users = (
    #         User.query
    #         .filter(User.email.in_(emails))
    #         .filter(User.loan_expire_date)
    #         .all()
    #     )
        
    #     # Create user schema for serializing.
    #     user_schema = UserSchema(many=True)
        
    #     # Get json data
    #     data, errors = user_schema.dump(users)
        
    #     # Return json data from db.
    #     return data
    
    # except Exception as why:
    #     # Log the error.
    #     logging.error(why)
    #     # Return error.
    #     return error.INVALID_INPUT_422
    
    