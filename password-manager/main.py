from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savedata():
    website = website_entry.get()
    mail = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't left any fields")
    else:
        try:
            with open("saved_password.json", "r") as file:
                # json.dump(new_data, file, indent=4)
                data = json.load(file)
                data.update(new_data)
            with open("saved_password.json", "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("saved_password.json", "w") as file:
                json.dump(new_data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# -----------------------------search-----------------------------------#

def search_info():
    try:
        web_search = website_entry.get()
        # load json data
        with open("saved_password.json", "r") as file:
            search_data = json.load(file)
            search_email = search_data[f"{web_search}"]["email"]
            search_pwd = search_data[f"{web_search}"]["password"]
        messagebox.showinfo(title=f"{web_search} info", message=f"email: {search_email}\npassword: {search_pwd}")
    except KeyError:
        messagebox.showinfo(title="OOPS!!", message=f"please enter the correct entry of website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Builder")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(row=0, column=1)

label1 = Label(text="website")
label1.grid(row=1, column=0)
userName = Label(text="Email/Username")
userName.grid(row=2, column=0)
passwordLabel = Label(text="Password")
passwordLabel.grid(row=3, column=0)
search_btn = Button(text="search_info", width=14, command=search_info)
search_btn.grid(row=1, column=2)
Generate_pwd = Button(text="Generate Password", command=generate_password)
Generate_pwd.grid(row=3, column=2)
Add = Button(text="Add", width=36, command=savedata)
Add.grid(row=4, column=1, columnspan=2)
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=43)
email_entry.insert(0, "aravind.merugu2610@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

window.mainloop()
