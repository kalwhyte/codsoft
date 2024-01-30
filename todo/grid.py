import tkinter as tk
win = tk.Tk()
for i in range(8):
    for j in range(6):
        frame = tk.Frame(
            master = win,
            relief= tk.RAISED,
            borderwidth= 2
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label =tk.Label(master=frame, text=f"Row {i}\nColumn{j}")
        label.pack()
win.mainloop()