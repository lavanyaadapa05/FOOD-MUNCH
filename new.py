import tkinter as tk
from tkinter import messagebox
from new import Page2
from tkinter import messagebox
# Assuming you have a file named page2.py with the Page2 class

class DisplaySelectedItemsWindow:
    def __init__(self, root, selected_items):
        self.root = root
        self.root.title("Selected Items")
        self.selected_items = selected_items

        self.label = tk.Label(root, text="Selected Items:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        for item in selected_items:
            tk.Label(root, text=item).pack(pady=5)

# Example usage in HotelLogin class:
# In the login method, after calling open_page2_window, you can get selected items and open the new window.
# Add the following lines in the login method:

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
            # If login is successful, open the Page2 window
            page2_window = tk.Toplevel(self.root)
            page2 = Page2(page2_window)

            # Get selected items from Page2
            selected_items = page2.get_selected_items()

            # Open a new window to display selected items
            display_items_window = tk.Toplevel(self.root)
            display_items = DisplaySelectedItemsWindow(display_items_window, selected_items)
        else:
            messagebox.showinfo("", "Incorrect username or password")
    except mysql.Error as err:
        messagebox.showerror("Error", f"Error occurred: {err}")
    finally:
        if 'con' in locals():
            con.close()
