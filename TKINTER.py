import tkinter as tk
import tkinter.font as tkFont
import sys,time


from displaywindow import *
from patterns import *

class mainui():
    def __init__(self,master):
        self.master = master
        self.title_screen_widgets = []
        self.mode_screen_widgets = []
        self.about_screen_widgets = []
        self.help_screen_widgets = []
        self.pattern_screen_widgets = []

    def title_screen(self,master):
        for elem in self.mode_screen_widgets:
            elem.place_forget()
        for elem in self.about_screen_widgets:
            elem.place_forget()
        for elem in self.help_screen_widgets:
            elem.place_forget()


        heading = tk.Label(self.master,text="Conway's Game Of life",font=heading_font,bg="black",fg="white")
        heading.place(x=450,y=50)
        self.title_screen_widgets.append(heading)

        enter_button = tk.Button(self.master, text = "Play Conway's Game Of Life",font = button_font,
                                 bg="black",fg="white",relief="solid",command = lambda: self.mode_select(master))
        enter_button.place(x=50,y=300)
        self.title_screen_widgets.append(enter_button)

        about_button = tk.Button(self.master, text = "About",font = button_font,
                                 bg="black",fg="white",relief="solid",command = lambda: self.about(master))
        about_button.place(x=50,y=400)
        self.title_screen_widgets.append(about_button)

        exit_button = tk.Button(self.master, text = "Exit",font = button_font,
                                 bg="black",fg="white",relief="solid",command = self.exit)
        exit_button.place(x=50,y=500)
        self.title_screen_widgets.append(exit_button)

        secret_button = tk.Button(self.master,image = stopsign,bg="black",relief="solid",
                                  command = lambda: self.snake(gameloop))
        secret_button.place(x=0,y=0)
        self.title_screen_widgets.append(secret_button)


    def mode_select(self,master):
        for elem in self.title_screen_widgets:
            elem.place_forget()
        for elem in self.pattern_screen_widgets:
            elem.place_forget()


        mode_select_heading = tk.Label(self.master,text="Select what mode to play in",font=heading_font,
                                       bg="black",fg="white")
        mode_select_heading.place(x=400,y=50)
        self.mode_screen_widgets.append(mode_select_heading)

        freeplay_button = tk.Button(self.master, text = "Free play",font = button_font,
                                 bg="black",fg="white",relief="solid",command = self.master.destroy)
        freeplay_button.place(x=50,y=300)
        self.mode_screen_widgets.append(freeplay_button)

        pattern_button = tk.Button(self.master, text = "Premade patterns",font = button_font,
                                 bg="black",fg="white",relief="solid",command = lambda: self.pattern_select(master))
        pattern_button.place(x=50,y=400)
        self.mode_screen_widgets.append(pattern_button)

        back_button = tk.Button(self.master, text = "Back",font = button_font,
                                 bg="black",fg="white",relief="solid",command = lambda: self.title_screen(master))
        back_button.place(x=50,y=900)
        self.mode_screen_widgets.append(back_button)


    def pattern_select(self,master):
        for elem in self.mode_screen_widgets:
            elem.place_forget()

        pattern_select_heading = tk.Label(self.master,text="Select which pattern to use",font=heading_font,
                                       bg="black",fg="white")
        pattern_select_heading.place(x=400,y=50)
        self.pattern_screen_widgets.append(pattern_select_heading)

        glidergun_button = tk.Button(self.master,image=patternimage1,bg="black",relief = "solid",
                                     command = lambda: self.patterntype1(boxsize,window,cell_color,cells_added))
        glidergun_button.place(x=725,y=550)
        self.pattern_screen_widgets.append(glidergun_button)

        pulsar_button = tk.Button(self.master,image=patternimage2,bg="black",relief = "solid",
                                  command = lambda: self.patterntype2(boxsize,window,cell_color,cells_added))
        pulsar_button.place(x=400,y=500)
        self.pattern_screen_widgets.append(pulsar_button)

        ship_button = tk.Button(self.master,image=patternimage3,bg="black",relief = "solid",
                                command = lambda: self.patterntype3(boxsize,window,cell_color,cells_added))
        ship_button.place(x=1300,y=500)
        self.pattern_screen_widgets.append(ship_button)

        glidergun_label = tk.Label(self.master,text="Glider gun",font=button_font,
                                   bg="black",fg="white")
        glidergun_label.place(x=850,y=500)
        self.pattern_screen_widgets.append(glidergun_label)

        pulsar_label = tk.Label(self.master,text="18-step oscillator",font=button_font,
                                   bg="black",fg="white")
        pulsar_label.place(x=400,y=450)
        self.pattern_screen_widgets.append(pulsar_label)

        ship_label = tk.Label(self.master,text="Flying Machine",font=button_font,
                                   bg="black",fg="white")
        ship_label.place(x=1300,y=450)
        self.pattern_screen_widgets.append(ship_label)

        back_button = tk.Button(self.master, text = "Back",font = button_font,
                                 bg="black",fg="white",relief="solid",command = lambda: self.mode_select(master))
        back_button.place(x=50,y=900)
        self.pattern_screen_widgets.append(back_button)


    def about(self,master):
        for elem in self.title_screen_widgets:
            elem.place_forget()

        about_label = tk.Label(self.master, text = "About :\n\nThis is a student made project which recreates the famous \"zero player game\" conway\'s game of life.\nIt is a cellular simulation, and in it we simulate the state of a cell.\nA cell can be either dead or alive.\nThe state of a cell is dependent on how many alive cells there are next to it.\n\nThe rules of the simulation are simple. They are:\n\n1. If a cell has 2 or 3 alive cells next to it then the cell will live\n\n2. If a cell has more than 3 alive cells next to it then the cell will die\n\n3. If a cell has lesser than 2 alive cells next to it then the cell will die\n\n4. If a dead cell has exactly 3 alive cells next to it then the cell will become alive",
                               font=button_font,bg="black",fg="white",justify="left")  
        about_label.place(x=100,y=200)
        self.about_screen_widgets.append(about_label)

        back_button = tk.Button(self.master, text = "Back",font = button_font,
                                 bg="black",fg="white",relief="solid",command = lambda: self.title_screen(master))
        back_button.place(x=50,y=900)
        self.about_screen_widgets.append(back_button)

    def patterntype1(self,boxsize,window,cell_color,cells_added):
        pattern1(boxsize,window,cell_color,cells_added)
        self.master.destroy()

    def patterntype2(self,boxsize,window,cell_color,cells_added):
        pattern2(boxsize,window,cell_color,cells_added)
        self.master.destroy()

    def patterntype3(self,boxsize,window,cell_color,cells_added):
        pattern3(boxsize,window,cell_color,cells_added)
        self.master.destroy()

    def snake(self,gameloop):
        self.master.destroy()
        snake(gameloop)

    def exit(self):
        sys.exit()



root = tk.Tk()
root.attributes("-fullscreen",True)
root.title("Conway's Game Of Life")
root.configure(bg = "black")

patternimage1 = tk.PhotoImage(file = "pattern1.png")
patternimage2 = tk.PhotoImage(file = "pattern2.png")
patternimage3 = tk.PhotoImage(file = "pattern3.png")
stopsign = tk.PhotoImage(file = "Stop_sign.png")

heading_font = tkFont.Font(family="LEMON MILK light",size=50)
button_font = tkFont.Font(family="LEMON MILK light",size=20)



program = mainui(root)
program.title_screen(root)

root.mainloop()


