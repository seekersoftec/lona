import logging
from api.database.database import db
from api.models.models import Blacklist, User
from datetime import timedelta, datetime

BRIDGE_AMOUNT = 100000

# 
def max_time(amount,due_time):
    """
        Checks if time range is greater than maximum 
        - amount
        - due_time [in weeks]
    """
    
    # start_date = '20090909' # default start date
    # end_date = datetime.today().strftime("%Y%m%d") # default end date
    # datetime.now()
    if (
        (amount < BRIDGE_AMOUNT and due_time <= 52) or
        (amount > BRIDGE_AMOUNT and due_time <= (52+26))
        ):
        return True

    return False


def send_loan_to_User(bvn_number,user_bank,bank_account_number):
    if ():
        pass
    #datetime.datetime.today().strftime("%Y%m%d") 
    return False

def verify_payment_details():
    if ():
        pass
    return False

