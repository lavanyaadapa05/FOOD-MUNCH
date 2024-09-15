import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
from signup import *
from main import Home
class HotelLogin:
    def _init_(self, root):
        self.root = root
        self.root.title("Hotel Management Login")
        self.root.configure(bg='#D2B48C')
        window_width = 500
        window_height = 400
        x = 550
        y = 150
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label = tk.Label(root, text="Enter your details", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.staff_id_label = tk.Label(root, text="UserName:")
        self.staff_id_label.pack(pady=10, padx=30)
        self.staff_id_entry = tk.Entry(root)
        self.staff_id_entry.pack(pady=10, padx=30)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=10, padx=30)
        self.password_entry = tk.Entry(root, show="*")  
        self.password_entry.pack(pady=10, padx=30)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.signup_button = tk.Button(root, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=5)
        self.button_back = tk.Button(self.root, text="Back", command=self.go_back)
        self.button_back.pack(pady=2, padx=2)

    def login(self):
        staff_id = self.staff_id_entry.get()
        password = self.password_entry.get()
        
        sql = "SELECT * FROM staff WHERE name = %s AND password = %s"
        try:
            con = mysql.connect(host="localhost", user="root", password="#Lavanya30", database="python_tkinter")
            cursor = con.cursor()
            cursor.execute(sql, (staff_id, password))
            results = cursor.fetchall()
            if results:
                messagebox.showinfo("", "Login Success")
                self.staff_id_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                return True
            else:
                messagebox.showinfo("", "Incorrect username or password")
                return False
        except mysql.Error as err:
            messagebox.showerror("Error", f"Error occurred: {err}")
        finally:
            if 'con' in locals():
                con.close()

    def signup(self):
        self.root.withdraw() 
        signup_window = tk.Toplevel(self.root)
        signup = HotelSignUp(signup_window)
    def go_back(self):
        self.root.withdraw() 
        root = tk.Tk()
        app = Home(root)
        root.mainloop()