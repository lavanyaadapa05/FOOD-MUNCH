import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

# Define the variables and functions from the provided code
categories = ["Soups", "Starters"]
items = {
    "Soups": [
        {"name": "Tomato Soup", "price": 5.99},
        {"name": "Mushroom Soup", "price": 6.99},
        {"name": "Chicken Noodle Soup", "price": 7.99},
    ],
    "Starters": [
        {"name": "Garlic Bread", "price": 4.99},
        {"name": "Chicken Wings", "price": 8.99},
        {"name": "Mozzarella Sticks", "price": 6.49},
    ],
}

selected_items = {category: {} for category in categories}
current_category_index = 0
def add_to_bill():
    current_category = categories[current_category_index]
    selected_index = listbox.curselection()
    
    if selected_index:
        index = selected_index[0]
        selected_item = items[current_category][index]
        name = selected_item["name"]
        price = selected_item["price"]
        quantity = int(quantity_var.get())

        if name in selected_items[current_category]:
            selected_items[current_category][name]["quantity"] += quantity
        else:
            selected_items[current_category][name] = {"price": price, "quantity": quantity}

        update_bill_listbox()
        update_total()

def update_bill_listbox():
    current_category = categories[current_category_index]
    bill_listbox.delete(0, tk.END)
    for name, item_data in selected_items[current_category].items():
        price = item_data["price"]
        quantity = item_data["quantity"]
        total_price = price * quantity
        bill_listbox.insert(tk.END, f"{name} x{quantity} - ₹{total_price}")

def update_total():
    total = sum(sum(item_data["price"] * item_data["quantity"] for item_data in items.values()) for items in selected_items.values())
    total_var.set(f"Total: ₹{total}")

def next_category():
    global current_category_index
    current_category_index += 1
    if current_category_index < len(categories):
        current_category = categories[current_category_index]
        listbox.delete(0, tk.END)
        for item in items[current_category]:
            listbox.insert(tk.END, item["name"])
        if current_category == "Soups":
            category_label.config(text="Choose any three soups from below:",bg = "white")
        elif current_category == "Starters":
            category_label.config(text="Choose any two starters from below:",bg="white")
        else:
            category_label.config(text=f"Category: {current_category}")
        next_button.config(state=tk.DISABLED)
        back_button.config(state=tk.NORMAL)
        update_bill_listbox()
        update_total()
    if current_category_index == len(categories) - 1:
        next_button.config(text="Finish", command=root.quit)

def previous_category():
    global current_category_index
    current_category_index -= 1
    if current_category_index >= 0:
        current_category = categories[current_category_index]
        listbox.delete(0, tk.END)
        for item in items[current_category]:
            listbox.insert(tk.END, item["name"])
        if current_category == "Soups":
            category_label.config(text="Choose any three soups from below:")
        elif current_category == "Starters":
            category_label.config(text="Choose any two starters from below:")
        else:
            category_label.config(text=f"Category: {current_category}")
        next_button.config(state=tk.NORMAL)
        back_button.config(state=tk.NORMAL)
        if current_category_index == 0:
            back_button.config(state=tk.DISABLED)
        update_bill_listbox()
        update_total()

    # Create the main window
        root = tk.Tk()
        root.title("Restaurant Menu")

        # Create a frame for the category
        category_frame = tk.Frame(root)
        category_frame.pack()

        # Create a label for the category
        category_label = tk.Label(category_frame, text="Choose any three soups from below",bg="white")
        category_label.pack()

        # Create a listbox to display items
        listbox = tk.Listbox(category_frame, selectmode=tk.SINGLE, height=5)
        listbox.pack(pady=10)

        # Create an entry for specifying the quantity
        quantity_label = tk.Label(category_frame, text="Quantity:")
        quantity_label.pack()
        quantity_var = tk.StringVar()
        quantity_entry = tk.Entry(category_frame, textvariable=quantity_var)
        quantity_entry.pack()

        # Create a button to add selected item to the bill
        add_button = tk.Button(category_frame, text="Add to Bill", command=add_to_bill)
        add_button.pack()

        # Create a listbox to display the bill
        bill_listbox = tk.Listbox(category_frame, selectmode=tk.SINGLE, height=5)
        bill_listbox.pack(pady=10)

        # Create a button to navigate to the next category
        next_button = tk.Button(category_frame, text="Next", command=next_category)
        next_button.pack(side=tk.RIGHT)

        # Create a button to navigate to the previous category
        back_button = tk.Button(category_frame, text="Back", command=previous_category, state=tk.DISABLED)
        back_button.pack(side=tk.LEFT)

        # Create a frame for the total bill
        total_frame = tk.Frame(root)
        total_frame.pack()

        # Create a label to display the total price
        total_var = tk.StringVar()
        total_var.set("Total: ₹0")
        total_label = tk.Label(total_frame, textvariable=total_var)
        total_label.pack()

        # Initial category to display
        current_category = categories[current_category_index]
        for item in items[current_category]:
            listbox.insert(tk.END, item["name"])


