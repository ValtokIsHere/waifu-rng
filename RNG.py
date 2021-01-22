import random
from tkinter import *
from Window import image

#i know this is utterly fucking terrible but it works
def rng():
    rng = random.randint(0, 20)
    if rng == 0:
        print("konichiwa")
    elif rng == 1:
        print("onii chan")
    elif rng == 2:
        print("yes")
    elif rng == 3:
        print("no")
    elif rng == 4:
        print("okay")
    elif rng == 5:
        print("beautiful")
    elif rng == 6:
        print("why")
    elif rng == 7:
        print("as")
    elif rng == 8:
        print("go")
    elif rng == 9:
        print("house")
    elif rng == 10:
        print("tomorrow")
    elif rng == 11:
        print("leave")
    elif rng == 12:
        print("not")
    elif rng == 13:
        print("serious")
    elif rng == 14:
        print("amazing")
    elif rng == 15:
        print("if")
    elif rng == 16:
        print("glass")
    elif rng == 17:
        print("god")
    elif rng == 18:
        print("job")
    elif rng == 19:
        print("oh")
    else:
        print("who")

def printrng():
    rng()

printrng()
def shitass():
    root = Tk()
    root.geometry('300x300')
    button = Button(root, text = 'talk', bd = '5', command = printrng())
    button.pack(side = 'top')
    root.mainloop()

image()
shitass()


#still working on it dont worry

#todo:
#1. make both windows appear at the same time
#2. make the rng show some input on the window
#3. add more words
#4. add more waifus!

