from tkinter import *
import cv2

from PIL import Image,ImageTk
import threading
import queue
import time


class App:

    def __init__(self):
        root = Tk()
        root.bind("<<update_gui>>", self.update_gui)
        frame = Frame(root)
        frame.pack()

        self.button = Button(
            frame, text="run", fg="red", command=self.on_start_button
            )
        self.button.pack(side=LEFT)
        
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        filename = '/home/levin/workspace/snrprj/snr/data/banknotes/sample_test/1/bmp/F001Z11479.bmp'
        w = Label(root, text=filename)
        w.pack()
        
        
        
        img = cv2.imread(filename, 0)

        self.photo = ImageTk.PhotoImage(Image.fromarray(img))
        self.note_image_widget = Label(root)
        self.note_image_widget.config(image=self.photo)
        self.note_image_widget.pack()
        
        root.after(100, self.update_gui)
        self.root = root
        return
    def worker(self):
        while True:
            self.worker_q.get()
            time.sleep( 3 )
            self.gui_q.put("update_gui")
            self.worker_q.task_done()
    def on_start_button(self):
#         self.root.event_generate("<<update_gui>>", when="tail")
        self.worker_q.put("work")
        return
        
        
    def run(self):
        #start the worker thread
        self.gui_q = queue.Queue()
        self.worker_q = queue.Queue()
        t = threading.Thread(target=self.worker)
        t.daemon = True
        t.start()
        self.root.mainloop()
        return
    def update_gui(self, *args):
        try:
            self.gui_q.get(0)
            self.gui_q.task_done()
            # Show result of the task if needed
            print("updating gui...")
            filename = '/home/levin/workspace/snrprj/snr/data/banknotes/sample_test/1/bmp/F001F29359.bmp'
            img = cv2.imread(filename, 0)
    
            self.photo = ImageTk.PhotoImage(Image.fromarray(img))
            self.note_image_widget.config(image=self.photo)
        except queue.Empty:
            pass
        
        self.root.after(100, self.update_gui)
        
        
        return

    def say_hi(self):
        print("hi there, everyone!")
        filename = '/home/levin/workspace/snrprj/snr/data/banknotes/sample_test/1/bmp/F001F29359.bmp'
        img = cv2.imread(filename, 0)

        self.photo = ImageTk.PhotoImage(Image.fromarray(img))
        self.note_image_widget.config(image=self.photo)

if __name__ == "__main__":   
    obj= App()
    obj.run()




# root.destroy() # optional; see description below