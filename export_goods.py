# import Tkinter library and messagebox for displaying messages
from tkinter import *
from tkinter import messagebox
from import_goods import imported_goods

# list to store exported goods
exported_goods = []

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

# function to set up and display the exported goods screen
def export_goods_screen(root):
    # create the exported goods window
    export_window = Toplevel(root)
    export_window.title("Exported Goods")  # window title
    export_window.geometry("600x450")  # window size
    export_window.configure(bg="#ba9dc4")  # background color

    # center the main menu window
    center_window(export_window)

    # goods name entry field
    Label(export_window, text="Goods Name:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(20, 5))  # Padding for top and bottom
    name_entry = Entry(export_window, font=("Arial", 10, "bold"))
    name_entry.pack(pady=(0, 10))  # Padding for top and bottom

    # quantity entry field
    Label(export_window, text="Quantity:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5))  # Padding for top and bottom
    quantity_entry = Entry(export_window, font=("Arial", 10, "bold"))
    quantity_entry.pack(pady=(0, 10))  # Padding for top and bottom

    # export date entry field 
    Label(export_window, text="Export Date:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5))  # Padding for top and bottom
    export_date_entry = Entry(export_window, font=("Arial", 10, "bold"))
    export_date_entry.pack(pady=(0, 10))  # Padding for top and bottom

    # cost entry field
    Label(export_window, text="Cost:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5))  # Padding for top and bottom
    cost_entry = Entry(export_window, font=("Arial", 10, "bold"))
    cost_entry.pack(pady=(0, 10))  # Padding for top and bottom

    # export location entry field
    Label(export_window, text="Export Location:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5))  # Padding for top and bottom
    location_entry = Entry(export_window, font=("Arial", 10, "bold"))
    location_entry.pack(pady=(0, 20))  # Padding for top and bottom

    # function to reset the fields after adding goods
    def reset_fields():
        name_entry.delete(0, 'end')
        quantity_entry.delete(0, 'end')
        export_date_entry.delete(0, 'end')
        cost_entry.delete(0, 'end')
        location_entry.delete(0, 'end')

    # function to save entered goods data
    def save_export():
        try:
            # attempt to convert the input to an integer
            quantity = int(quantity_entry.get())
            if quantity < 0:  # check if quantity is negative
                raise ValueError("Quantity cannot be negative.")  # raise exception if negative

            cost = float(cost_entry.get())
            if cost < 0:  # check if cost is negative
                raise ValueError("Cost cannot be negative.")  # raise exception if negative

            # create a dictionary to store data and add it to the list
            good = {
                "name": name_entry.get(),
                "quantity": quantity,
                "export_date": export_date_entry.get(),
                "cost": cost,
                "location": location_entry.get()
            }
            exported_goods.append(good)

            # confirmation message after adding the goods
            messagebox.showinfo("Success", "Goods exported successfully")
            show_completion_screen()


        except ValueError as e:
            # show error message if input is invalid
            messagebox.showerror("Error", str(e) + "\nPlease enter valid data.")

# function to display the completion screen
    def show_completion_screen():
        # create the completion screen window
        completion_window = Toplevel(export_window)
        completion_window.title("Goods added successfully")  # window title
        completion_window.geometry("400x250")  # window size
        completion_window.configure(bg="#ba9dc4")  # background color

        # center the completion screen window
        center_window(completion_window)

        # options to either return to the previous screen or add more goods
        Button(completion_window, text="Previous Screen", command=export_window.destroy, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)
        Button(completion_window, text="Add More Goods", command= lambda :[completion_window.destroy(), reset_fields()], font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)

    # button to add goods
    Button(export_window, text="Add", command=save_export, width=10, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)  # Centering the button
