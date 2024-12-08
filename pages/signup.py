import tkinter as tk
from tkinter import Toplevel, Frame, Label, Entry, Button
from PIL import Image, ImageTk

class SignupWindow:
    def __init__(self, root):
        self.root = root
        self.signup_window = Toplevel(root)
        self.signup_window.title("Sign Up")
        self.signup_window.geometry("1080x600")
        self.signup_window.configure(bg="#ffffff")
        self.signup_window.resizable(False, False)

        # Open and resize the image
        img = Image.open("resources/signin_img.png")
        resized_img = img.resize((550, 400))
        self.img = ImageTk.PhotoImage(resized_img)

        # Create a label to display the image
        Label(self.signup_window, image=self.img, bg="#ffffff").pack(side="left", padx=(20,0))

        # Create a frame for the signup form
        signupFrame = Frame(self.signup_window, width=470, height=470, bg="#ffffff")
        signupFrame.pack_propagate(False)
        signupFrame.pack(side="right", padx=(0,20), pady=(20,20))

        # Add a heading to the signup frame
        heading = Label(signupFrame, text="Sign Up", font=("Krub", 25),bg="#ffffff", fg="#8d9e36")
        heading.pack(side="top", pady=(20, 10))
        
        # NAME SECTION
        nameFrame = Frame(signupFrame, width=470, bg="#ffffff")
        nameFrame.pack(side="top", pady=(20, 0))

        # Sub-frame for the first name entry and its underline
        fnameFrame = Frame(nameFrame, bg="#ffffff")
        fnameFrame.pack(side="left")

        # First name entry
        self.fnameEntry = Entry(fnameFrame, font=("Krub", 13), width=15, border=0, fg="gray")
        self.fnameEntry.pack(side="top", padx=(0, 2))
        self.fnameEntry.insert(0, 'Firstname')
        self.fnameEntry.bind('<FocusIn>', self.on_fname_click)
        self.fnameEntry.bind('<FocusOut>', self.on_fname_focusout)

        # Add underline for first name entry
        Frame(fnameFrame, width=184, height=2, bg="#737d28").pack(side="top", padx=(0,2))

        # Sub-frame for the last name entry and its underline
        lnameFrame = Frame(nameFrame, bg="#ffffff")
        lnameFrame.pack(side="left")

        # Last name entry
        self.lnameEntry = Entry(lnameFrame, font=("Krub", 13), width=15, border=0, fg="gray")
        self.lnameEntry.pack(side="top", padx=(2, 0))
        self.lnameEntry.insert(0, 'Lastname')
        self.lnameEntry.bind('<FocusIn>', self.on_lname_click)
        self.lnameEntry.bind('<FocusOut>', self.on_lname_focusout)

        # Add underline for last name entry
        Frame(lnameFrame, width=184, height=2, bg="#737d28").pack(side="top", padx=(2, 0))
        
        # CONTACT SECTION
        contactFrame= Frame(signupFrame, width=470, bg="#ffffff")
        contactFrame.pack()
        
        self.contactEntry = Entry(contactFrame, font=("Krub", 13), width=32, border=0, fg="gray")
        self.contactEntry.pack(side="top", pady=(20, 0))
        self.contactEntry.insert(0, 'Contact no.')
        self.contactEntry.bind('<FocusIn>', self.on_contact_click)
        self.contactEntry.bind('<FocusOut>', self.on_contact_focusout)
        Frame(contactFrame, width=370, height=2, bg="#737d28").pack(side="top")
        
        # EMAIL SECTION
        emailFrame= Frame(signupFrame, width=470, bg="#ffffff")
        emailFrame.pack()
        
        self.emailEntry = Entry(emailFrame, font=("Krub", 13), width=32, border=0, fg="gray")
        self.emailEntry.pack(side="top", pady=(20, 0))
        self.emailEntry.insert(0, 'E-mail')
        self.emailEntry.bind('<FocusIn>', self.on_email_click)
        self.emailEntry.bind('<FocusOut>', self.on_email_focusout)
        Frame(emailFrame, width=370, height=2, bg="#737d28").pack(side="top")
        
        # PASSWORD SECTION
        passFrame = Frame(signupFrame, width=470, bg="#ffffff")
        passFrame.pack(side="top", pady=(20, 0))

        # Sub-frame for the password entry and its underline
        pass1Frame = Frame(passFrame, bg="#ffffff")
        pass1Frame.pack(side="left")

        # password entry
        self.pass1Entry = Entry(pass1Frame, font=("Krub", 13), width=15, border=0,fg="gray", show='')
        self.pass1Entry.insert(0, 'Password')
        self.pass1Entry.bind('<FocusIn>', self.on_pass1_click)
        self.pass1Entry.bind('<FocusOut>', self.on_pass1_focusout)
        self.pass1Entry.pack(side="top", padx=(0, 2))
        
        # Add underline for password entry
        Frame(pass1Frame, width=184, height=2, bg="#737d28").pack(side="top", padx=(0,2))

        # Sub-frame for the last name entry and its underline
        pass2Frame = Frame(passFrame, bg="#ffffff")
        pass2Frame.pack(side="left")

        # Last name entry
        self.pass2Entry = Entry(pass2Frame, font=("Krub", 13), width=15, border=0, fg="gray", show='')
        self.pass2Entry.insert(0, 'Confirm Password')
        self.pass2Entry.bind('<FocusIn>', self.on_pass2_click)
        self.pass2Entry.bind('<FocusOut>', self.on_pass2_focusout)
        self.pass2Entry.pack(side="top", padx=(2, 0))

        # Add underline for last name entry
        Frame(pass2Frame, width=184, height=2, bg="#737d28").pack(side="top", padx=(2, 0))
        
        self.toggle_btn = Button(signupFrame, text='Show Password', font=("Krub", 10), bg="#ffffff", fg="#8d9e36", activebackground="#ffffff", activeforeground="#8d9e36", cursor='hand2', border=0, command=self.toggle_password)
        self.toggle_btn.pack(side="top", pady=(10, 0))
        
        # Add a sign up button
        signupBtn = Button(signupFrame, text="Sign Up", font=("Krub", 10), width=30, bg="#8d9e36", fg="#ffffff", activebackground="#737d28", activeforeground="#ffffff", cursor='hand2', border=0)
        signupBtn.pack(side="top", pady=(30, 10))

    def on_fname_click(self, event):
        if self.fnameEntry.get() == 'Firstname':
            self.fnameEntry.delete(0, tk.END)
            self.fnameEntry.insert(0, '')
            self.fnameEntry.config(fg='black')

    def on_fname_focusout(self, event):
        if self.fnameEntry.get() == '':
            self.fnameEntry.insert(0, 'Firstname')
            self.fnameEntry.config(fg='grey')

    def on_lname_click(self, event):
        if self.lnameEntry.get() == 'Lastname':
            self.lnameEntry.delete(0, tk.END)
            self.lnameEntry.insert(0, '')
            self.lnameEntry.config(fg='black')

    def on_lname_focusout(self, event):
        if self.lnameEntry.get() == '':
            self.lnameEntry.insert(0, 'Lastname')
            self.lnameEntry.config(fg='grey')

    def on_contact_click(self, event):
        if self.contactEntry.get() == 'Contact no.':
            self.contactEntry.delete(0, tk.END)
            self.contactEntry.insert(0, '')
            self.contactEntry.config(fg='black')

    def on_contact_focusout(self, event):
        if self.contactEntry.get() == '':
            self.contactEntry.insert(0, 'Contact no.')
            self.contactEntry.config(fg='grey')

    def on_email_click(self, event):
        if self.emailEntry.get() == 'E-mail':
            self.emailEntry.delete(0, tk.END)
            self.emailEntry.insert(0, '')
            self.emailEntry.config(fg='black')

    def on_email_focusout(self, event):
        if self.emailEntry.get() == '':
            self.emailEntry.insert(0, 'E-mail')
            self.emailEntry.config(fg='grey')

    def on_pass1_click(self, event):
        if self.pass1Entry.get() == 'Password':
            self.pass1Entry.delete(0, tk.END)
            self.pass1Entry.insert(0, '')
            self.pass1Entry.config(fg='black')

    def on_pass1_focusout(self, event):
        if self.pass1Entry.get() == '':
            self.pass1Entry.insert(0, 'Password')
            self.pass1Entry.config(fg='grey')

    def on_pass2_click(self, event):
        if self.pass2Entry.get() == 'Confirm Password':
            self.pass2Entry.delete(0, tk.END)
            self.pass2Entry.insert(0, '')
            self.pass2Entry.config(fg='black')

    def on_pass2_focusout(self, event):
        if self.pass2Entry.get() == '':
            self.pass2Entry.insert(0, 'Confirm Password')
            self.pass2Entry.config(fg='grey')
            
    def toggle_password(self):
        if self.pass1Entry.cget('show') == '':
            if self.pass1Entry.get() != 'Password':
                self.pass1Entry.config(show='*')
                self.pass2Entry.config(show='*')
            self.toggle_btn.config(text='Show Password')
        else:
            self.pass1Entry.config(show='')
            self.pass2Entry.config(show='')
            self.toggle_btn.config(text='Hide Password')
            
            
# def toggle_password():
#     if loginPass.cget('show') == '':
#         if loginPass.get() != 'Password':
#             loginPass.config(show='*')
#         toggle_btn.config(text='Show Password')
#     else:
#         loginPass.config(show='')
#         toggle_btn.config(text='Hide Password')