class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("FOOD MUNCH")
        self.root.configure(bg='#D2B48C')
        label = tk.Label(root, text="FOOD MUNCH", font=('Times New Roman', 20, 'bold'), bg="#D2B48C")
        label.pack(fill='x')
        label = tk.Label(root, text="Choose your needs!!!", bg="white")
        label.pack(fill='x')

        # Calculate the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the window's position to center it
        window_width = 500  # Set your preferred window width
        window_height = 400  # Set your preferred window height
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window's geometry
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create and configure Scan QR Code button
        self.scan_button = tk.Button(root, text="Scan QR Code", command=self.open_scan_qr_window)
        self.scan_button.pack(pady=20, padx=50, fill=tk.X)
        self.scan_button.bind("<Enter>", self.on_scan_qr_code_enter)
        self.scan_button.bind("<Leave>", self.on_scan_qr_code_leave)

        # Create and configure Hotel Management button
        self.hotel_button = tk.Button(root, text="Hotel Management", command=self.on_hotel_management_click)
        self.hotel_button.pack(pady=20, padx=50, fill=tk.X)
        self.hotel_button.bind("<Enter>", self.on_hotel_management_enter)
        self.hotel_button.bind("<Leave>", self.on_hotel_management_leave)

        # Initialize the Scan QR Code window (Toplevel)
        self.scan_qr_window = None
        self.budget_entry = None
        self.people_entry = None
        self.preferences_var = None

    def on_scan_qr_code_click(self):
        self.scan_button.config(bg='yellow')

    def on_hotel_management_click(self):
        self.hotel_button.config(bg='yellow')

    def on_scan_qr_code_enter(self, event):
        self.scan_button.config(bg='yellow')

    def on_hotel_management_enter(self, event):
        self.hotel_button.config(bg='yellow')

    def on_scan_qr_code_leave(self, event):
        self.scan_button.config(bg='SystemButtonFace')

    def on_hotel_management_leave(self, event):
        self.hotel_button.config(bg='SystemButtonFace')

    def open_scan_qr_window(self):
        self.root.withdraw()  # Hide the main window
        if self.scan_qr_window is None:
            self.scan_qr_window = tk.Toplevel(self.root)
            self.scan_qr_window.title("Options Page")
            self.scan_qr_window.configure(bg="#D2B48C")
            label = tk.Label(self.scan_qr_window, text="We work with your choices...", bg="white")
            label.pack(fill='x')
            window_width = 500
            window_height = 400
            x = 550
            y = 150
            self.scan_qr_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Create and configure Budget entry
            budget_label = tk.Label(self.scan_qr_window, text="Budget:", padx=10, pady=10)
            budget_label.pack(pady=5)
            self.budget_entry = tk.Entry(self.scan_qr_window)
            self.budget_entry.pack(pady=5)

            # Create and configure People entry
            people_label = tk.Label(self.scan_qr_window, text="Number of People:", padx=10, pady=10)
            people_label.pack(pady=5)
            self.people_entry = tk.Entry(self.scan_qr_window)
            self.people_entry.pack(pady=5)

            # Create and configure Preferences option menu
            preferences_label = tk.Label(self.scan_qr_window, text="Dietary Preferences:", padx=10, pady=10)
            preferences_label.pack(pady=5)

            self.preferences_var = tk.StringVar()
            self.preferences_var.set("Both")  # Default selection

            preferences_menu = tk.OptionMenu(self.scan_qr_window, self.preferences_var, "Veg", "Non-Veg", "Both")
            preferences_menu.pack(pady=5)

            # Create a Submit button
            submit_button = tk.Button(self.scan_qr_window, text="Submit", command=self.process_data)
            submit_button.pack(pady=10, padx=10)

            # Create a Back button
            back_button = tk.Button(self.scan_qr_window, text="Back", command=self.back_to_home)
            back_button.pack(side=tk.LEFT, pady=10, padx=10)

            # Create a Next button
            next_button = tk.Button(self.scan_qr_window, text="Next", command=self.go_to_next_step)
            next_button.pack(side=tk.RIGHT, pady=10, padx=10)

            # Create a label to display the result
            self.result_label = tk.Label(self.scan_qr_window, text="", font=("Helvetica", 12))
            self.result_label.pack(pady=10)

    def process_data(self):
        # Access data from instance variables
        budget_value = self.budget_entry.get()
        people_value = self.people_entry.get()
        preferences_value = self.preferences_var.get()
        self.result_label.config(text=f"Budget: {budget_value}, People: {people_value}, Preferences: {preferences_value}")

    def back_to_home(self):
        if self.scan_qr_window:
            self.scan_qr_window.destroy()  # Close the Scan QR Code window
        self.root.deiconify()  # Show the main Home window

    def go_to_next_step(self):
        global current_category_index
        current_category_index += 1
        if current_category_index < len(categories):
            current_category = categories[current_category_index]
            listbox.delete(0, tk.END)
            for item in items[current_category]:
                listbox.insert(tk.END, item["name"])
            if current_category == "Soups":
                category_label.config(text="Choose any three soups from below:", bg="white")
            elif current_category == "Starters":
                category_label.config(text="Choose any two starters from below:", bg="white")
            else:
                category_label.config(text=f"Category: {current_category}")
            next_button.config(state=tk.DISABLED)
            back_button.config(state=tk.NORMAL)
            update_bill_listbox()
            update_total()
        if current_category_index == len(categories) - 1:
            next_button.config(text="Finish", command=self.show_restaurant_menu)

    def show_restaurant_menu(self):
        global current_category_index
        current_category_index = 0
        self.root.deiconify()  # Show the main Home window
        if self.scan_qr_window:
            self.scan_qr_window.destroy()  # Close the Scan QR Code window

        # Create the main window for the restaurant menu
        root = tk.Toplevel(self.root)
        root.title("Restaurant Menu")
        # Data for different categories

        root.mainloop()

            # Rest of the code from the provided restaurant menu example (CategoryPage, main function, etc.

# Initialize the current_category_index
current_category_index = 0

if __name__ == "__main__":
    root = tk.Tk()
    home = Home(root)
    root.mainloop()