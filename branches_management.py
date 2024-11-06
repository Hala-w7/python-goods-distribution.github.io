# Import Tkinter library and messagebox for displaying messages
from tkinter import *
from tkinter import messagebox
from edit_branch import edit_branch

# List to store branches
branches = []

# Function to center the window on the screen
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

# Function to set up and display the branches menu
def branches_menu(root):
    # Create the branches window
    branches_window = Toplevel(root)
    branches_window.title("Branches")  # Window title
    branches_window.geometry("400x350")  # Window size
    branches_window.configure(bg="#ba9dc4")  # Background color

    # Center the branches menu window
    center_window(branches_window)

    # Frame to hold the buttons, placed in the middle of the window with padding
    button_frame = Frame(branches_window, bg="#ba9dc4")
    button_frame.pack(expand=True, pady=30)  # Adjust `pady` to control vertical positioning

    # Button dimensions
    button_width = 20
    button_height = 1

    # Button to display all branches
    Button(button_frame, text="Show All Branches", command=show_all_branches, width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Delete Branch", command=delete_branch, width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Edit Branch Information", command=choose_branch_to_edit, width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)
    Button(button_frame, text="Add New Branch", command=add_branch, width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=10)

    Button(button_frame, text="Previous Screen", command=branches_window.destroy, width=button_width, height=button_height, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(side=BOTTOM, pady=10)

# Function to add a new branch
def add_branch():
    # Create a new window for adding a branch
    add_window = Toplevel()
    add_window.title("Add New Branch")
    add_window.geometry("400x250")
    add_window.configure(bg="#ba9dc4")

    # Center the add window
    center_window(add_window)

    # Entry fields for new branch
    Label(add_window, text="Branch Name:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    new_name_entry = Entry(add_window, font=("Arial", 10, "bold"))
    new_name_entry.pack(pady=5)

    Label(add_window, text="Branch Location:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    new_location_entry = Entry(add_window, font=("Arial", 10, "bold"))
    new_location_entry.pack(pady=5)

    # Function to save the new branch
    def save_new_branch():
        name = new_name_entry.get()  # Get the branch name
        location = new_location_entry.get()  # Get the branch location

        # Validate inputs
        if not name or not location:
            messagebox.showerror("Error", "Both fields are required.")
            return

        # Create a new branch dictionary and add it to the list
        branch = {
            "name": name,
            "location": location
        }

        # Add the new branch to the list
        branches.append(branch)
        messagebox.showinfo("Success", f"Branch '{name}' added successfully.")
        add_window.destroy()

    # Button to save the new branch
    Button(add_window, text="Add Branch", command=save_new_branch, bg="#9c81a6", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

# Function to display all branches
def show_all_branches():
    # Check if the list is empty
    if not branches:
        messagebox.showinfo("Information", "No branches available. Please add a branch.")  # Inform the user that there are no branches
    else:
        # Create a new window to display the branches
        branches_window = Toplevel()
        branches_window.title("Branches List")
        branches_window.geometry("300x300")
        branches_window.configure(bg="#ba9dc4")

        # Center the branches window
        center_window(branches_window)

        # Initialize an empty string to hold branch details
        branches_list = ""

        # Use a for loop to iterate through the branches
        for branch in branches:
            branches_list += f"{branch['name']} - {branch['location']}\n"  # Add each branch's details to the string

        # Create a Label to display the branches list
        Label(branches_window, text=branches_list, bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

# Function to delete a branch
def delete_branch():
    # Check if the list is empty
    if not branches:
        messagebox.showinfo("Information", "No branches available to delete. Please add a branch.")  # Inform the user that there are no branches
        return

    # Create a new window for branch selection
    delete_window = Toplevel()
    delete_window.title("Delete Branch")
    delete_window.geometry("300x200")
    delete_window.configure(bg="#ba9dc4")

    # Center the delete window
    center_window(delete_window)

    # List of branch names to display
    branch_names = [branch["name"] for branch in branches]

    # Function to show confirmation dialog
    def show_confirmation_dialog(branch_name):
        # Confirmation message
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the branch '{branch_name}'?")
        if confirm:  # If the user confirmed
            confirm_deletion(branch_name)  # Call the confirm_deletion function
        else:
            delete_window.destroy()  # Close the window if the user selected "No"

    # Function to confirm deletion
    def confirm_deletion(branch_name):
        for branch in branches:
            if branch["name"] == branch_name:
                branches.remove(branch)
                messagebox.showinfo("Success", f"Branch '{branch_name}' deleted successfully.")
                delete_window.destroy()
                return
        messagebox.showerror("Error", "Branch not found.")

    # Create buttons for each branch name
    for branch_name in branch_names:
        Button(delete_window, text=branch_name, command=lambda name=branch_name: show_confirmation_dialog(name), width=10, bg="#9c81a6", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# Function to choose a branch to edit
def choose_branch_to_edit():
    # Check if there are any branches
    if not branches:
        messagebox.showinfo("Information", "No branches available to edit.")
        return

    # Create a new window for choosing a branch
    choose_window = Toplevel()
    choose_window.title("Choose Branch to Edit")
    choose_window.geometry("300x200")
    choose_window.configure(bg="#ba9dc4")
    # Center the choose window
    center_window(choose_window)

    # Label to instruct the user
    Label(choose_window, text="Select a Branch to Edit:", bg="#ba9dc4", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

    for branch in branches:
        Button(choose_window, text=branch["name"], command=lambda b=branch: edit_branch(b), width=20, bg="#9c81a6", fg="white", font=("Arial", 10, "bold")).pack(pady=5)