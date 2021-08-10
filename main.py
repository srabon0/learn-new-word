from tkinter import *

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}
try:
    word_data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_word_data = pd.read_csv('data/french_words.csv')
    to_learn = original_word_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text='french',fill='black')
    canvas.itemconfig(word,text=current_card['French'],fill='black')
    canvas.itemconfig(front_ground,image=front_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(title,text="English",fill='white')
    canvas.itemconfig(word, text =current_card["English"],fill='white')
    canvas.itemconfig(front_ground,image=back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv')

    next_card()




window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,func=flip_card)
canvas = Canvas(width=800,height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

front_ground = canvas.create_image(400,263,image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400,150,text="",font=('Ariel',25,'italic'))
word = canvas.create_text(400,245,text="",font=('Ariel',50,'bold'))
canvas.grid(row=0,column=0,columnspan=2)
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
button_right = Button(image=right,command=is_known, highlightthickness=0)
button_right.grid(row=1,column=0)
button_wrong = Button(image=wrong,command=next_card, highlightthickness=0)
button_wrong.grid(row=1,column=1)

next_card()
window.mainloop()
