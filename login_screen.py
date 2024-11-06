# import Tkinter library & messagebox for displaying messages
from tkinter import *
from tkinter import messagebox

# import the main menu to display it after successful login
from main_menu import main_menu

# Dictionary to store valid login credentials for multiple users
users = {
    "admin": "1234",
    "hazem": "2222",
    "hala": "1111",
}
# number of allowed attempts
attempts = 3

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

# function to set up and display the login screen
def login_screen(root):
    # create the login window
    login_window = Toplevel(root)
    login_window.title("Login")  # window title
    login_window.geometry("400x250")  # window size
    login_window.configure(bg="#ba9dc4")  # background color

    # center the main menu window
    center_window(login_window)

    # user entry field
    Label(login_window, text="Username:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    username_entry = Entry(login_window, font=("Arial", 10, "bold"))
    username_entry.pack(pady=5)

    # password entry field
    Label(login_window, text="Password:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    password_entry = Entry(login_window, show="*", font=("Arial", 10, "bold"))
    password_entry.pack(pady=5)


    # function to validate login credentials
    def validate_login():
        global attempts
        username = username_entry.get()
        password = password_entry.get()

        # check if username exists and password matches
        if username in users and users[username] == password:
            # show successful message if the credentials are correct
            messagebox.showinfo("Success", "Logged in successfully!")
            login_window.destroy()  # close the login window 
            main_menu(root)  # open the main menu
        else:
            # decrease attempts if credentials are incorrect
            attempts -= 1
            if attempts > 0:
                # show error message with remaining attempts
                messagebox.showerror("Error", f"Incorrect data. {attempts} attempts left.")
            else:
                # quit program if attempts are exhausted
                messagebox.showerror("Error", "All attempts exhausted. Access denied.")
                login_window.destroy()
                root.quit()

    # Login button
    Button(login_window, text="Login", command=validate_login, width=10, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)
