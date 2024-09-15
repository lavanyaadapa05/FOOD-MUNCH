import tkinter as tk
from itertools import product
from main import Home
class Page2:
    def _init_(self,root):
        h1=Home.open_scan_qr_window
        self.root = root
        self.root.title("Choose your combo")
        self.root.configure(bg='#D2B48C')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 500  
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label_budget = tk.Label(self.root, text="Enter Total Budget:")
        self.label_budget.pack(pady=10, padx=30)
        self.entry_budget = tk.Entry(self.root)
        self.entry_budget.pack(pady=10, padx=30)

        self.label_people = tk.Label(self.root, text="Enter Number of People:")
        self.label_people.pack(pady=10, padx=30)
        self.entry_people = tk.Entry(self.root)
        self.entry_people.pack(pady=10, padx=30)

        self.preference_var = tk.StringVar(value="both")
        self.label_preference = tk.Label(self.root, text="Select Preference:")
        self.label_preference.pack(pady=10, padx=30)

        self.veg_radio = tk.Radiobutton(self.root, text="Veg", variable=self.preference_var, value="veg")
        self.veg_radio.pack(pady=10, padx=30)
        self.nonveg_radio = tk.Radiobutton(self.root, text="Non-Veg", variable=self.preference_var, value="nonveg")
        self.nonveg_radio.pack(pady=10, padx=30)
        self.both_radio = tk.Radiobutton(self.root, text="Both", variable=self.preference_var, value="both")
        self.both_radio.pack(pady=10, padx=30)

        self.button = tk.Button(self.root, text="Split Budget", command=self.on_button_click)
        self.button.pack(pady=10, padx=30)
        self.button_back = tk.Button(self.root, text="Back", command=self.go_back)
        self.button_back.pack(pady=2, padx=2)
        

        self.root.mainloop()

    def show_combinations(self, total_budget, num_people, preference):
        veg_dishes = {
            "Soup": {"Tomato": 100, "Lentil": 300, "Spinach": 110},
            "Starter": {"Paneer": 212, "Cauliflower": 213, "Potato": 214},
            "Biryani": {"Vegetable": 215, "Mushroom": 216, "Peas": 217}
        }
        nonveg_dishes = {
            "Soup": {"Chicken": 100, "Mutton": 113, "Seafood": 123},
            "Starter": {"Chicken": 150, "Fish": 168, "Mutton": 170},
            "Biryani": {"Chicken": 200, "Mutton": 210, "Seafood": 220}
        }

        selected_dishes = veg_dishes if preference == "veg" else nonveg_dishes
        budget_per_person = total_budget / num_people

        all_combinations = product(selected_dishes["Soup"].items(), selected_dishes["Starter"].items(), selected_dishes["Biryani"].items())

        valid_combinations = [
            combination for combination in all_combinations if sum(price for _, price in combination) * num_people <= total_budget
        ]

        # Limit to 5 combinations
        valid_combinations = valid_combinations[:5]

        self.combinations_window = tk.Toplevel(self.root)
        self.combinations_window.title("Available Combinations")

        background_color = self.root.cget("bg")
        root_geometry = self.root.geometry()

        self.combinations_window.configure(bg=background_color)
        self.combinations_window.geometry(root_geometry)

        self.var = tk.StringVar(value="")  # Set the initial value to an empty string

        for idx, combination in enumerate(valid_combinations):
            items_info = ", ".join(f"{name} ({price})" for name, price in combination)
            tk.Radiobutton(self.combinations_window, text=f"Combination {idx + 1}: {items_info}", variable=self.var, value=f"{combination}").pack(padx=10,pady=10)

        tk.Button(self.combinations_window, text="Select", command=lambda: self.on_combination_select(self.var.get(), total_budget, num_people)).pack()

    def on_combination_select(self, selected_combination, total_budget, num_people):
        selected_combination = eval(selected_combination)
        items_info = ", ".join(f"{name} ({price})" for name, price in selected_combination)

        # Append the selected items to the list
        self.selected_items.append(items_info)

        bill_window = tk.Toplevel(self.root)
        bill_window.title("Bill Details")

        background_color = self.root.cget("bg")
        root_geometry = self.root.geometry()

        bill_window.configure(bg=background_color)
        bill_window.geometry(root_geometry)

        tk.Label(bill_window, text=f"Selected Combination: {items_info}").pack(padx=10, pady=10)

        total_price = sum(price for _, price in selected_combination) * num_people
        tk.Label(bill_window, text=f"Total Bill: {total_price}").pack()

        confirm_button = tk.Button(bill_window, text="Confirm Order", command=lambda: self.confirm_order(bill_window))
        confirm_button.pack(pady=10)

    def back_to_home(self, confirmation_window):
        
        confirmation_window.destroy()  
        self.root.deiconify() 
        self.main_page_instance.root.deiconify()  

    def confirm_order(self, bill_window):
        bill_window.destroy() 
        confirmation_window = tk.Toplevel(self.root)
        confirmation_window.title("Confirmation")

        background_color = self.root.cget("bg")
        root_geometry = self.root.geometry()

        confirmation_window.configure(bg=background_color)
        confirmation_window.geometry(root_geometry)

        tk.Label(confirmation_window, text="Your order is confirmed", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(confirmation_window, text=u"\u2713", font=("Arial", 24)).pack()  

        back_to_home_button = tk.Button(confirmation_window, text="Back to Home", command=lambda: self.back_to_home(confirmation_window))
        back_to_home_button.pack(pady=10)

    def on_button_click(self):
        total_budget = float(self.entry_budget.get())
        num_people = int(self.entry_people.get())
        preference = self.preference_var.get()
        self.show_combinations(total_budget, num_people, preference)
    def go_back(self):
        self.root.withdraw() 
        root = tk.Tk()
        app = Home(root)
        root.mainloop()