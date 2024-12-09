import tkinter as tk
from tkinter import *

def create_navbar(root, show_frame):
    # Create a frame for the navigation bar with increased width
    navbar = Frame(root, width=270, bg="#333333", height=600, relief="raised", borderwidth=2)
    navbar.pack_propagate(False)
    navbar.pack(side="left", fill="y")

    nav_items = Frame(navbar, bg="#333333")
    nav_items.pack(expand=True, fill="x")
    # Add buttons to the navigation bar
    btn_events = Button(nav_items, text="Events", font=("Krub", 12), bg="#333333", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: show_frame("EventsPage"))
    btn_events.pack(fill="x", pady=10)

    btn_about_us = Button(nav_items, text="About Us", font=("Krub", 12), bg="#333333", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: show_frame("AboutPage"))
    btn_about_us.pack(fill="x", pady=10)

    btn_profile = Button(nav_items, text="Profile", font=("Krub", 12), bg="#333333", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: show_frame("ProfilePage"))
    btn_profile.pack(fill="x", pady=10)

    btn_logout = Button(navbar, text="Logout", font=("Krub", 12), bg="#333333", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: print("Logout"))
    btn_logout.pack(fill="x", pady=10)