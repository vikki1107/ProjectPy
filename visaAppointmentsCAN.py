#!/usr/bin/python
#-------------------------------------------------------------------------------
# Following program helps in finding the available visa appointment dates for
# Canada from https://ais.usvisa-info.com/en-ca/niv/users/sign_in
# This would require selenium and urllib3 modules installed and
# also an temporary group without paying the visa fees but up until that page
# This script is configured to run on macOs as it requires a supporting file
# sendMessage.applescript. If trying to run it on Linux then change that to
# send email using UI automation. If using iMessage as mentioend here then
# iMessage has to be configured for a buddyID.
#-------------------------------------------------------------------------------
# import selenium and other essential modules
from selenium import webdriver
import time, subprocess

def refreshPage():
    # The following link will be the one from the payment page of an application from the group where the payment
    # hasn't been made. That profile would show the appointment dates for all locations.
    # Update the profileID below.
    driver.get("https://ais.usvisa-info.com/en-ca/niv/schedule/<profileID>/payment")    # Enter the profileID

# Locations for which we are looking for an appointment date
fav_loc=['Calgary', 'Toronto', 'Vancouver']                                     # Update the locations according to your choice

# Chrome options to run it in background
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver=webdriver.Chrome("/usr/local/bin/chromedriver",chrome_options=options)

# Login to the ais website using the username and password
# Sleep for 5 mins before entering the profileID page
# Update the email id and password of ais login page
driver.get("https://ais.usvisa-info.com/en-ca/niv/users/sign_in")
username = driver.find_element_by_id("user_email")
username.clear()
username.send_keys("<username>")                                                # Enter your ais user name here.. Usually your gmail id
password = driver.find_element_by_id("user_password")
password.clear()
password.send_keys("<password>")                                                 # Enter your ais user password.
policy = driver.find_element_by_id("policy_confirmed")
driver.execute_script("arguments[0].click();", policy)
driver.find_element_by_name("commit").click()

time.sleep(5)
refreshPage()

# Store all the records matched with "tr"
tr_records=driver.find_elements_by_css_selector("tr")

# Write the dates in /tmp/appointments.tmp and also
# send an iMessage using applescript
with open('/tmp/appointments.tmp', 'w') as out:
 out.write(time.strftime("%H:%M:%S")+'\n')
 for ll in tr_records[3:]:
  out.write(ll.text+'\n')
  if ll.text.split(' ')[0] in fav_loc:
   # Condition to get the dates Here all the dates that are less than June(month 6). Change the condition accordingly
   # You can add dates in the condition too like int(ll.text.split(' ')[1]) < 25
   if ll.text.split(' ')[2].strip(',') != 'Appointments' and (time.strptime(ll.text.split(' ')[2].strip(','), "%B").tm_mon < 6):
    message=time.strftime("%H:%M:%S") + " - BOOK: " + ll.text.split(' ')[0] + " " + ll.text.split(' ')[2].strip(',') + " " + ll.text.split(' ')[1].strip(',')
    subprocess.call(["osascript","sendMessage.applescript","<iMessage number>",message])      # Enter your phone number for iMessage with country code and without +
 out.write('\n')

# close the webdriver
driver.close()
