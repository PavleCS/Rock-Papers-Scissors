from tkinter import *
import random

comp_options = ["rock", "paper", "scissors"]
user_choice = int
comp_choice = int
score = 0
winning_streak = 0

# ----- Reading High score file -----
with open("high_score.txt") as file:
    highest_score = file.read()
high_score = int(highest_score)


def writing_high_score():
    with open("high_score.txt", mode="w") as data:
        data.write(str(high_score))


def random_comp_choice():
    choice = random.choice(comp_options)
    return choice


def choice_to_number(choice):
    num = {"rock": 0, "paper": 1, "scissors": 2}
    return num[choice]


def number_to_choice(num):
    choice = {0: "rock", 1: "paper", 2: "scissors"}
    return choice[num]


def result(user, comp):
    global score
    global high_score
    global winning_streak
    res = ""

    if user == 0 and comp == 2:
        res += "You win!"
        winning_streak += 1
        score += 1
        if winning_streak > 0:
            if score >= high_score:
                high_score = score
                writing_high_score()
    elif comp == 0 and user == 2:
        res += "You lose"
        winning_streak = 0
        score = 0
    elif comp > user:
        res += "You lose"
        winning_streak = 0
        score = 0
    elif user > comp:
        res += "You win!"
        score += 1
        winning_streak += 1
        if winning_streak > 0:
            if score >= high_score:
                high_score = score
                writing_high_score()
    elif comp == user:
        res += "It's a draw"
        score = 0
        winning_streak = 0

    text = "Your choice: {yc} \nComputer choice: {cc} \nResult: {r}".format(yc=number_to_choice(user),
                                                                            cc=number_to_choice(comp), r=res)
    text_area.delete(1.0, END)
    text_area.insert(END, text)

    high_score_text_area.delete(1.0, END)
    high_score_text_area.insert(END, f"Current score: {score} \nHigh score: {high_score}")


FONT = "Arial"
SIZE = 10
STYLE = "bold"

# ----- UI -----
window = Tk()
window.title("Rock Paper Scissors")
window.config(pady=50, padx=50)
window.config(bg="#A0D8B3")

# ----- Canvas/Logo -----
canvas = Canvas(width=200, height=200, bg="#A0D8B3", highlightthickness=0)
icon_img = PhotoImage(file="icon.png")
icon_img = icon_img.subsample(2, 2)
canvas.create_image(100, 100, image=icon_img)
canvas.grid(row=0, column=0)

# ----- Main text area -----
text_area = Text(height=12, width=30, bg="#E5F9DB")
text_area.grid(row=1, column=0, pady=50)
text_area.insert(END, "Ready? \nClick the button")

# -----High score text area -----
high_score_text_area = Text(height=10, width=16, bg="#E5F9DB")
high_score_text_area.grid(row=0, column=1)
high_score_text = f"Current score: 0 \nHigh score: {high_score}"
high_score_text_area.insert(1.0, high_score_text)


# ----- Button Function -----
def rock():
    global user_choice
    global comp_choice

    user_choice = choice_to_number("rock")
    comp_choice = choice_to_number(random_comp_choice())
    result(user_choice, comp_choice)


def paper():
    global user_choice
    global comp_choice

    user_choice = choice_to_number("paper")
    comp_choice = choice_to_number(random_comp_choice())
    result(user_choice, comp_choice)


def scissors():
    global user_choice
    global comp_choice

    user_choice = choice_to_number("scissors")
    comp_choice = choice_to_number(random_comp_choice())
    result(user_choice, comp_choice)


# ----- Buttons -----
frame = Frame(window, width=10, bg="#E5F9DB")
frame.grid(row=1, column=1, padx=50)

rock_button = Button(frame, text="Rock", font=(FONT, SIZE, STYLE), width=10, highlightthickness=0, border=0,
                     bg="#A2A378", fg="white", command=rock)
rock_button.grid(row=0, column=1, pady=5, padx=20)

paper_button = Button(frame, text="Paper", font=(FONT, SIZE, STYLE), width=10, highlightthickness=0, border=0,
                      bg="#A2A378", fg="white", command=paper)
paper_button.grid(row=1, column=1, pady=10)

scissors_button = Button(frame, text="Scissors", font=(FONT, SIZE, STYLE), width=10, highlightthickness=0, border=0,
                         bg="#A2A378", fg="white", command=scissors)
scissors_button.grid(row=2, column=1, pady=5)

window.mainloop()
