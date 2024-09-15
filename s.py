from tkinter import *
import sqlite3

class Home:
    def _init_(self, root):
        self.root = root
        #self.first_img = Image.open('login.png')
        #self.first_img= self.first_img.resize((500, 350))
        #self.first_img = ImageTk.PhotoImage(self.first_img)
        
        
        self.first_lbl = Label(root, image=self.first_img)
        self.first_lbl.place(x=0, y=0)
        
        self.title = Label(root, text='',font=('typewriter',20))
        self.title.place(x=45, y=0)
        
        self.bt1= Button(root, text = 'PATIENT', font = ('Garmond',12, 'bold'), command=self.customer)
        self.bt1.place(x=300, y = 150)
        
        self.bt2= Button(root, text = 'ORGANISATION', font = ('Garmond',12, 'bold'), command=self.org)
        self.bt2.place(x=300, y = 200)
        self.center_window()

    def center_window(self, event=None):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 500  
        window_height = 350
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    def create_database_tables(self):
        # Connect to the SQLite database (creates a new database if not exists)
        conn = sqlite3.connect('bloodbank.db')
        cursor = conn.cursor()

        # Table for Patient Login
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PatientLogin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_or_phone TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Table for Organization Login
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS OrganizationLogin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_or_phone TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Table for Patient Signup
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PatientSignup (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email_or_phone TEXT NOT NULL,
                password TEXT NOT NULL,
                confirm_password TEXT NOT NULL,
                otp TEXT NOT NULL
            )
        ''')

        # Table for Organization Signup
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS OrganizationSignup (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email_or_phone TEXT NOT NULL,
                password TEXT NOT NULL,
                confirm_password TEXT NOT NULL,
                otp TEXT NOT NULL
            )
        ''')

        # Table for Blood Requests
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS BloodRequests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                blood_type TEXT NOT NULL,
                zone TEXT NOT NULL,
                pound_of_blood TEXT NOT NULL,
                reason TEXT NOT NULL
            )
        ''')

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    def setup_ui(self):
        # Add the UI setup code here
        #self.first_img = Image.open('login.png')
        #self.first_img = self.first_img.resize((500, 350))
        #self.first_img = ImageTk.PhotoImage(self.first_img)

        self.first_lbl = Label(self.root, image=self.first_img)
        self.first_lbl.place(x=0, y=0)

        self.title = Label(self.root, text='', font=('typewriter', 20))
        self.title.place(x=45, y=0)

        self.bt1 = Button(self.root, text='PATIENT', font=('Garmond', 12, 'bold'), command=self.customer)
        self.bt1.place(x=300, y=150)

        self.bt2 = Button(self.root, text='ORGANISATION', font=('Garmond', 12, 'bold'), command=self.org)
        self.bt2.place(x=300, y=200)

    def customer(self):
        self.title.destroy()
        self.bt1.destroy()
        self.bt2.destroy()
        self.first_lbl.destroy()
        
        self.c_img = Image.open('login.png')
        self.c_img = self.c_img.resize((500, 350))
        #self.c_img = ImageTk.PhotoImage(self.c_img)
        
        self.c_lbl = Label(root, image=self.c_img)
        self.c_lbl.place(x=0, y=0)
        
        self.title = Label(root, text='WELCOME',font=('typewriter',13,'bold'))
        self.title.place(x=200, y=90)
        
        self.name = Label(root ,text = 'Email/Ph no:', font = ('Courier New', 15),width=12)
        self.name.place(x=50, y= 150)
        self.name.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name.entry.place(x = 220, y = 150)
        
        self.name1 = Label(root ,text = 'Password:', font = ('Courier New', 15),width=10)
        self.name1.place(x=55, y= 200)
        
        self.name1.entry = Entry(root,show ='*', font = ('Courier New', 10, 'bold'))
        self.name1.entry.place(x = 220, y = 200)
        
        self.bt1= Button(root, text = 'login', font = ('Garmond',12, 'bold'),command = self.blooddetails1)
        self.bt1.place(x=200, y = 250)
        
        self.bt4= Button(root, text = 'sign up?', font = ('Garmond',12),command=self.otp2)
        self.bt4.place(x=200, y = 290)
        
        self.bt_back = Button(root, text='Back', font=('Garmond', 12),command=lambda: self._init_(root))
        self.bt_back.place(x=50, y=290)
                
        
        

    def blooddetails1(self): 
        self.title.destroy()
        self.name.destroy()
        self.name1.destroy()
        
        self.name.entry.destroy()
        self.name1.entry.destroy()
        self.bt1.destroy()
        self.bt4.destroy()
        
        self.name10 = Label(root ,text = 'Name:', font = ('Courier New', 12),width=16)
        self.name10.place(x=50, y= 60)
        self.name10.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name10.entry.place(x = 250, y = 60)
        
        self.name11 = Label(root ,text = 'Blood type', font = ('Courier New', 12),width=16)
        self.name11.place(x=50, y= 90)
        self.name11.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name11.entry.place(x = 250, y = 90)
        
        self.name12 = Label(root ,text = 'zone', font = ('Courier New', 12),width=16)
        self.name12.place(x=50, y= 120)
        self.name12.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name12.entry.place(x = 250, y = 120)
        
        self.name13 = Label(root ,text = 'pound of blood', font = ('Courier New', 12),width=16)
        self.name13.place(x=50, y= 150)
        self.name13.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name13.entry.place(x = 250, y = 150)
        
        self.name14 = Label(root ,text = 'reason', font = ('Courier New', 12),width=10)
        self.name14.place(x=50, y= 190)
        self.name14.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name14.entry.place(x = 250, y = 190)
        
        self.bt8= Button(root, text = 'send request', font = ('Garmond',12, 'bold'))
        self.bt8.place(x=200, y = 250)
               
        self.bt_back = Button(root, text='Back', font=('Garmond', 12), command=self.customer)
        self.bt_back.place(x=50, y=290)
        
        
        
    def otp2(self):
        self.name.destroy()
        self.name1.destroy()
        self.title.destroy()
        self.name1.entry.destroy()
        self.name.entry.destroy()
        self.bt1.destroy()
        self.bt4.destroy()
        
        
        self.name6 = Label(root ,text = 'Name:', font = ('Courier New', 12),width=16)
        self.name6.place(x=50, y= 60)
        self.name6.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name6.entry.place(x = 250, y = 60)
        
        self.name7 = Label(root ,text = 'Email/Ph no:', font = ('Courier New', 12),width=16)
        self.name7.place(x=50, y= 90)
        self.name7.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name7.entry.place(x = 250, y = 90)
        
        self.name8 = Label(root ,text = 'Enter Password', font = ('Courier New', 12),width=16)
        self.name8.place(x=50, y= 120)
        self.name8.entry = Entry(root,show='*', font = ('Courier New', 10, 'bold'))
        self.name8.entry.place(x = 250, y = 120)
        
        self.name9 = Label(root ,text = ' Confirm Password:', font = ('Courier New', 12),width=16)
        self.name9.place(x=50, y= 150)
        self.name9.entry = Entry(root,show='*', font = ('Courier New', 10, 'bold'))
        self.name9.entry.place(x = 250, y = 150)
        
        self.name5 = Label(root ,text = 'Enter OTP:', font = ('Courier New', 12),width=10)
        self.name5.place(x=50, y= 190)
        self.name5.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name5.entry.place(x = 250, y = 190)
        
        self.bt4= Button(root, text = 'Submit', font = ('Garmond',12, 'bold'),command = self.blooddetails)
        self.bt4.place(x=200, y = 250)
        
        self.bt_back = Button(root, text='Back', font=('Garmond', 12), command=self.customer)
        self.bt_back.place(x=50, y=290)

    def org(self):
        self.title.destroy()
        self.bt1.destroy()
        self.bt2.destroy()
        self.first_lbl.destroy()
        
        self.o_img = Image.open('o.png')
        self.o_img = self.o_img.resize((500, 350))
        #self.o_img = ImageTk.PhotoImage(self.o_img)
        
        self.o_lbl = Label(root, image=self.o_img)
        self.o_lbl.place(x=0, y=0)
        
        self.title = Label(root, text='Welcome!!!',font=('typewriter',13,'bold'))
        self.title.place(x=200, y=20)
        
        self.name3 = Label(root ,text = 'Email/Ph no:', font = ('Courier New', 12),width=12)
        self.name3.place(x=50, y= 60)
        self.name3.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name3.entry.place(x = 200, y = 60)
        
        self.name4 = Label(root ,text = 'Password:', font = ('Courier New', 12),width=10)
        self.name4.place(x=50, y= 90)
        self.name4.entry = Entry(root,show='*',  font = ('Courier New', 10, 'bold'))
        self.name4.entry.place(x = 200, y = 90)
        
        self.bt10= Button(root, text = 'login', font = ('Garmond',12, 'bold'))
        self.bt10.place(x=200, y = 130)
        
        self.bt11= Button(root, text = 'sign up?', font = ('Garmond',12),command=self.orglogin)
        self.bt11.place(x=200, y = 170)
        
        self.bt_back = Button(root, text='Back', font=('Garmond', 12),command=lambda: self._init_(root))
        self.bt_back.place(x=50, y=290)
                


        
    def orglogin(self): 
        self.name3.destroy()
        self.name4.destroy()
        self.title.destroy()
    
        self.name3.entry.destroy()
        self.name4.entry.destroy()
        self.bt10.destroy()
        self.bt11.destroy()
        
        self.namel = Label(root ,text = 'Name:', font = ('Courier New', 12),width=16)
        self.namel.place(x=50, y= 60)
        self.namel.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.namel.entry.place(x = 250, y = 60)
        
        self.namea = Label(root ,text = 'Email/Ph no:', font = ('Courier New', 12),width=16)
        self.namea.place(x=50, y= 90)
        self.namea.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.namea.entry.place(x = 250, y = 90)
        
        self.nameb = Label(root ,text = 'Enter Password', font = ('Courier New', 12),width=16)
        self.nameb.place(x=50, y= 120)
        self.nameb.entry = Entry(root,show='*',  font = ('Courier New', 10, 'bold'))
        self.nameb.entry.place(x = 250, y = 120)
        
        self.namec = Label(root ,text = ' Confirm Password:', font = ('Courier New', 12),width=16)
        self.namec.place(x=50, y= 150)
        self.namec.entry = Entry(root,show='*',  font = ('Courier New', 10, 'bold'))
        self.namec.entry.place(x = 250, y = 150)
        
        self.named = Label(root ,text = 'Enter OTP:', font = ('Courier New', 12),width=10)
        self.named.place(x=50, y= 190)
        self.named.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.named.entry.place(x = 250, y = 190)
        
        self.bt9= Button(root, text = 'Submit', font = ('Garmond',12, 'bold'))
        self.bt9.place(x=200, y = 250)
        
        self.bt_back = Button(root, text='Back', font=('Garmond', 12), command=self.org)
        self.bt_back.place(x=50, y=290)     
                   
            
    def blooddetails(self): 
        self.name6.destroy()
        self.name7.destroy()
        self.name5.destroy()
        self.name8.destroy()
        self.name9.destroy()
    
        self.name5.entry.destroy()
        self.name6.entry.destroy()
        self.name7.entry.destroy()
        self.name8.entry.destroy()
        self.name9.entry.destroy()
        self.bt4.destroy()
        
        self.name6 = Label(root ,text = 'Name:', font = ('Courier New', 12),width=16)
        self.name6.place(x=50, y= 60)
        self.name6.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name6.entry.place(x = 250, y = 60)
        
        self.name7 = Label(root ,text = 'Blood type', font = ('Courier New', 12),width=16)
        self.name7.place(x=50, y= 90)
        self.name7.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name7.entry.place(x = 250, y = 90)
        
        self.name8 = Label(root ,text = 'zone', font = ('Courier New', 12),width=16)
        self.name8.place(x=50, y= 120)
        self.name8.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name8.entry.place(x = 250, y = 120)
        
        self.name9 = Label(root ,text = 'pound of blood', font = ('Courier New', 12),width=16)
        self.name9.place(x=50, y= 150)
        self.name9.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name9.entry.place(x = 250, y = 150)
        
        self.name5 = Label(root ,text = 'reason', font = ('Courier New', 12),width=10)
        self.name5.place(x=50, y= 190)
        self.name5.entry = Entry(root, font = ('Courier New', 10, 'bold'))
        self.name5.entry.place(x = 250, y = 190)
        
        self.bt4= Button(root, text = 'send request', font = ('Garmond',12, 'bold'))
        self.bt4.place(x=200, y = 250)
        
        self.bt_back = Button(root, text='Back', font=('Garmond', 12), command=self.otp2)
        self.bt_back.place(x=50, y=290)
        
        
      
    def _init_(self, root):
        self.root = root
        self.first_img = Image.open('login.png')
        self.first_img= self.first_img.resize((500, 350))
        #self.first_img = ImageTk.PhotoImage(self.first_img)
        
        self.first_lbl = Label(root, image=self.first_img)
        self.first_lbl.place(x=0, y=0)
        
        self.title = Label(root, text='',font=('typewriter',20))
        self.title.place(x=45, y=0)
        
        self.bt1= Button(root, text = 'PATIENT', font = ('Garmond',12, 'bold'), command=self.customer)
        self.bt1.place(x=300, y = 150)
        
        self.bt2= Button(root, text = 'ORGANISATION', font = ('Garmond',12, 'bold'), command=self.org)
        self.bt2.place(x=300, y = 200)

root = Tk()
root.geometry('500x350+550+200')
root.title('BLOODBANK')

home = Home(root)
root.bind('<Configure>', home.center_window)
root.mainloop()