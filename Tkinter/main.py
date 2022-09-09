from tkinter import *

window = Tk()
window.title("MY first GUI program")
window.config(padx=20,pady=20)


def on_button_clicked():
    my_label.config(text=f"{round((float(user_input.get())*1.609),2)}")


user_input = Entry(width=10)
user_input.grid(column=1, row=0)

my_label = Label(text="0", font=("Courier", 12, "normal"))
my_label.grid(column=1, row=1)

my_label_1 = Label(text="miles", font=("Courier", 12, "normal"))
my_label_1.grid(column=2, row=0)

my_label_2 = Label(text="is equal to", font=("Courier", 12, "normal"))
my_label_2.grid(column=0, row=1)

my_label_3 = Label(text="km", font=("Courier", 12, "normal"))
my_label_3.grid(column=2, row=1)

button = Button(text="Click ME!", command=on_button_clicked)
button.grid(column=1, row=2)

window.mainloop()

# # def add(*args):
# #     sum=0
# #     for n in args:
# #         sum+=n
# #     return sum
# #
# # print(add(5,6,7,8))
#
# class car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw.get("model")
#
#
# my_car = car(make="Nissan")
# print(my_car.model, my_car.make)
