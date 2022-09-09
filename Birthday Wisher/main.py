import smtplib
import datetime as dt
import random
import pandas
#
my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"
#
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password = password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="aravindmeruguwgl@gmail.com",
#     msg="Subject:Hello\n\nThis is the body of the email")
# connection.close()
# my_email = "aravindkucet@gmail.com"
# password = "@Infopath77"
# now = dt.datetime.now()
# if(now.weekday()==4 and now.hour==15 and now.minute==14):
#     with open("quotes.txt", 'r') as file:
#         quotes_list = file.readlines()
#         body = (quotes_list[random.randint(0, 101)])
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password = password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=my_email,
#             msg=f"Subject:Quote of the day\n\n{body}")

now = dt.datetime.now()
pd = pandas.read_csv("birthdays.csv")
pd_dict = pd.to_dict(orient="records")
for item in pd_dict:
    if item["month"] == now.month and item["day"] == now.day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            contents = letter.read()
            contents=contents.replace("[NAME]",item["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password = password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=item["email"],
                msg=f"Subject:Happy Birthday {item['name']}\n\n{contents}")



