import tkinter as tk
from tkinter import *
from tkinter import Frame, Label, Button
import sqlite3

def create_navbar(root, show_frame, active_page, buttons):
    # Create a frame for the navigation bar with increased width
    navbar = Frame(root, width=270, bg="#333333", height=600, relief="raised", borderwidth=2)
    navbar.pack_propagate(False)
    navbar.pack(side="left", fill="y")

    nav_items = Frame(navbar, bg="#333333")
    nav_items.pack(expand=True, fill="x")

    # Function to create a navigation button
    def create_nav_button(text, page_name):
        bg_color = "#555555" if active_page == page_name else "#333333"
        button = Button(nav_items, text=text, font=("Krub", 12), bg=bg_color, fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: show_frame(page_name))
        button.pack(fill="x", pady=10)
        buttons[page_name] = button

    # Add buttons to the navigation bar
    create_nav_button("Events", "EventsPage")
    create_nav_button("About Us", "AboutUsPage")
    create_nav_button("Profile", "ProfilePage")

    # Add the logout button at the bottom
    btn_logout = Button(navbar, text="Logout", font=("Krub", 12), bg="#333333", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: print("Logout"))
    btn_logout.pack(side="bottom", fill="x", pady=10)
    
# FUNCTION FOR CREATING EVENT CARDS IN PROFILE PAGE
def create_event_card(parent, author, title, date, participants):
    Events = Frame(parent, borderwidth=5, relief="groove", bg="red", width=260, height=160)
    Events.pack_propagate(False)
    Events.pack(side="left", expand=True,padx=20, pady=20)
    
    EventAuthor = Label(Events, text=author, font=("Krub", 9))
    EventAuthor.pack(side="top", anchor="w", padx=5, pady=(5, 0))
    
    EventTitle = Label(Events, text=title, font=("Krub", 12))
    EventTitle.pack(side="top", anchor="w", padx=5)
    EventDate = Label(Events, text=date, font=("krub", 8))
    EventDate.pack(side="top", anchor="w", padx=5)
    
    # Container for bottom part of the card
    PartiFrame = Frame(Events)
    PartiFrame.pack(side="bottom", anchor="s", fill="x", expand=True, padx=5, pady=(0, 5))
    
    EventParticipants = Label(PartiFrame, text=f"Participants: {participants}", font=("krub", 8, "italic"))
    EventParticipants.pack(side="left")
    
    EventBtn = Button(PartiFrame, text="Participate", font=("krub", 8), bg="green", fg="white", activebackground="green", activeforeground="white")
    EventBtn.pack(side="right")
    
    Expand = Button(PartiFrame, text="Expand", font=("krub", 8), bg="green", fg="white", activebackground="green", activeforeground="white")
    Expand.pack(side="right", padx=5)

def add_event_cards(container, cards, max_columns):
    row_frame = None
    for i, card in enumerate(cards):
        if i % max_columns == 0:
            row_frame = Frame(container)
            row_frame.pack(side="top", expand=True)
        create_event_card(row_frame, *card)



# Example event cards data
event_cards = [
    ("Admin", "Event Title 1", "Date from - Date to", 11),
    ("Admin", "Event Title 2", "Date from - Date to", 12),
    ("Admin", "Event Title 9", "Date from - Date to", 13),
    ("Admin", "Event Title 4", "Date from - Date to", 14),
    ("Admin", "Event Title 5", "Date from - Date to", 15),
    ("Admin", "Event Title 5", "Date from - Date to", 15)
]