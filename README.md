# amazonpricetracker
I have built a web scraper with Beautiful Soup and Requests that will track the price of airpods (although you can use any item). It will tell you the former price and discount. Furthermore, it will send a text to your phone number alerting you of that discount.

**Steps**:
(Assuming you have python installed and a proper text editor or IDE)

1. Make sure you have the dependencies:

pip install bs4 (Requests is built in)

pip install smtplib

pip install email-to

2. Grab the URL of the web page

3. Set HEADERS = User Agent dictionary.
This is used to disguise youself as a human, not as a python script

4. Make sure you have a status code of 200 (not 503) and set up soup object to parse html
Make sure you use "html.parser"

5. Find the prices from "inspect" and use soup.find(id = "insert_id_here")

6. Prompt user to enter his/her phone number, gmail (must be gmail), password, and mobile phone provider

7. Sent text from email

Have fun saving money!

![Airpods](airpods.jpg)
