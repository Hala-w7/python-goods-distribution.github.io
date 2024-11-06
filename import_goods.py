# import Tkinter library and messagebox for displaying messages
from tkinter import *
from tkinter import messagebox

# list to store imported goods
imported_goods = []

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


# function to set up and display the imported goods screen
def import_goods_screen(root):
    # create the imported goods window
    import_window = Toplevel(root)
    import_window.title("Imported Goods")  # window title
    import_window.geometry("600x450")  # window size
    import_window.configure(bg="#ba9dc4")  # background color

    # center the main menu window
    center_window(import_window)

    # goods name entry field
    Label(import_window, text="Goods Name:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(20, 5)) # Padding for top and bottom
    name_entry = Entry(import_window, font=("Arial", 10, "bold"))
    name_entry.pack(pady=(0, 10))  # Padding for top and bottom

    # quantity entry field
    Label(import_window, text="Quantity:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5)) # Padding for top and bottom
    quantity_entry = Entry(import_window, font=("Arial", 10, "bold"))
    quantity_entry.pack(pady=(0, 20))  # Padding for top and bottom

    # arrival date entry field
    Label(import_window, text="Arrival Date:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5)) # Padding for top and bottom
    arrival_date_entry = Entry(import_window, font=("Arial", 10, "bold"))
    arrival_date_entry.pack(pady=(0, 10))

    # cost entry field
    Label(import_window, text="Cost:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5)) # Padding for top and bottom
    cost_entry = Entry(import_window, font=("Arial", 10, "bold"))
    cost_entry.pack(pady=(0, 10))

    # import location entry field
    Label(import_window, text="Import Location:", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 5)) # Padding for top and bottom
    location_entry = Entry(import_window, font=("Arial", 10, "bold"))
    location_entry.pack(pady=(0, 20))

    # function to reset the fields after adding goods
    def reset_fields():
        name_entry.delete(0, 'end')
        quantity_entry.delete(0, 'end')
        arrival_date_entry.delete(0, 'end')
        cost_entry.delete(0, 'end')
        location_entry.delete(0, 'end')

    # function to save entered goods data
    def save_import():
        # create a dictionary to store data and add it to the list
        try:
            quantity = int(quantity_entry.get())
            if quantity < 0:  # check if quantity is negative
                raise ValueError("Quantity cannot be negative.")  # raise exception if negative
            
            cost = float(cost_entry.get())  
            if cost < 0:
                raise ValueError("Cost cannot be negative.")  # check if cost is negative

            # create a dictionary to store data and add it to the list
            good = {
                "name": name_entry.get(),
                "quantity": quantity,
                "arrival_date": arrival_date_entry.get(),
                "cost": cost,
                "location": location_entry.get()
            }
            imported_goods.append(good)

            # confirmation message after adding the goods
            messagebox.showinfo("Success", "Goods added successfully")
            show_completion_screen()

        except ValueError as e:
            # show error message if input is invalid
            messagebox.showerror("Error", str(e) + "\nPlease enter valid data.")

    # function to display the completion screen
    def show_completion_screen():
        # create the completion screen window
        completion_window = Toplevel(import_window)
        completion_window.title("Goods added successfully")  # window title
        completion_window.geometry("400x250")  # window size
        completion_window.configure(bg="#ba9dc4")  # background color

        # center the completion screen window
        center_window(completion_window)

        # options to either return to the previous screen or add more goods
        Button(completion_window, text="Previous Screen", command=import_window.destroy, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)
        Button(completion_window, text="Add More Goods", command= lambda: [completion_window.destroy(), reset_fields()], font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)
               
    # button to add goods
    Button(import_window, text="Add", command=save_import, width=10, font=("Arial", 10, "bold"), bg="#9c81a6", fg="white").pack(pady=20)  # Centering the button