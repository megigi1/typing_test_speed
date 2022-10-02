from tkinter import *
import random
import time


# Constant

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer = None
WORK_MIN = 1


window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50, bg=YELLOW)

def click():
    button.destroy()
    canvas.delete('all')
    # typing_label.config(text="This is this")
    buttons()


def buttons():
    entry_window = Entry(width=15)
    entry_window.grid(column=1, row=2)
    entry_window.icursor(0)


    text =  "Cut off all of your hair Did you flinch did you care Did he look, did he stop and stare At your brand Local boy, local news Power lines, hangin' boots Firemen in their trucks cut loose A local boy's shoes Cadillac, Cadillac Business men dressed in slacks I'ma buy one for us when I get back A big Cadillac And you can wave to all of your friends And I'll never leave you again Would you write, would you call back, baby If I wrote you a song? I been gone but you're still my lady And I need you at home Romeo, Juliet Balcony silhouette Makin' o's  with her cigarette It's Juliet Flapper girl, flapper girl Prohibition in curls Hair of gold and a neck of pearls It's flapper girl And  you can wave to all of your friends And I'll never leave you again Would you write, would you call back, baby If I wrote you a song? I been gone but you're still my lady And I need you at home because If you ain't behind my door Then I ain't got a home anymore Would you write, would you call back, baby"
    new_text = random.choice(text.split())
    text_label = Label(text= new_text, bg=YELLOW, font=(FONT_NAME, 70, "bold"))
    text_label.grid(column=1, row=1)

    t0 = time.time()

    def calculate():
        t1 = time.time()
        st = entry_window.get()

        mylabel = Label(window, text="TIME TAKEN: " + str(round(t1 - t0)))
        mylabel.grid(column=4, row=1)
        if (t1 - t0) >= 60:
            mylabel = Label(window, text="SPEED: POOR")
            mylabel.grid(column=2, row=1)
        elif (t1 - t0) >= 30 and (t1 - t0) <= 60:
            mylabel = Label(window, text="SPEED: AVERAGE")
            mylabel.grid(column=2, row=1)
        else:
            mylabel = Label(window, text="SPEED: EXCELLENT")
            mylabel.grid(column=2, row=1)

        def text_next():
            if str(st) == text_label.cget("text"):
                entry_window.delete(0, 'end')
                text_label.config(text=random.choice(text.split()))
                print("yes")
                count = 0
                w_count = len(st.split())
                mylabel = Label(window, text="TOTAL WORDS: " + str(count + w_count))
                mylabel.grid(column=3, row=1)
            else:
                print("no")


        text_next()


    text_type_btn = Button(window, text="RESULT", font="helvetica 20", padx=10, pady=10, relief=RAISED,
                           command=calculate).grid(column=2, row=2)



# Creating first page of screen
typing_label = Label(text="Let's Start Typing!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
typing_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
info_label = canvas.create_text(100, 130, text="Press start when you are ready!", fill="black", font=(FONT_NAME, 10, "bold"))
canvas.grid(column=1, row=1)

button = Button(text="START", bg=YELLOW, command=click)
button.grid(column=1, row=1)




window.mainloop()