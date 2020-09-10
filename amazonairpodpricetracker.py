#!/usr/bin/env python
# coding: utf-8

# In[123]:

# Getting webpage
from selenium import webdriver
# Used for sending text messages
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#To censor password
from getpass import getpass
#Download from README
driver = webdriver.Chrome(your_path_here)

URL = "https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_1_sspa?dchild=1&keywords=airpods&qid=1599024311&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUjNJTlJHODdaTUtaJmVuY3J5cHRlZElkPUEwMzI0NzIzMktMRkxZSUE5U1JINSZlbmNyeXB0ZWRBZElkPUExMDA0ODcwREJCVUpMV1FWMk9MJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

driver.get(URL)

title = driver.find_element_by_id('productTitle').text

discounted_price = driver.find_element_by_id("priceblock_ourprice").text                                                  

original_price = driver.find_element_by_xpath(("/html/body/div[4]/div[3]/div[2]/div[10]/div[13]/div/table/tbody/tr[1]/td[2]/span[1]")).text

discount = driver.find_element_by_xpath(("/html/body/div[4]/div[3]/div[2]/div[10]/div[13]/div/table/tbody/tr[3]/td[2]")).text.strip("(18%)")

#Get phone carrier
input_phone_carrier = int(input("Choose the number corresponding with your phone's mobile carrier: \n 0-AT&T, 1-Sprint, 2-T-Mobile, 3-Verizon, 4-Boost, 5-Cricket, 6-Metro PCS, 7-Track Phone, 8-US Cellular, 9-Virgin Mobile\n")) 

carrier_list = ["txt.att.net", "messaging.sprintpcs.com", "tmomail.net", "vtext.com", "myboostmobile.com", 
"sms.mycricket.com", "mymetropcs.com", "mmst5.tracfone.com", "email.uscc.net", "vmobl.com"]  
    
phone_number = input("Enter your phone number: ") + "@"

for i in range(len(carrier_list)):
    if i == input_phone_carrier:
        new_gateway = phone_number + carrier_list[i]
        i += 1

email = input('Enter your gmail: ')
password = getpass("Enter your password: ")   

def if_user_wants_to_send_text():
    decide_to_send_text = input("Would you like to have a text sent alerting you of discounts? ")
    
    if decide_to_send_text == "Yes":
        send_text()
    elif decide_to_send_text == "No":
        print("No text will be sent :)")
    else:
        print(decide_to_send_text, "is an invalid input. Please enter Yes or No")
    
    return decide_to_send_text        
        
def send_text():    
    ### Sending sms
    sms_gateway = new_gateway
    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
    # and port is also provided by the email provider.
    smtp = "smtp.gmail.com" 
    port = 587
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,password)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    # Make sure you add a new line in the subject
    msg['Subject'] = "Alert!\n\n"
    # Make sure you also add new lines to your body
    body = "There is a discount available on {}! The price has dropped from {} to {}.".format(title, original_price, discounted_price)
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)

    # lastly quit the server
    server.quit()

if_user_wants_to_send_text()
              
print("There is a discount on {}! The price has dropped from {} to {}!".format(title, original_price, discounted_price))
              
driver.close()
driver.quit()
