# amazonpricetracker
I have built a web scraper with Beautiful Soup and Requests that will check the current price of an item and check for discounts.  Furthermore, it will send a text to your phone number alerting you of that discount.

**To run my code, simply enter your URL in the URL variable and create an instance of class WebScraper with the URL passed in the initialization.**

**Steps to make this yourself:**
(Assuming you have python installed and a proper text editor or IDE)

1. Make sure you have the dependencies:

pip install -r requirements.txt. While many libraries are being used, bs4 (Beautiful Soup) is the only one that needs to be installed.

2. Grab the URL of the web page

3. Set HEADERS = User Agent dictionary.
This is used to disguise youself as a human, not as a python script

4. Make sure you have a status code of 200 (not 503), and create a soup object to parse html.
Make sure you use "html.parser"

5. Find the prices from "inspect" and use soup.find(id = "insert_id_here").

6. Prompt user to enter his/her phone number, gmail (must be gmail), password, and mobile phone provider.

7. Sent text from email.

Have fun saving money!

![](https://www.marketplace.org/wp-content/uploads/2019/07/Amazondotcom.png)
