from twilio.rest import Client
import smtplib

account_sid = "YOUR_SID"
auth_token = "YOUR_AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR_TWILLIO_VIRTUAL_NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR_TWILLIO_VERIFIED_NUMBER"

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login("aravindkucet@gmail.com", "@Infopath77")
            for email in emails:
                connection.sendmail(
                    from_addr="aravindkucet@gmail.com",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
