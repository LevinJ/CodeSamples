from _cffi_backend import string

from astropy.units import uP
try:
    from tkinter import *
except:
    from Tkinter import *
import cv2
import os
import sys


class App():

    def __init__(self):

        root = Tk()
        root.title("AIWAYS Camera Data Collection Tool")
        frame = Frame(root)
        frame.pack()
     

        self.button_start = Button(frame, text="Start",  command=self.button_start_fun).pack(side=LEFT)
        self.button_puase = Button(frame, text="Pause",  command=self.button_pause_fun).pack(side=LEFT)
        self.button_stop = Button(frame, text="Stop",  command=self.button_stop_fun).pack(side=LEFT)
        
        self.show_stream_var = IntVar()
        Checkbutton(frame, text="Show Stream", variable=self.show_stream_var).pack(side=LEFT)
        
        
        #image stream information
        frame = Frame(root)
        frame.pack()
        self.image_stream_var = StringVar()
        Label(root, textvariable=self.image_stream_var).pack()
        
        
        #insert ground truth region
        frame = Frame(root)
        frame.pack()
        self.button_insert = Button(frame, text="insert",  command=self.button_insert_fun).pack(side=LEFT)
        Label(frame, text="World X:").pack(side=LEFT)
        self.entry_x = Entry(frame).pack(side=LEFT)
        Label(frame, text="World Y:").pack(side=LEFT)
        self.entry_y = Entry(frame).pack(side=LEFT)
        
      
           
#         root.after(1, self.update_gui)
        #initialize the GUI
        self.image_stream_var.set("no image stream yet!")
        self.show_stream_var.set(1)
        self.root = root
        return
    def button_start_fun(self):
        return
    def button_pause_fun(self):
        return
    def button_stop_fun(self):
        return
    def button_insert_fun(self):
        return
    

        
        
    def run(self):
        self.root.mainloop()

        return
    def update_gui(self, *args):
        
        self.root.after(1, self.update_gui)
            
        return

    

if __name__ == "__main__":   
    obj= App()
    obj.run()



