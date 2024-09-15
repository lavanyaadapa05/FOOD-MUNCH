import tkinter as tk
from main import *
class SecondPage:
    h1=Home.open_scan_qr_window
    categories = ["Soups", "Starters", "Biryanis", "Desserts"]
    items = {
        "Soups": [
                {"name": "Tomato Soup", "price": 500},
                {"name": "Mushroom Soup", "price": 600},
                {"name": "Chicken Noodle Soup", "price": 700},
         ],
         "Starters": [
                {"name": "Garlic Bread", "price": 400},
                {"name": "Chicken Wings", "price": 800},
                {"name": "Mozzarella Sticks", "price": 600},
        ],
            "Biryanis": [
                {"name": "Chicken Biryani", "price": 350},
                {"name": "Vegetable Biryani", "price": 250},
                {"name": "Mutton Biryani", "price": 400},
        ],
            "Desserts": [
                {"name": "Gulab Jamun", "price": 50},
                {"name": "Rasgulla", "price": 60},
                {"name": "Ice Cream", "price": 70},
        ]
            }

    selected_items = {category: {} for category in categories}
    current_category_index =0

    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Menu")
        self.root.configure(bg='#D2B48C')
        window_width = 500
        window_height = 400
        x = 550
        y = 150
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.category_frame = tk.Frame(root)
        self.category_frame.pack()


        self.category_label = tk.Label(self.category_frame, text="Choose any three soups from below",bg="white")
        self.category_label.pack()


        self.listbox = tk.Listbox(self.category_frame, selectmode=tk.SINGLE, height=5)
        self.listbox.pack(pady=10)


        self.quantity_label = tk.Label(self.category_frame, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_var = tk.IntVar()
        self.quantity_entry = tk.Entry(self.category_frame, textvariable=self.quantity_var)
        self.quantity_entry.pack()


        self.add_button = tk.Button(self.category_frame, text="Add to Bill", command=self.add_to_bill)
        self.add_button.pack()


        self.bill_listbox = tk.Listbox(self.category_frame, selectmode=tk.SINGLE, height=5)
        self.bill_listbox.pack(pady=10)


        self.next_button = tk.Button(self.category_frame, text="Next", command=self.next_category)
        self.next_button.pack(side=tk.RIGHT)

        self.back_button = tk.Button(self.category_frame, text="Back", command=self.h1, state=tk.DISABLED)
        self.back_button.pack(side=tk.LEFT)


        total_frame = tk.Frame(root)
        total_frame.pack()


        self.total_var = tk.StringVar()
        self.total_var.set("Total: ₹0")
        self.total_label = tk.Label(total_frame, textvariable=self.total_var)
        self.total_label.pack()


        current_category = self.categories[self.current_category_index]
        for item in self.items[current_category]:
            self.listbox.insert(tk.END, item["name"])
    def add_to_bill(self):
        current_category = self.categories[self.current_category_index]
        selected_index = self.listbox.curselection()
    
        if selected_index:
            index = selected_index[0]
            selected_item = self.items[current_category][index]
            name = selected_item["name"]
            price = selected_item["price"]
            quantity = int(self.quantity_var.get())
            if name in self.selected_items[current_category]:
                self.selected_items[current_category][name]["quantity"] += quantity
            else:
                self.selected_items[current_category][name] = {"price": price, "quantity": quantity}

            self.update_bill_listbox()
            self.update_total()
    def update_bill_listbox(self):
        current_category = self.categories[self.current_category_index]
        self.bill_listbox.delete(0, tk.END)
        for name, item_data in self.selected_items[current_category].items():
            price = item_data["price"]
            quantity = item_data["quantity"]
            total_price = price * quantity
            self.bill_listbox.insert(tk.END, f"{name} x{quantity} - ₹{total_price}")
    def update_total(self):
            total = sum(sum(item_data["price"] * item_data["quantity"] for item_data in items.values()) for items in self.selected_items.values())
            self.total_var.set(f"Total: ₹{total}")
    def next_category(self):
        
        self.current_category_index += 1
        if self.current_category_index < len(self.categories):
            current_category = self.categories[self.current_category_index]
            self.listbox.delete(0, tk.END)
            for item in self.items[current_category]:
                self.listbox.insert(tk.END, item["name"])
            if current_category == "Soups":
                self.category_label.config(text="Choose any three soups from below:",bg = "white")
            elif current_category == "Starters":
                self.category_label.config(text="Choose any two starters from below:",bg="white")
            else:
                self.category_label.config(text=f"Category: {current_category}")
            self.next_button.config(state=tk.DISABLED)
            self.back_button.config(state=tk.NORMAL)
            self.update_bill_listbox()
            self.update_total()
        if self.current_category_index == len(self.categories) - 1:
            self.next_button.config(text="Finish", command=self.root.quit)
    def previous_category(self):
        
        self.current_category_index -= 1
        if self.current_category_index >= 0:
            current_category = self.categories[self.current_category_index]
            self.listbox.delete(0, tk.END)
            for item in self.items[current_category]:
                self.listbox.insert(tk.END, item["name"])
            if current_category == "Soups":
                self.category_label.config(text="Choose any three soups from below:")
            elif current_category == "Starters":
                self.category_label.config(text="Choose any two starters from below:")
            else:
                self.category_label.config(text=f"Category: {current_category}")
            self.next_button.config(state=tk.NORMAL)
            self.back_button.config(state=tk.NORMAL)
            if self.current_category_index == 0:
                self.back_button.config(state=tk.DISABLED)
            self.update_bill_listbox()
            self.update_total()