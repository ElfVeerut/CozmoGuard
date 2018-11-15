import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import cam
import cv2
import facerec3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import requests

def cozmoguard():
    print(requests.get('http://127.0.0.1:5000/cozmoguardOpen').text)

def cozmoguardClose():
    print(requests.get('http://127.0.0.1:5000/cozmoguardClose').text)
 
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Scan , Controller, Register, Setting):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="COZM0 GUARD", font=("controller.title_font", 50, "bold italic"))
#        label.config(font=)
        label.pack(side="top", fill="x", padx=50, pady=50)

        button1 = tk.Button(self, text="Scan",
                            command=lambda: controller.show_frame("Scan"))
        button2 = tk.Button(self, text="Controller",
                            command=lambda: controller.show_frame("Controller"))
        button3 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("Register"))
        button4 = tk.Button(self, text="Setting",
                            command=lambda: controller.show_frame("Setting"))
        button1.config(font="System, 20")
        button1.pack(pady=10)
        button2.config(font="System, 20")
        button2.pack(pady=10)
        button3.config(font="System, 20")
        button3.pack(pady=10)
        button4.config(font="System, 20")
        button4.pack(pady=10)


class Scan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scan", font=("controller.title_font", 50, "bold italic"))
        label.pack(side="top", fill="x", padx=50, pady=50)
        button = tk.Button(self, text="Scan",
                           command=lambda: facerec3.facerec())
        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.config(font="System, 30")
        button.pack()
        button2.config(font="System, 30")
        button2.pack()

class Controller(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Controller", font=("controller.title_font", 50, "bold italic"))
        label.pack(side="top", fill="x", padx=50, pady=50)
        button = tk.Button(self, text="Open",
                           command= cozmoguard)
        button1 = tk.Button(self, text="Close",
                           command= cozmoguardClose)
        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.config(font="System, 30")
        button.pack()
        button1.config(font="System, 30")
        button1.pack()
        button2.config(font="System, 30")
        button2.pack()

class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Face Registering", font=("controller.title_font", 50, "bold italic"))
        label.grid(row=0,ipadx=50, ipady=50)

        registerentry = tk.Entry(self)
        registerentry.grid(row=2)
        registerentry.config(width="30")
        button = tk.Button(self, text="Submit",
                           command=lambda: cam.cam(registerentry.get()))
        button.bind("<Button-1>",lambda:controller.show_frame("StartPage") )
        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        
        label1= tk.Label(self,text="Username")
        label1.config(font="System, 40")
        label1.grid(row=1)
        button.config(font="System, 30")
        button.grid(row=3)
        button2.config(font="System, 30")
        button2.grid(row=4)

        #tum username laew hai mun popup camera to take pic #milestone 2

class Setting(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Setting", font=("controller.title_font", 50, "bold italic"))
        label.pack(side="top", fill="x", padx=50, pady=50)
        button = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.config(font="System, 30")
        button.pack()

 
    
    


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
