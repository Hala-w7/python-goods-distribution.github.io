# Import Tkinter library and messagebox for displaying messages
from tkinter import *
from tkinter import messagebox

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

# Function to edit branch information
def edit_branch(branch):
    # Create the edit window
    edit_window = Toplevel()
    edit_window.title("Edit Branch")
    edit_window.geometry("400x350")
    edit_window.configure(bg="#ba9dc4")

    # Center the edit window
    center_window(edit_window)

    # Label to prompt the user to choose which field to edit
    Label(edit_window, text="Select Field to Edit:", bg="#ba9dc4", fg="white", font=("Arial", 12, "bold")).pack(pady=5)

    # Variable to store the selected field (name or location)
    field_choice = StringVar()
    field_choice.set("name")  # Default selection

    # Radio button for editing the branch name
    Radiobutton(edit_window, text="Edit Branch Name", variable=field_choice, value="name", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(anchor=W, padx=20, pady=5)
    
    # Radio button for editing the branch location
    Radiobutton(edit_window, text="Edit Branch Location", variable=field_choice, value="location", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(anchor=W, padx=20, pady=5)

    # Label and entry to input the new value
    Label(edit_window, text="Enter New Value:", bg="#ba9dc4", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
    edit_entry = Entry(edit_window, font=("Arial", 10))
    edit_entry.pack(pady=5)

    # Function to save the edited information
    def save_edited_info():
        # Get the selected field to edit (name or location)
        field = field_choice.get()
        new_info = edit_entry.get()  # Get the new value from the entry field

        # Validate if the new value is provided
        if not new_info:
            messagebox.showerror("Error", "The field cannot be empty.")
            return

        # Update the branch information based on the selected field
        if field == "name":
            branch["name"] = new_info  # Update the branch name
        elif field == "location":
            branch["location"] = new_info  # Update the branch location

        # Success message and close the edit window
        messagebox.showinfo("Success", "Branch information updated successfully.")
        edit_window.destroy()

    # Button to save changes
    Button(edit_window, text="Save Changes", command=save_edited_info, bg="#9c81a6", fg="white", font=("Arial", 10, "bold")).pack(pady=20)


