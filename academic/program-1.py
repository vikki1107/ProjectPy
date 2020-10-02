# Assignment 1
"""
A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month. 
Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each. 
All cell phone bills include an additional charge of $0.44 to support 911 call centers. 
The entire bill (including 911 charge) is subject to 9% sales tax. 

Write a program that reads the number of minutes and text messages used in a month from the user. 
Display the base charge, additional minutes charge (if any), additional text message change (if any), the 911 fee, tax, and total bill amount. 
Only display the additional minute and text message charges if the user incurred costs in these categories. 
Ensure that all of the charges are displayed using 2 decimal places.

Created on Wed Oct 07 11:09:00 2015
@author: Vivek
"""

# user inputs number of minutes and text messages used in a month
minutes = int(input("Please enter the number of minutes: "))
messages = int(input("Please enter the number of messages: "))

emergency_support = .44
base_price = 15
additional_charge = 0

# check if the inputs are covered under the base price; if yes then print the base price else print the base price
# along with the additional charges(either messages or minutes or both)
if minutes <= 50 and messages <= 50:
    additional_charge = 0
    print "\nBase charge ------------------- %.2f " % base_price
elif minutes > 50 and messages > 50:
    additional_charge = ((minutes - 50) * .25) + ((messages - 50) * .15)
    print "\nBase charge ------------------- %.2f " % base_price
    print "Additional minutes charge ------ %.2f " % ((minutes - 50) * .25)
    print "Additional messages charge ----- %.2f " % ((messages - 50) * .15)
    print "Total additional usage charge -- %.2f " % additional_charge
elif minutes > 50:
    additional_charge = (minutes - 50) * .25
    print "\nBase charge ------------------- %.2f " % base_price
    print "Additional minutes charge ------ %.2f " % additional_charge
elif messages > 50:
    additional_charge = (messages - 50) * .15
    print "\nBase charge ------------------- %.2f " % base_price
    print "Additional messages charge ----- %.2f " % additional_charge

print "911 Emergency charge ---------- ", emergency_support

total_bill_before_tax = base_price + additional_charge + emergency_support

sales_tax = (total_bill_before_tax * 9) / 100
print "Sales tax ---------------------- %.2f " % sales_tax
print "========================================="
print "Total Bill amount -------------- %.2f " % (total_bill_before_tax + sales_tax)