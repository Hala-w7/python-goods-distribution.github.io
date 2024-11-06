from tkinter import *
from tkinter import messagebox

from import_goods import imported_goods, import_goods_screen
from branches_management import branches
from export_goods import exported_goods

show_good_details = ""

# function to center the window on the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# function to create a new screen for distribution options
def distribution_screen(root):
    distribution_window = Toplevel(root)
    distribution_window.title("Distribution Options")
    distribution_window.geometry("400x300")
    distribution_window.configure(bg="#ba9dc4")
    center_window(distribution_window)

    button_frame = Frame(distribution_window, bg="#ba9dc4")
    button_frame.pack(expand=True, pady=20)

    Button(button_frame, text="Show Available Goods", command=show_available_goods, font=("Arial", 12, "bold"), bg="#9c81a6", fg="white", width=25).pack(pady=10)
    Button(button_frame, text="Distribution Locations", command=show_distribution_locations, font=("Arial", 12, "bold"), bg="#9c81a6", fg="white", width=25).pack(pady=10)
    
    # Add a Previous button
    Button(button_frame, text="Previous", command=distribution_window.destroy, font=("Arial", 12, "bold"), bg="#9c81a6", fg="white", width=25).pack(pady=10)

# function to show available goods with choice between imported and exported
def show_available_goods():

    # Check if there are any goods available
    if not imported_goods and not exported_goods:
        messagebox.showinfo("Information", "No goods available. Please add goods first.")
        return
    
    choice_window = Toplevel()
    choice_window.title("Choose Goods Type")
    choice_window.geometry("300x150")
    choice_window.configure(bg="#ba9dc4")
    center_window(choice_window)

    Label(choice_window, text="Do you want to view:", bg="#ba9dc4", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    
    Button(choice_window, text="Imported Goods", command=lambda: display_goods("imported"), bg="#9c81a6", fg="white", width=20).pack(pady=5)
    Button(choice_window, text="Exported Goods", command=lambda: display_goods("exported"), bg="#9c81a6", fg="white", width=20).pack(pady=5)

# function to display goods based on choice (imported or exported) with detailed fields
def display_goods(goods_type):
    goods_window = Toplevel()
    goods_window.title(f"{goods_type.capitalize()} Goods")
    goods_window.geometry("400x400")
    goods_window.configure(bg="#ba9dc4")
    center_window(goods_window)

    goods_list = imported_goods if goods_type == "imported" else exported_goods

    # Check if goods list is empty and show a message box
    if not goods_list:
        messagebox.showinfo("No Goods Available", "There are no goods available in this category.")
        goods_window.destroy()  # Close the window if no goods are available
        return

    # Create a frame to hold the goods
    goods_frame = Frame(goods_window, bg="#ba9dc4")
    goods_frame.pack(pady=20)
    # Create a frame to hold the details
    details_frame = Frame(goods_window, bg="#ba9dc4")
    details_frame.pack(pady=10)

    for good in goods_list:
        # Create a button for each good
        button = Button(goods_frame, text=f"{good['name']}", command=lambda g = good: show_good_details(g, details_frame), bg="#9c81a6", fg="white", width=20)
        button.pack(pady=5)

# Function to show good details under the selected button
def show_good_details(good, details_frame):
    # Clear previous details
    for widget in details_frame.winfo_children():
        widget.destroy()

    # Displaying the details of the selected good
    Label(details_frame, text=f"Goods Name: {good['name']}", bg="#ba9dc4", fg="white", font=("Arial", 10, "bold")).pack(pady=(5, 2))
    Label(details_frame, text=f"Quantity: {good['quantity']}", bg="#ba9dc4", fg="white", font=("Arial", 10)).pack(pady=(0, 2))
    Label(details_frame, text=f"Cost: {good['cost']}", bg="#ba9dc4", fg="white", font=("Arial", 10)).pack(pady=(0, 2))
    
    if 'arrival_date' in good:  # For imported goods
        Label(details_frame, text=f"Arrival Date: {good['arrival_date']}", bg="#ba9dc4", fg="white", font=("Arial", 10)).pack(pady=(0, 2))
    if 'export_date' in good:  # For exported goods
        Label(details_frame, text=f"Export Date: {good['export_date']}", bg="#ba9dc4", fg="white", font=("Arial", 10)).pack(pady=(0, 2))

    separator = Frame(details_frame, height=2, bd=1, relief=SUNKEN, bg="#9c81a6")
    separator.pack(fill="x", padx=5, pady=5)  # Add a separator after details

# function to show distribution locations
def show_distribution_locations():

    # check if branches list is empty
    if not branches:
        messagebox.showinfo("No Branches", "No branches have been added yet.")
        return  # exit the function if no branches are available

    locations_window = Toplevel()
    locations_window.title("Distribution Locations")
    locations_window.geometry("400x300")
    locations_window.configure(bg="#ba9dc4")
    center_window(locations_window)

    Label(locations_window, text="Select The Branch:", bg="#ba9dc4", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    
    branch_frame = Frame(locations_window, bg="#ba9dc4")
    branch_frame.pack(pady=20)
    
    for branch in branches:
        button = Button(branch_frame, text=branch['name'], command=lambda : request_delivery_info(branch), bg="#9c81a6", fg="white", width=25, font=("Arial", 10, "bold"))
        button.pack(pady=5)

# function to request delivery information
def request_delivery_info(branch):

    # check if branches list is empty
    if not imported_goods:
        messagebox.showinfo("No Goods", "No imported goods have been added yet.")
        return  # exit the function if no imported goods are available

    delivery_info_window = Toplevel()
    delivery_info_window.title("Delivery Date and Quantity")
    delivery_info_window.geometry("400x200")
    delivery_info_window.configure(bg="#ba9dc4")
    center_window(delivery_info_window)

    Label(delivery_info_window, text="Select Imported Good:", bg="#ba9dc4", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

    # Frame to display imported goods
    goods_frame = Frame(delivery_info_window, bg="#ba9dc4")
    goods_frame.pack(pady=5)

    # Create buttons for each imported good
    for good in imported_goods: 
        Button(goods_frame, text=f"{good['name']}", command=lambda : enter_delivery_details(good, delivery_info_window), bg="#9c81a6", fg="white", width=20, font=("Arial", 10, "bold")).pack(pady=5)

# Function to enter delivery details after selecting a good
def enter_delivery_details(good, parent_window):
    # Close the parent window for a clean interface
    parent_window.destroy()
    
    delivery_detail_window = Toplevel()
    delivery_detail_window.title("Delivery Date and Quantity")
    delivery_detail_window.geometry("400x200")
    delivery_detail_window.configure(bg="#ba9dc4")
    center_window(delivery_detail_window)

    Label(delivery_detail_window, text="Enter Delivery Date:", bg="#ba9dc4", fg="white", font=("Arial", 11, "bold")).pack(pady=10)
    date_entry = Entry(delivery_detail_window, font=("Arial", 10, "bold"))
    date_entry.pack(pady=5)

    Label(delivery_detail_window, text="Enter Quantity:", bg="#ba9dc4", fg="white", font=("Arial", 11, "bold")).pack(pady=10)
    quantity_entry = Entry(delivery_detail_window, font=("Arial", 10, "bold"))
    quantity_entry.pack(pady=5)

    date = date_entry.get()
    quantity = quantity_entry.get()
    Button(delivery_detail_window, text="Calculate Expected Profit", command=lambda: calculate_expected_profit(good, date, quantity), bg="#9c81a6", fg="white").pack(pady=10)

# function to calculate expected profit and show options
def calculate_expected_profit(good, delivery_date, quantity):
     
    try:     
        quantity = int(quantity)
        if quantity < 0:  # check if quantity is negative
                raise ValueError("Quantity cannot be negative.")  # raise exception if negative
            
        global selected_good_name 
        selected_good_name = good['name']
        
        for good in imported_goods:
            if good['name'] == selected_good_name:
                if quantity > good['quantity']:
                    messagebox.showerror("Error", "Not enough goods available for distribution.")
                    return
                
                good['quantity'] -= quantity
                profit_margin = 10
                expected_profit = quantity * profit_margin
                messagebox.showinfo("Expected Profit", f"Expected profit: {expected_profit}.\nRemaining Quantity: {good['quantity']}")
                
                show_options()
                return  # Exit the function after processing
            
         # If the function reaches here, the good was not found
        messagebox.showerror("Error", "Selected good not found in the imported goods.")
                
    except ValueError as e:
        messagebox.showerror("Error", str(e) + "Please enter a valid quantity.")

# function to show options after completing the operation
def show_options():
    options_window = Toplevel()
    options_window.title("Choose Next Action")
    options_window.geometry("300x200")
    options_window.configure(bg="#ba9dc4")
    center_window(options_window)
    
    Label(options_window, text="Choose your next action:", font=("Arial", 12), bg="#ba9dc4").pack(pady=10)

    Button(options_window, text="Return to Previous Screen", command = options_window.destroy, bg="#9c81a6", fg="white", width=25).pack(pady=5)
    Button(options_window, text="Add Another Good", command=add_another_good, bg="#9c81a6", fg="white", width=25).pack(pady=5)
    Button(options_window, text="Return to Main Screen", command =lambda: distribution_screen.destroy(), bg="#9c81a6", fg="white", width=25).pack(pady=5)

# function to simulate adding another good (implement logic as needed)
def add_another_good():
    import_goods_screen()