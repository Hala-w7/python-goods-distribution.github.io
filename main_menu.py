# import Tkinter library 
from tkinter import *

# import other screens
from import_goods import import_goods_screen
from export_goods import export_goods_screen
from branches_management import branches_menu
from statistics_screen import statistics_screen
from exported_goods_to_branches import distribution_screen

# function to center the window on the screen
def center_window(window):
    # Update the window to get the most recent size and geometry
    window.update_idletasks() 

    # Get the current width and height of the window
    width = window.winfo_width()
    height = window.winfo_height()

    # Calculate the x and y coordinates to center the window
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)

    # Set the new geometry for the window to position it at the center of the screen
    window.geometry(f"{width}x{height}+{x}+{y}")

# function to set up and display the main menu
def main_menu(root):
    # create the main menu window
    main_menu_window = Toplevel(root) 
    main_menu_window.title("Main Menu")  # window title
    main_menu_window.geometry("500x400")  # window size
    main_menu_window.configure(bg="#ba9dc4")  # background color

    # center the main menu window
    center_window(main_menu_window)

    # Frame to hold the buttons, placed in the middle of the window with padding
    button_frame = Frame(main_menu_window, bg="#ba9dc4")
    button_frame.pack(expand=True, pady=30)  # Adjust `pady` to control vertical positioning

    # Button dimensions
    button_width = 20
    button_height = 1

    # main menu buttons to access other screens
    Button(button_frame, text="Imported Goods", command=lambda: import_goods_screen(root), width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Export Goods", command=lambda: export_goods_screen(root), width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Distribution Options", command=lambda: distribution_screen(root), width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Branch Management", command=lambda: branches_menu(root), width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Statistics", command=lambda: statistics_screen(root), width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)


