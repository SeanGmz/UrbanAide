import tkinter as tk
from tkinter import *
from tkinter import Frame, Label, Button
import sqlite3

def create_event_card(parent, post_id, title, desc, date_from, date_until, location, landmark, part_count, status, author):
    Events = Frame(parent, borderwidth=5, relief="groove", bg="red", width=260, height=160)
    Events.pack_propagate(False)
    Events.pack(side="left", expand=True, padx=20, pady=20)
    
    # Store post_id as an attribute of the Events frame
    Events.post_id = post_id
    EventAuthor = Label(Events, text=f"{author} (Admin)", font=("Krub", 9))
    EventAuthor.pack(side="top", anchor="w", padx=5, pady=(5, 0))
    
    EventTitle = Label(Events, text=title, font=("Krub", 12))
    EventTitle.pack(side="top", anchor="w", padx=5)
    EventDate = Label(Events, text=f"{date_from} - {date_until}", font=("krub", 8))
    EventDate.pack(side="top", anchor="w", padx=5)
    
    # Container for bottom part of the card
    PartiFrame = Frame(Events)
    PartiFrame.pack(side="bottom", anchor="s", fill="x", expand=True, padx=5, pady=(0, 5))
    
    EventParticipants = Label(PartiFrame, text=f"Participants: {part_count}", font=("krub", 8, "italic"))
    EventParticipants.pack(side="left")
    
    if status == "ongoing":
        Expand = Button(PartiFrame, text="Expand", font=("krub", 8), bg="green", fg="white", activebackground="green", activeforeground="white")
        Expand.pack(side="right", padx=5)
    else:
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

def fetch_events(status):
    conn = sqlite3.connect('urban.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT post_id, post_name, post_desc, post_from, post_until, post_location, post_landmark, post_part_count, post_status, post_author 
        FROM posts
        WHERE post_status = ?
    """, (status,))
    rows = cursor.fetchall()

    conn.close()

    return rows