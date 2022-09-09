import requests
from flask import Flask, render_template, request
import smtplib, ssl

app = Flask(__name__)

OWN_EMAIL = 'YOUR_EMAIL'
OWN_PASSWORD = 'YOUR_PASSWORD'
context = ssl.create_default_context()
url = 'https://jsonkeeper.com/b/52R3'

response = requests.get(url).json()

@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", response=response)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    success = ''
    return render_template("contact.html",success=success)

@app.route('/post<int:id>')
def post(id):
    ind = id-1
    display_post = response[ind]
    return render_template("post.html", display_post=display_post)

@app.route('/login',methods=["POST"])
def receive_data():
    success = ''
    if request.method == "POST":
        success = 'Email sent successfully'
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True, success=success)
    else:
        return render_template("contact.html", msg_sent=False, success=success)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls(context=context)
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)