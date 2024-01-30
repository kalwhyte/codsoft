import tkinter as tk
from tkinter import Listbox, ttk
from tkinter import messagebox
import sqlite3


# Define an empty list to store the tasks
""" This list will be used to store the tasks 
    that are added to the todo list
"""

tasks = []

# Create a function to add a task to the list
""" This function will be used to add the task to the list
    and also to the database
"""
def add_task():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute('create table if not exists tasks(task text)')
 
    # Get the task from the entry widget
    task = task_field.get()
    if len(task) == 0:
        messagebox.showerror("Error", "Task cannot be empty")
    else:
        # Add the task to the list
        c.execute('insert into tasks values (?)', (task,))
        conn.commit()
        tasks.append(task)
        list_update()
        task_field.delete(0, tk.END)


# Create a function to update the listbox
def list_update():
    # Clear the listbox
    clear_listbox()
    # Loop through the tasks list
    for task in tasks:
        # Add each task to the listbox
        listbox.insert(tk.END, task)


# Create a function to clear the listbox
def clear_listbox():
    try:
        # Get the selected entry
        selection = Listbox.get(listbox.curselection())

        # Remove the selected entry from the list
        if selection in tasks:
            tasks.remove(selection)

            list_update()

            cursor.execute('delete from tasks where task = (?)', (selection,))
    except:
        messagebox.showerror("Error", "No task selected")


# Create a function to delete all the tasks
def delete_all():
    # Display a message box to confirm the action
    confirm = messagebox.askyesno("Confirm", "Do you really want to delete all the tasks?")
    # Check if the user confirmed the action
    if confirm == True:
        # Clear the listbox
        clear_listbox()
        # Clear the tasks list
        tasks.clear()
        # Delete all the tasks from the database
        cursor.execute('delete from tasks')

        list_update()


# Create a function to clear list
def clear():
    # USing the delete_all function to clear the list
    Listbox.delete(0, tk.END)


def close():
    # Display a message box to confirm the action
    confirm = messagebox.askyesno("Confirm", "Do you really want to close the app?")
    # Check if the user confirmed the action
    if confirm == True:
        # Close the guiWindow
        guiWindow.destroy()


# Create a function to retrieve the tasks from the database
""" This function will be used to retrieve the tasks from the database
    and add them to the list
"""
def retrieve_tasks():
    # Get the tasks from the database
    tasks_db = cursor.execute('select * from tasks')
    # Loop through the tasks
    for task in tasks_db:
        # Add each task to the list
        tasks.append(task[0])
    # Update the listbox
    list_update()


# MAin function
""" This function will be used to create the GUI
    and also to connect to the database
"""
if __name__ == "__main__":
    # Create a guiWindow
    guiWindow = tk.Tk()
    # Set the title
    guiWindow.title("Todo App")
    # Set the size
    guiWindow.geometry("500x500+2050+250")
    # Disable resizing
    guiWindow.resizable(False, False)
    # Set the background color
    guiWindow.config(bg="lightblue")
 
# Using connect() method to connect to the database
conn = sqlite3.connect('todo.db')

# Using cursor() method to create a cursor object
cursor = conn.cursor()

# Using execute() method to create a table
cursor.execute('create table if not exists tasks(task text)')

# Using commit() method to save the changes
conn.commit()

# Using execute() method to retrieve the tasks from the database
tasks_from_db = cursor.execute('select * from tasks')

# defining frames using tk.Frame() widget
header_frame = tk.Frame(guiWindow, bg="lightblue")
function_frame = tk.Frame(guiWindow, bg="lightblue")
listbox_frame = tk.Frame(guiWindow, bg="lightblue")

# placing the frames using place() method
header_frame.pack(fill = "both")
function_frame.pack(side = "left", expand = True, fill = "both")
listbox_frame.pack(side = "right", expand = True, fill = "both")

# defining labels for the frames

label1 = tk.Label(header_frame,
                  text = "The ToDo List",
                  font = ("Brush Script MT", "30"),
                  bg = "lightblue",
                  fg = "black"
    )
label1.pack(padx = 20, pady = 20)

task_label = tk.Label(function_frame,
                  text = "Add Task",
                  font = ("Arial", "20"),
                  bg = "lightblue",
                  fg = "black"
                )
task_label.place(x = 30, y = 40)


# defining entry widgets for the frames
task_field = tk.Entry(
    function_frame,
    font = ("Arial", "15"),
    width =  18,
    fg="black",
    bg = "lightblue"
    )

task_field.place(x = 180, y = 40)

# defining buttons for the frames
add_task_button = tk.Button(
    function_frame,
    text = "Add Task",
    font = ("Arial", "15"),
    bg = "lightblue",
    fg = "black",
    command = add_task
    )
del_button = tk.Button(
    function_frame,
    text = "Delete",
    font = ("Arial", "15"),
    bg = "lightblue",
    fg = "black",
    command = clear_listbox
    )

del_all_button = tk.Button(
    function_frame,
    text = "Delete All",
    font = ("Arial", "15"),
    bg = "lightblue",
    fg = "black",
    command = delete_all
    )

exit_button = tk.Button(
    function_frame,
    text = "Exit",
    font = ("Arial", "15"),
    bg = "lightblue",
    fg = "black",
    command = close
    )

add_task_button.place(x = 30, y = 100)
del_button.place(x = 150, y = 100)
del_all_button.place(x = 2200, y = 100)
exit_button.place(x = 390, y = 100)

# defining listbox for the frames
listbox = tk.Listbox(
    listbox_frame,
    width =  26,
    height= 13,
    selectmode = "SINGLE",
    font = ("Arial", "15"),
    fg="black",
    bg = "lightblue"
    )

guiWindow = tk.Tk()  # Define the guiWindow variable

listbox.place(x = 30, y = 40)

# calling the mainloop() method
retrieve_tasks()
list_update()

guiWindow.mainloop()

# Using close() method to close the connection
conn.close()