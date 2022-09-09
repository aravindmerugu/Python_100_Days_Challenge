import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    check_marks.config(text="")
    canvas.itemconfig(canvas_timer, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.grid(column=1, row=1)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=PINK)
        count_down(long_break_sec)
        marks()
    elif REPS % 2 == 0:
        timer_label.config(text="SHORT BREAK", fg=RED)
        count_down(short_break_sec)
        marks()
    else:
        timer_label.config(text="WORK TIME!", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    if count >= 0:
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds in range(0, 10):
            seconds = f"0{seconds}"
        canvas.itemconfig(canvas_timer, text=f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", font=(FONT_NAME, 10, "normal"), bg=YELLOW, highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", font=(FONT_NAME, 10, "normal"), bg=YELLOW, highlightthickness=0,
                      command=reset_timer)
reset_button.grid(column=2, row=2)


def marks():
    marks = ""
    for _ in range(int(REPS / 2)):
        marks += "✔"
    check_marks.config(text=f"{marks}")


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
