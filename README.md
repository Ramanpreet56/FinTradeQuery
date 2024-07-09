
Sample use case for a Financial Reporting System.

Since it was not specified what type of reporting system , I created a simple Trade Reporting platform which generates an Online view and a PDF view for the end user.

On the home page , User is asked for an input Account Number ( This can be 1-50) in our example and recvies the Trade executed by this user.

There are Two types of data representing the real life banking situations i.e. Static Data and Dynamic Data 

In our example we have everything basic : 

Static Data : Customer Details
Dynamic Data : Trade details

Initially for the web view , my plan was to implement a more granular view with links to everything  eg IF user sees portfolio on screen and clicks it he gets to see static data about portfolio from portfolio table , same goes for Counterparty  and other static items. This can be implemented further.

For PDF view , Currently we have used a Text File as a Template to print the PDF . This picking up of a Text file and replacing placeholder represents templating ( Very important for Financial Reporting). I could have expanded this on further levels (eg Updating Static / Dynamic Data from Text files  being delivered to us) and so on and so forth if required.


To run this : Do a git clone : 

git clone https://github.com/Ramanpreet56/FinTradeQuery.git

Then from the app directory run:

python3 app.py

The result output PDF would be available in the appdir . 

Trades are available only for account number 1,2,3 and for rest there would be no trade data.