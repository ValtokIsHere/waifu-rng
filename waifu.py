import random
from tkinter import *
from words import *

print('Current waifus: akeno, ')
print('Make sure the name is all lowercase!')
waifu = input("Please input the name of your waifu (currently wont do anything): ")

#a new chad word generator
def cbc(tex):
    return lambda : callback(tex)
def callback(tex):
    r = random.choice(words) + " "
    tex.insert(END, r,)
    tex.see(END)

root = Tk()
root.title('RNG')
root.geometry('500x300')
tex = Text(master=root, height=24)
tex.pack(side=BOTTOM)
bop = Frame()
bop.pack(side=BOTTOM)
button = Button(bop, text = 'talk', bd = '5', command=cbc(tex))
button.pack(side='top')

img = PhotoImage(file='akeno.ppm')

def toplevel():
    top = Toplevel()
    top.title(waifu)
    top.wm_geometry("380x530")
    imagething = Canvas(top)
    imagething.pack(fill=BOTH, expand=2)
    imagething.create_image(20,20, anchor=NW, image=img)

toplevel()
root.mainloop()

#todo:
#1. add more waifus!

