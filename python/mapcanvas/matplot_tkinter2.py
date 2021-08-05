import math
import numpy as np   
#-------------------------------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg #NavigationToolbar2TkAgg
#------------------------------------------------------------------------------------------
import tkinter as tk
#------------------------------------------------------------------------------------------
 
 
mpl.rcParams['font.sans-serif'] = ['SimHei'] #Chinese display
mpl.rcParams['axes.unicode_minus']=False #negative sign display
 
class From:
    def __init__(self): 
        self.root=tk.Tk() #Create the main form
        self.canvas=tk.Canvas() #Create a canvas to display graphics
        self.figure=self.create_matplotlib() #Return figure object of figure drawn by matplotlib
        self.create_form(self.figure) #Display the figure above the tkinter form
        self.root.mainloop()
 
    def create_matplotlib(self):
                 #Create drawing object f
        f=plt.figure(num=2,figsize=(16,12),dpi=80,facecolor="pink",edgecolor='green',frameon=True)
                 #Create a sub-picture
        fig1=plt.subplot(1,1,1)
 
        x=np.arange(0,2*np.pi,0.1)
        y1=np.sin(x)
        y2=np.cos(x)
 
        line1,=fig1.plot(x,y1,color='red',linewidth=3,linestyle='--') #Draw the first line
        line2,=fig1.plot(x,y2) 
        plt.setp(line2,color='black',linewidth=8,linestyle='-',alpha=0.3)# second line

        fig1.set_title("This is the first picture",loc='center',fontsize='xx-large',color='red') #Set title
        line1.set_label("Sine curve") #Determine the legend
        fig1.legend(['Sine','Cosine'],loc='upper left',facecolor='green',frameon=True,shadow=True,framealpha=0.5,fontsize='xx-large')

        fig1.set_xlabel('abscissa') #Determine the axis title
        fig1.set_ylabel("ordinate")
        fig1.set_yticks([-1,-1/2,0,1/2,1]) #Set the coordinate axis scale
        fig1.grid(which='major', axis='x', color='r', linestyle='-', linewidth=2) #set grid
        
        return f
 
    def create_form(self,figure):
                 #Display the drawn graphics on the tkinter window
        self.canvas=FigureCanvasTkAgg(figure,self.root)
        self.canvas.draw() #The previous version used the show() method. After matplotlib 2.2, it is no longer recommended to use show() instead of draw, but using show will not report an error and will display a warning.
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
        #Display the navigation toolbar drawn by matplotlib on the tkinter window
        toolbar =NavigationToolbar2TkAgg(self.canvas, self.root) #matplotlib 2.2 version is recommended to use NavigationToolbar2Tk, if you use NavigationToolbar2TkAgg will warn
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
if __name__=="__main__":
    form=From()
