import tkinter
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk() # Create the main window of tkinter
root.title("Use matplotlib in tkinter")

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111) # Add subgraph: 1 row, 1 column, 1st

# Generate data for drawing sin graph
x = np.arange(0, 3, 0.01)
y = np.sin(2 * np.pi * x)

# Draw on the sub-picture obtained earlier
a.plot(x, y)

# Display the drawn graphics to tkinter: create a canvas canvas belonging to root, and place the figure f on the canvas
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw() # Note that the show method is outdated, use draw here instead
canvas.get_tk_widget().pack(side=tkinter.TOP, # align top
                                                        fill=tkinter.BOTH, # fill method
                                                        expand=tkinter.YES) # adjust with window size adjustment

# matplotlib's navigation toolbar is displayed (it will not be displayed by default)
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=tkinter.TOP, # get_tk_widget() gets _tkcanvas
                     fill=tkinter.BOTH,
                     expand=tkinter.YES)


def on_key_event(event):
        """Keyboard Event Handling"""
        print("You pressed %s"% event.key)
        key_press_handler(event, canvas, toolbar)


# Bind the keyboard event handler function defined above
canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
        """Call this function when clicking the exit button"""
        root.quit() # End the main loop
        root.destroy() # destroy the window


# Create a button and bind the above function
button = tkinter.Button(master=root, text="quit", command=_quit)
# Button below
button.pack(side=tkinter.BOTTOM)

# Main loop
root.mainloop()