from tkinter import *

#this shoudld do the trick for now...
def image():
    root2 = Tk()
    photothing = Canvas(root2, width = 380, height = 530)
    photothing.pack()
    img = PhotoImage(file="akeno.ppm")
    photothing.create_image(20,20, anchor=NW, image=img)
    mainloop()
