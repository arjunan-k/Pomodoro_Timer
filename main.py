from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#446A46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label1.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label1.config(text="WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    if count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        tick = ""
        for i in range(0, int(reps/2)):
            tick += "✔"
        label2.config(text=tick)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label1.grid(column=1, row=0)
button1 = Button(text="Reset", command=reset_timer)
button1.grid(column=3, row=3)
button2 = Button(text="Start", command=start_timer)
button2.grid(column=0, row=3)
label2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label2.grid(column=1, row=4)
window.mainloop()