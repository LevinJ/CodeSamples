import Tkinter as tk
import random
import math

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
       
 
        self.button_track = tk.Button(self, text="Reset",  command=self.button_track_fun)
        self.button_revert = tk.Button(self, text="Revert",  command=self.button_revert_fun)
        # self.button_track.pack(side=tk.LEFT)
        
        self.canvas = tk.Canvas(self, width=400, height=400, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.button_track.grid(row=2, column=0)
        self.button_revert.grid(row=3, column=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Plot some rectangles
        for n in range(50):
            x0 = random.randint(0, 900)
            y0 = random.randint(50, 900)
            x1 = x0 + random.randint(50, 100)
            y1 = y0 + random.randint(50,100)
            color = ("red", "orange", "yellow", "green", "blue")[random.randint(0,4)]
            self.canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill=color, activefill="black", tags=n)
        self.canvas.create_text(50,10, anchor="nw", text="Click and drag to move the canvas\nScroll to zoom.")

        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)
        self.origX = self.canvas.xview()[0]
        self.origY = self.canvas.yview()[0]
        self.scale_histroy = []
        return
    def button_revert_fun(self):
        self.view_revert(revert_all = False)
        return
    def view_revert(self, revert_all = True):
        if(len(self.scale_histroy) == 0):
            return
        if revert_all:
            for sc in reversed(self.scale_histroy):
                self.canvas.scale(*sc)
            self.scale_histroy = [] 
        else:
            _, lastx, lasty, _, _ = self.scale_histroy[-1]
            while True:
                self.canvas.scale(*self.scale_histroy[-1])
                del self.scale_histroy[-1]
                if(len(self.scale_histroy) == 0):
                    break
                _, nextx, nexty, _, _ = self.scale_histroy[-1]
                gap = (lastx - nextx) *  (lastx - nextx)  + (lasty - nexty) * (lasty - nexty)
                gap = math.sqrt(gap)
                if(gap > 1):
                    break
                    
        
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))    
        
        
        
        self.canvas.xview_moveto(self.origX)
        self.canvas.yview_moveto(self.origY)
        return
    def button_track_fun(self):  
        print("button clicked")  
        self.view_revert()
        
        
       
        return

    #move
    def move_start(self, event):
        print ("start uv={}".format([event.x,event.y]))
        self.canvas.scan_mark(event.x, event.y)
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        print ("canvas xy={}".format([x,y]))
    def move_move(self, event):
        # print ("move uv={}".format([event.x,event.y]))
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    #windows zoom
    def zoomer(self,event):
        print ("zoomer uv={}".format([event.x,event.y]))
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #linux zoom
    def zoomerP(self,event):
        print ("zoomerP uv={}".format([event.x,event.y]))
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        self.canvas.scale("all", x, y, 1.1, 1.1)
        
        self.scale_histroy.append(("all", x, y, 1/1.1, 1/1.1))
        # self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
       
        print ("canvas xy={}".format([x,y]))
    def zoomerM(self,event):
        print ("zoomerM uv={}".format([event.x,event.y]))
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()