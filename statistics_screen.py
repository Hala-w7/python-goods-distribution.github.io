# Import required libraries for Tkinter and Matplotlib
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# Import other screens
from import_goods import imported_goods
from export_goods import exported_goods

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

# Function to set up and display the statistics screen
def statistics_screen(root):
    # Create the statistics window
    statistics_window = Toplevel(root)
    statistics_window.title("Goods Statistics")
    statistics_window.geometry("600x400")
    statistics_window.configure(bg="#d4c7d9")

    # Center the statistics window on the screen
    center_window(statistics_window)

    # Check if there are any imported or exported goods to display
    if not imported_goods and not exported_goods:
        messagebox.showinfo("Information", "No imported or exported goods to display.")
        statistics_window.destroy()
        return  # Exit the function if the lists are empty

    # Buttons for showing import statistics and export statistics
    Button(statistics_window, text="Show Import Statistics", command=display_import_statistics, font=("Arial", 10, "bold"), bg="#977aa1", fg="white").pack(pady=(20, 10))
    Button(statistics_window, text="Show Export Statistics", command=display_export_statistics, font=("Arial", 10, "bold"), bg="#977aa1", fg="white").pack(pady=10)
    Button(statistics_window, text="Show All Statistics", command=show_all_statistics, font=("Arial", 10, "bold"), bg="#977aa1", fg="white").pack(pady=10)
    
    # Add a Previous button
    Button(statistics_window, text="Previous", command=statistics_window.destroy, font=("Arial", 10, "bold"), bg="#977aa1", fg="white").pack(pady=(10))

# Function to display all statistics (import and export)
def show_all_statistics():
    display_import_statistics()
    display_export_statistics()

# Function to display a bar chart of the imported goods statistics
def display_import_statistics():
    if not imported_goods:
        messagebox.showinfo("Information", "No imported goods to display.")
        return

    # Prepare data for import statistics chart
    goods_names = [good["name"] for good in imported_goods]  # Extract goods names
    quantities = [good["quantity"] for good in imported_goods]  # Extract quantities
    arrival_dates = [good["arrival_date"] for good in imported_goods]  # Extract arrival dates

    # Create a bar chart for imported goods
    plt.figure(figsize=(10, 5))
    plt.bar(goods_names, quantities, width=0.5, color="#818aa6")
    plt.xlabel("Goods Name")
    plt.ylabel("Quantity")
    plt.title("Imported Goods Statistics")
    plt.xticks(rotation=45)

    # Display arrival dates as annotations
    for i, (quantity, arrival_date) in enumerate(zip(quantities, arrival_dates)):
        plt.annotate(f"{arrival_date}", xy=(i, quantity), ha='center', va='bottom', fontsize=8, color='blue')
    
    # Draw import quantities based on the date
    date_quantity = {}
    for good in imported_goods:
        date_str = good['arrival_date']  # Use date as a string directly
        if date_str in date_quantity:
            date_quantity[date_str] += good['quantity']
        else:
            date_quantity[date_str] = good['quantity']

    dates = list(date_quantity.keys())
    quantities_by_date = list(date_quantity.values())

    plt.figure(figsize=(10, 5))
    plt.bar(dates, quantities_by_date, color="#ba9dc4", width=0.4)
    plt.xlabel("Arrival Dates")
    plt.ylabel("Total Quantity Imported")
    plt.title("Imported Goods Quantity by Date")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

# Function to display a bar chart of the exported goods statistics
def display_export_statistics():
    if not exported_goods:
        messagebox.showinfo("Information", "No exported goods to display.")
        return

    # Prepare data for export statistics chart
    export_goods_names = [good["name"] for good in exported_goods]
    export_quantities = [good["quantity"] for good in exported_goods]

    # Get imported quantities for each item from the main warehouse
    imported_goods_dict = {good["name"]: good["quantity"] for good in imported_goods}

    # Calculate base quantities and the differences
    base_quantities = [imported_goods_dict.get(name, 0) for name in export_goods_names]
    quantity_differences = [base - exported for base, exported in zip(base_quantities, export_quantities)]

    # Create a bar chart for exported goods
    plt.figure(figsize=(10, 5))
    bar_width = 0.35
    index = range(len(export_goods_names))

    # Plot bars for export quantities and base quantities
    plt.bar(index, export_quantities, width=bar_width, color="orange", label="Exported Quantity")
    plt.bar(index, base_quantities, width=bar_width, color="#818aa6", alpha=0.5, label="Base Quantity")

    plt.xlabel("Goods Name")
    plt.ylabel("Quantity")
    plt.title("Exported Goods Statistics")
    plt.xticks(index, export_goods_names, rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()
