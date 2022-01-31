from patterns import *
from tkinter import *
root = Tk()
boxsize = 10

def patterncaller(boxsize,cell_color,cells_added):
                pattern(boxsize,window,cell_color,cells_added)
mylabel1 = Label(root, text="CONWAY'S GAME OF LIFE",fg = "black",font=25, bd=1, relief="solid", )

mylabel1.pack()
mylabel2 = Label(root, text='Choose an option below',font = 18,  fg = "black", padx = 20, pady = 20)
mylabel2.pack()



root.configure(bg='light blue')


mybutton = Button(root, text= "game of life", fg="white", bg="black", padx = 15, pady = 10)
mybutton.pack()

mybutton2 = Button(root, text= "glider gun", fg="white", bg="black", padx = 15, pady = 10, command = patterncaller)
mybutton2.pack()
mybutton3 = Button(root, text= "pulsar", fg="white", bg="black", padx = 15, pady = 10, command = pattern1)
mybutton3.pack()
mybutton4 = Button(root, text= "flying machine", fg="white", bg="black", padx = 15, pady = 10, command = pattern2)
mybutton4.pack()



def myclick1():
    myLabel = Label(root, text='ABOUT:')
    myLabel.pack()

def myclick2():
    myLabel2 = Label(root, text='HELP:')
    myLabel2.pack()




mybutton5 = Button(root, text= "secret button", fg="white", bg="black", padx = 15, pady = 10)
mybutton5.pack()
mybutton6 = Button(root, text= "ABOUT", fg="white", bg="black", padx = 20, pady = 10, command = myclick1)
mybutton6.pack()
mybutton7 = Button(root, text= "HELP", fg="white", bg="black", padx = 20, pady = 10, command = myclick2)
mybutton7.pack()


buttonquit = Button(root, text="exit game of life ",fg="black",font=15, command = root.quit)
buttonquit.pack()
root.mainloop()
from displaywindow import *

game()