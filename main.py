import tkinter as tk
from tkinter import messagebox
from tkinter import *
from pages.modules.navbar import create_navbar
from pages.profile import ProfilePage
from pages.events import EventsPage
from pages.about import AboutPage

root = tk.Tk()
root.title("UrbanAid")
root.geometry("1080x600")
root.configure(bg="#ffffff")
root.resizable(False, False)

screens = Frame(root)
screens.pack(side="right", fill="both", expand=True)

frames = {}

def show_frame(page_name):
    frame = frames[page_name]
    frame.tkraise()


# Create the navigation bar
create_navbar(root, show_frame)

for x in  (ProfilePage, AboutPage, EventsPage):
    page_name = x.__name__
    frame = x(parent=screens, controller=root)
    frames[page_name] = frame
    frame.grid(row=0, column=0, sticky="nsew")

show_frame("EventsPage")

root.mainloop()