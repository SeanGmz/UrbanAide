import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from signup import SignupWindow
from modules.functions import handle_login

root = tk.Tk()
root.title("Login")
root.geometry("1080x600")
root.configure(bg="#ffffff")
root.resizable(False, False)

def on_entry_click(event):
    if loginEntry.get() == 'E-mail/Contact No.':
       loginEntry.delete(0, END)
       loginEntry.insert(0, '')
       loginEntry.config(fg = 'black')
def on_entry_focusout(event):
    if loginEntry.get() == '':
        loginEntry.insert(0, 'E-mail/Contact No.')
        loginEntry.config(fg = 'grey')
        
def on_pass_click(event):
    if loginPass.get() == 'Password':
        loginPass.delete(0, END)
        loginPass.config(fg='black', show='*')

def on_pass_focusout(event):
    if loginPass.get() == '':
        loginPass.insert(0, 'Password')
        loginPass.config(fg='grey', show='')

def toggle_password():
    if loginPass.cget('show') == '':
        if loginPass.get() != 'Password':
            loginPass.config(show='*')
        toggle_btn.config(text='Show Password')
    else:
        loginPass.config(show='')
        toggle_btn.config(text='Hide Password')

img = Image.open("resources/signin_img.png")
resized_img = img.resize((550, 400))
img = ImageTk.PhotoImage(resized_img)

Label(root, image=img, bg="#ffffff").pack(side="left", padx=(20,0))

loginFrame = Frame(root, width=470, height=470, bg="#ffffff")
loginFrame.pack_propagate(False)
loginFrame.pack(side="right", padx=(0,20))

heading = Label(loginFrame, text="Sign In", font=("Krub", 25), bg="#ffffff", fg="#8d9e36")
heading.pack(side = "top", pady=(80, 30))

loginEntry = Entry(loginFrame, width=30, font=("Krub", 13), fg="gray", border=0, )
loginEntry.pack(side="top")
loginEntry.insert(0, 'E-mail/Contact No.')
loginEntry.bind('<FocusIn>', on_entry_click)
loginEntry.bind('<FocusOut>', on_entry_focusout)
Frame(loginFrame, width=350, height=2, bg="#737d28").pack(side="top")

loginPass = Entry(loginFrame, width=30, font=("Krub", 13), fg="gray", border=0, show='')
loginPass.pack(side="top", pady=(20, 0))
loginPass.insert(0, 'Password')
loginPass.bind('<FocusIn>', on_pass_click)
loginPass.bind('<FocusOut>', on_pass_focusout)
Frame(loginFrame, width=350, height=2, bg="#737d28").pack(side="top")

toggle_btn = Button(loginFrame, text='Show Password', font=("Krub", 10), bg="#ffffff", fg="#8d9e36", activebackground="#ffffff", activeforeground="#8d9e36", cursor='hand2', border=0, command=toggle_password)
toggle_btn.pack(side="top", pady=(10, 0))

signinBtn = Button(loginFrame, text="Sign In", font=("Krub", 10), width=30, bg="#8d9e36", fg="#ffffff", activebackground="#737d28", activeforeground="#ffffff", cursor='hand2', border=0, command=lambda: handle_login(root, loginEntry, loginPass))
signinBtn.pack(side="top", pady=(30, 10))

signupFrame = Frame(loginFrame, width=470, height=50, bg="#ffffff")
signupFrame.pack(side="top")

Label(signupFrame, text="Don't have an account? ", font=("Krub", 10),bg="#ffffff", fg="black").pack(side="left", pady=(10, 0))
signupBtn = Button(signupFrame, text="Click here to sign up", font=("Krub", 10), bg="#ffffff", fg="#8d9e36", activebackground="#ffffff", activeforeground="#8d9e36", cursor='hand2', border=0, command=lambda: SignupWindow(root))
signupBtn.pack(side="left", pady=(10, 0))

root.mainloop()