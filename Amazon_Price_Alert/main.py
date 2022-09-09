import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Xiaomi-Snapdragon-Unlocked-International-Bubblegum/dp/B093J49TFM/ref=sr_1_1?crid=2WNZ42FP1I3XO&keywords=mi+11x&qid=1649876125&sprefix=mi+11%2Caps%2C508&sr=8-1"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Encoding" : "gzip, deflate",
    "Request Line": "GET / HTTP/1.1",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
response = requests.get(URL, headers=headers)
website_html = response.text
# print(response.text)
soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())
price = soup.find(id="price_inside_buybox",class_="a-size-medium a-color-price")
print(price.getText().split('$')[1])
current_price = price.getText().split('$')[1]

my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if float(current_price) < 335.00:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="aravind.merugu2610@gmail.com",
            msg=f"Subject:Amazon Mi 11x price alert \n\nMI 11x price has dropped below {current_price} hurry up!")
    else:
        print("price is not below 350")
