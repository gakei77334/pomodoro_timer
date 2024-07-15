from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    ticks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
        
    # If it's the 8th rep: (Long Break)
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # If its the 2nd/4th/6th rep: (Short Break)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    else:    
        count_down(work_sec)
        timer_label.config(text="Timer", fg=GREEN)
        
    count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        ticks.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 46))
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, borderwidth=0, highlightthickness=0, font=(FONT_NAME, 16), command=start_timer)
start_button.grid(column=0, row=2)


ticks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
ticks.grid(column=1, row=3)


reset_button = Button(text="Reset", bg=YELLOW, borderwidth=0, highlightthickness=0, font=(FONT_NAME, 16), command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()