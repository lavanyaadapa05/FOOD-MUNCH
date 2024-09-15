import tkinter as tk
from tkinter import messagebox

class HotelLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Login")
        self.root.geometry("300x300")

        self.label = tk.Label(root, text="Enter your details", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.staff_id_label = tk.Label(root, text="Staff ID:")
        self.staff_id_label.pack()
        self.staff_id_entry = tk.Entry(root)
        self.staff_id_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")  # Show asterisks for password
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(root, text="Back", command=self.go_back)
        self.back_button.pack()

    def login(self):
        staff_id = self.staff_id_entry.get()
        password = self.password_entry.get()

        # Replace this with your actual authentication logic
        if staff_id == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Staff ID: " + staff_id)
        else:
            messagebox.showerror("Login Failed", "Invalid Staff ID or Password")

    def go_back(self):
        # You can implement the action to go back to the previous page or close the window
        # For now, let's just close the window as an example
        self.root.destroy()

if __name__== "__main__":
    root = tk.Tk()
    app = HotelLogin(root)
    root.mainloop()