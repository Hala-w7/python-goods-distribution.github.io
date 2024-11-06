# import Tkinter library
from tkinter import *
from tkinter import messagebox

# import the login screen from login_screen file
from login_screen import login_screen

# setting up the main application window
root = Tk()
root.title("Goods Distribution System") # window title

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width - 50}x{screen_height - 50}") # window size
root.configure(bg="#ba9dc4") # background color

# calling the login screen and launching it 
login_screen(root)

# start the main loop to keep the main window running
root.mainloop() 