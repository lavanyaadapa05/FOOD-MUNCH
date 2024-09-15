import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
class HotelSignUp:
    def _init_(self,root):
        self.root = root
        self.root.title("Hotel Management Sign Up")
        self.root.configure(bg='#D2B48C')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 500  
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create username label and entry
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack(pady=10, padx=30)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=20, padx=30)

        # Create password label and entry
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack(pady=10, padx=30)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=20, padx=30)

        # Create confirm password label and entry
        self.confirm_password_label = tk.Label(self.root, text="Confirm Password:")
        self.confirm_password_label.pack(pady=10, padx=30)
        self.confirm_password_entry = tk.Entry(self.root, show="*")
        self.confirm_password_entry.pack(pady=20, padx=30)

        # Create sign up button
        self.sign_up_button = tk.Button(self.root, text="Sign Up", command=self.sign_up)
        self.sign_up_button.pack()
        self.button_back = tk.Button(self.root, text="Back", command=self.go_back)
        self.button_back.pack(pady=2, padx=2)

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password or username == "" or password == "" or confirm_password == "":
            messagebox.showerror("Signup status", "Passwords do not match")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", password="#Lavanya30", database="python_tkinter")
                cursor = con.cursor()  # Corrected instantiation of cursor object
                cursor.execute("INSERT INTO staff VALUES (%s, %s, %s)", (username, password, confirm_password))
                con.commit()
                self.username_entry.delete(0, 'end')  # Corrected the method call
                self.password_entry.delete(0, 'end')  # Corrected the method call
                self.confirm_password_entry.delete(0, 'end')  # Corrected the method call
                messagebox.showinfo("Signup status", "Inserted Successfully")
            except mysql.Error as err:
                messagebox.showerror("Error", f"Error occurred: {err}")
            finally:
                if 'con' in locals():
                    con.close()
    def run(self):
        self.root.mainloop()

# Instantiate the class and run the application