import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from pages.signup import SignupWindow
from pages.modules.functions import handle_login
class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller

       
        main_container = Frame(self, bg="#ffffff")
        main_container.pack(side="top", fill="both", expand=True)
            
        img = Image.open("resources/signin_img.png")
        resized_img = img.resize((550, 400))
        img = ImageTk.PhotoImage(resized_img)

        Label(main_container, image=img, bg="#ffffff").pack(side="left", anchor="center", expand=True, fill="both")
        main_container.image = img
        
        # Login form
        loginFrame = Frame(main_container, width=470, height=470, bg="#ffffff")
        loginFrame.pack_propagate(False)
        loginFrame.pack(side="left", anchor="center", expand=True, fill="both", pady=(50,0))

        heading = Label(loginFrame, text="Sign In", font=("Krub", 25), bg="#ffffff", fg="#8d9e36")
        heading.pack(side="top", pady=(80, 30))

        self.loginEntry = Entry(loginFrame, width=30, font=("Krub", 13), fg="gray", border=0)
        self.loginEntry.pack(side="top")
        self.loginEntry.insert(0, 'E-mail/Contact No.')
        self.loginEntry.bind('<FocusIn>', self.on_entry_click)
        self.loginEntry.bind('<FocusOut>', self.on_entry_focusout)
        Frame(loginFrame, width=350, height=2, bg="#737d28").pack(side="top")

        self.loginPass = Entry(loginFrame, width=30, font=("Krub", 13), fg="gray", border=0, show='')
        self.loginPass.pack(side="top", pady=(20, 0))
        self.loginPass.insert(0, 'Password')
        self.loginPass.bind('<FocusIn>', self.on_pass_click)
        self.loginPass.bind('<FocusOut>', self.on_pass_focusout)
        Frame(loginFrame, width=350, height=2, bg="#737d28").pack(side="top")

        self.toggle_btn = Button(loginFrame, text='Show Password', font=("Krub", 10), bg="#ffffff", fg="#8d9e36", activebackground="#ffffff", activeforeground="#8d9e36", cursor='hand2', border=0, command=self.toggle_password)
        self.toggle_btn.pack(side="top", pady=(10, 0))

        signinBtn = Button(loginFrame, text="Sign In", font=("Krub", 10), width=30, bg="#8d9e36", fg="#ffffff", activebackground="#737d28", activeforeground="#ffffff", cursor='hand2', border=0, command=self.login)
        signinBtn.pack(side="top", pady=(30, 10))

        signupFrame = Frame(loginFrame, width=470, height=50, bg="#ffffff")
        signupFrame.pack(side="top")

        Label(signupFrame, text="Don't have an account? ", font=("Krub", 10), bg="#ffffff", fg="black").pack(side="left", pady=(10, 0))
        signupBtn = Button(signupFrame, text="Click here to sign up", font=("Krub", 10), bg="#ffffff", fg="#8d9e36", activebackground="#ffffff", activeforeground="#8d9e36", cursor='hand2', border=0, command=lambda: SignupWindow(self.controller))
        signupBtn.pack(side="left", pady=(10, 0))

    def on_entry_click(self, event):
        if self.loginEntry.get() == 'E-mail/Contact No.':
            self.loginEntry.delete(0, END)
            self.loginEntry.insert(0, '')
            self.loginEntry.config(fg='black')

    def on_entry_focusout(self, event):
        if self.loginEntry.get() == '':
            self.loginEntry.insert(0, 'E-mail/Contact No.')
            self.loginEntry.config(fg='grey')

    def on_pass_click(self, event):
        if self.loginPass.get() == 'Password':
            self.loginPass.delete(0, END)
            self.loginPass.config(fg='black', show='*')

    def on_pass_focusout(self, event):
        if self.loginPass.get() == '':
            self.loginPass.insert(0, 'Password')
            self.loginPass.config(fg='grey', show='')

    def toggle_password(self):
        if self.loginPass.cget('show') == '':
            if self.loginPass.get() != 'Password':
                self.loginPass.config(show='*')
            self.toggle_btn.config(text='Show Password')
        else:
            self.loginPass.config(show='')
            self.toggle_btn.config(text='Hide Password')

    def login(self):
        handle_login(self.controller, self.loginEntry, self.loginPass)
            
    def reset_entries(self):
        self.loginEntry.delete(0, tk.END)
        self.loginEntry.insert(0, 'E-mail/Contact No.')
        self.loginEntry.config(fg='grey')
        self.loginEntry.bind('<FocusIn>', self.on_entry_click)
        self.loginEntry.bind('<FocusOut>', self.on_entry_focusout)

        self.loginPass.delete(0, tk.END)
        self.loginPass.insert(0, 'Password')
        self.loginPass.config(fg='grey', show='')
        self.loginPass.bind('<FocusIn>', self.on_pass_click)
        self.loginPass.bind('<FocusOut>', self.on_pass_focusout)
            