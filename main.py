import tkinter as tk
from tkinter import messagebox 
from second1 import *
from hotellogin import *
class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("FOOD MUNCH")
        self.root.configure(bg='#D2B48C')
        label = tk.Label(root, text="FOOD MUNCH", font=('Times New Roman', 20, 'bold'), bg="#D2B48C")
        label.pack(fill='x')
        label = tk.Label(root, text="Choose your needs!!!", bg="white")
        label.pack(fill='x')

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = 500  
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.scan_button = tk.Button(root, text="Scan QR Code", command=self.open_scan_qr_window)
        self.scan_button.pack(pady=20, padx=50, fill=tk.X)
        self.scan_button.bind("<Enter>", self.on_scan_qr_code_enter)
        self.scan_button.bind("<Leave>", self.on_scan_qr_code_leave)


        self.hotel_button = tk.Button(root, text="Hotel Management", command=self.open_hotel_management)
        self.hotel_button.pack(pady=20, padx=50, fill=tk.X)
        self.hotel_button.bind("<Enter>", self.on_hotel_management_enter)
        self.hotel_button.bind("<Leave>", self.on_hotel_management_leave)


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
    def open_hotel_management(self):
        self.root.withdraw() 
        root = tk.Tk()
        app = HotelLogin(root)
        root.mainloop()
        



    def open_scan_qr_window(self):
        self.root.withdraw()  
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

            budget_label = tk.Label(self.scan_qr_window, text="Budget:", padx=10, pady=10)
            budget_label.pack(pady=5)
            self.budget_entry = tk.Entry(self.scan_qr_window)
            self.budget_entry.pack(pady=5)


            people_label = tk.Label(self.scan_qr_window, text="Number of People:", padx=10, pady=10)
            people_label.pack(pady=5)
            self.people_entry = tk.Entry(self.scan_qr_window)
            self.people_entry.pack(pady=5)

        
            preferences_label = tk.Label(self.scan_qr_window, text="Dietary Preferences:", padx=10, pady=10)
            preferences_label.pack(pady=5)

            self.preferences_var = tk.StringVar()
            self.preferences_var.set("Both")  

            preferences_menu = tk.OptionMenu(self.scan_qr_window, self.preferences_var, "Veg", "Non-Veg", "Both")
            preferences_menu.pack(pady=5)

        
            submit_button = tk.Button(self.scan_qr_window, text="Submit", command=self.process_data)
            submit_button.pack(pady=10, padx=10)

        
            back_button = tk.Button(self.scan_qr_window, text="Back", command=self.back_to_home)
            back_button.pack(side=tk.LEFT, pady=10, padx=10)

            
            next_button = tk.Button(self.scan_qr_window, text="Next", command=self.go_to_next_step)
            next_button.pack(side=tk.RIGHT, pady=10, padx=10)

            
            self.result_label = tk.Label(self.scan_qr_window, text="", font=("Helvetica", 12))
            self.result_label.pack(pady=10)

    def process_data(self):
        budget_value = self.budget_entry.get()
        people_value = self.people_entry.get()
        preferences_value = self.preferences_var.get()
        self.result_label.config(text=f"Budget: {budget_value}, People: {people_value}, Preferences: {preferences_value}")

    def back_to_home(self):
        if self.scan_qr_window:
            self.scan_qr_window.destroy()  
        self.root.deiconify()  

    def go_to_next_step(self):
        self.root.withdraw() 
        root = tk.Tk()
        app = SecondPage(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    home = Home(root)
    root.mainloop()