from tkinter import *


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
text = "placeholder"
text_area.insert(1.0, text)

# -----High score text area -----
high_score_text_area = Text(height=10, width=12, bg="#E5F9DB")
high_score_text_area.grid(row=0, column=1)
high_score_text = "High-score:"
high_score_text_area.insert(1.0, high_score_text)

# ----- Buttons -----
frame = Frame(window, width=10, bg="#E5F9DB")
frame.grid(row=1, column=1, padx=50)

rock_button = Button(frame, text="Rock", font=(FONT, SIZE, STYLE), width=10, highlightthickness=0, border=0,
                     bg="#A2A378", fg="white")
rock_button.grid(row=0, column=1, pady=5, padx=20)

paper_button = Button(frame, text="Paper", font=(FONT, SIZE, STYLE), width=10, highlightthickness=0, border=0,
                      bg="#A2A378", fg="white")
paper_button.grid(row=1, column=1, pady=10)

scissors_button = Button(frame, text="Scissors", font=(FONT, SIZE, STYLE), width=10, highlightthickness=0, border=0,
                         bg="#A2A378", fg="white")
scissors_button.grid(row=2, column=1, pady=5)

window.mainloop()
