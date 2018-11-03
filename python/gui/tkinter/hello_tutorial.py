import tkinter as tk

counter = 0 
stop_count = False
def counter_label(label, root):
	def count():
		global counter
		if stop_count:
				return
		counter += 1
		label.config(text=str(counter))
		root.after(1000, count)
	count()

def stop_count_fun():
	global stop_count
	stop_count = True
	return 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label, root)
button = tk.Button(root, text='Stop', width=25, command=stop_count_fun)
button.pack()
root.mainloop()