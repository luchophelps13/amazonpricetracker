#Send HTTP Requests
import requests
#Scrape HTML
from bs4 import BeautifulSoup
#Sending SMS
import smtplib 
#Formatting SMS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class WebScraper:
    
    def __init__(self, URL):
        self.URL = URL
    
    def scrape_data(self):
        URL = self.URL
        HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

        page = requests.get(URL, headers = HEADERS)
        
        soup = BeautifulSoup(page.content, "html.parser")

        print(f"\nStatus code: {page.status_code} \n")
        
        global product_title
        product_title = soup.find(id = "productTitle").get_text(strip=True)
        
        global listed_price
        listed_price = soup.find(id = "priceblock_ourprice")
        
        ## Check if there is a discount on the webpage, and if there isn't, set the values equal to None
        try:
            global discount
            discount = soup.find(class_ = "a-span12 a-color-price a-size-base priceBlockSavingsString").get_text(strip=True)
            
            print(f"The discount on '{product_title}' is: {discount}")
            
            global original_price
            original_price = soup.find(class_="priceBlockStrikePriceString a-text-strike").get_text(strip=True)
        
        except:
            discount = None
            original_price = None
            print(f"'{product_title}' has no discount")

    def if_user_wants_to_send_text(self):
        
        decide_to_send_text = input("Would you like to have a text sent alerting you of discounts? ")
        
        if decide_to_send_text == "Yes":
            self.send_text()
        elif decide_to_send_text == "No":
            print("No text will be sent :)")
        else:
            print(f"'{decide_to_send_text}' is an invalid input. Please enter Yes or No.")
        
        return decide_to_send_text

    def send_text(self):    

        phone_number = input("Enter your phone number: ") + "@"    

        input_phone_carrier = int(input("Input the number corresponding with your mobile phone carrier: \n0-AT&T, 1-Sprint, 2-T-Mobile, 3-Verizon, 4-Boost, 5-Cricket, 6-Metro PCS, 7-Track Phone, 8-US Cellular, 9-Virgin Mobile\n"))

        carrier_list = ["txt.att.net", "messaging.sprintpcs.com", "tmomail.net", "vtext.com", "myboostmobile.com", 
            "sms.mycricket.com", "mymetropcs.com", "mmst5.tracfone.com", "email.uscc.net", "vmobl.com"] 

        for i in range(len(carrier_list)):
            if i == input_phone_carrier:
                new_gateway = phone_number + carrier_list[i]
                i += 1

        gmail = input('Enter your gmail: ')

        password = input("Enter your password: ")        
       
        ### Sending sms
        sms_gateway = new_gateway
        # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
        # and port is also provided by the email provider.
        smtp = "smtp.gmail.com" 
        port = 587
        # This will start our email server
        server = smtplib.SMTP(smtp, port)
        # Starting the server
        server.starttls()
        # Now we need to login
        server.login(gmail,password)

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg['From'] = gmail
        msg['To'] = sms_gateway
        # Make sure you add a new line in the subject
        
        if discount != None:
            msg['Subject'] = "Alert!\n"
            body = f"There is a discount on {product_title}! The price is now {listed_price}, with a discount of {discount}!"
        else:
            msg['Subject'] = "I'm Sorry to Inform You... \n"
            body = f"There is no discount on {product_title}"
        # Make sure you also add new lines to your body
    
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))

        sms = msg.as_string()

        server.sendmail(gmail, sms_gateway, sms)

        # lastly quit the server
        server.quit()

URL = "enter_url_here"
my_scraper = WebScraper(URL)

my_scraper.scrape_data()
my_scraper.if_user_wants_to_send_text()
