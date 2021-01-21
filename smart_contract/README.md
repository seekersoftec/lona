Token - Lona
Customer
Loan Provider

Resources(Lona):
1. Smart Contract
2. REST server
3. Web App

User Flow:
1. User Register on the system through the web app
2. User inputs his eth address, bvn, account details and other details through the web app.
3. After registering, user logs in 

4. User tries to collect a loan by putting in the amount he wants, the server then calculates how much colateral he should pay (e.g 25% of the loan amount).

5. User pays the colateral amount which is connected to an equivalent value of lona token, which is stored on the smart contract with the users eth address attached to it.

6. Then the server sends the loan amount to the user, and stores the time due, amount, colateral amount, and interest rate in the database.

7. When the time comes for the loan to be repaid an email is sent to the user to repay the loan if the user repays the loan, the collateral token is destroyed, the amount sent back to the user and the userscore increased which would be used to calculate the colateral amount when next he wants to withdraw.

8. If the user refused to pay, the userscore would be decreased, the ethereum address flagged and his bvn, also the token is destroyed and the service keeps the amount.


Step by Step Process
The user registers on the platform by going to the address of the web app, inputing his details e.g: Name, NIN number, BVN number, business info then the web app does a background check to see if it is correct, he is also required to input his ethereum address if he has one, lest the platform creates one for him, his bank account details is also required, after inputting all these details, the web app processes these and chooses to either accept or reject the request.

After registering the user logs in and is welcomed into the platform.

The User requests for a loan, by inputting the amount required and the duration of the loan, if it is possible, the web app calculates the interest rate which is a function of the amount of Mark token the user has, if this is the first time requesting for a loan a standard interest rate is given, then the collateral amount is also calculated, which is function of both the loan amount requested and the amount of mark token the user has. Note

Note: The interest rate is inversely proportional to the number of marks to keep. While the collateral is directly proportional to the loan amount and inversely proportional to the number of mark tokens.

Interest Rate =k 1/Number of Mark Tokens

Collateral =k loan amount/Number of Mark Tokens

And sends a transaction to the smart contract to increase the mark tokens of the users.

Both the interest Rate and Collateral amount is then sent to the user, which the user can then process with the payment of the collateral.

After the collateral is payed on the web app, an equivalent LOA amount is created on the smart contract for the user, note that the LOA token is pegged to the Naira(NGN), so N50,000 is equivalent to 50,0000 LOA, then the smart contract will emit an event marking the successful creation of the Tokens.

Then the Loan Amount is sent to the Users bank account which he then confirms.

When the Loan Repayment is due, the web app sends an Email to the User, requesting him to repay the amount given with interest.
