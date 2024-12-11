import tkinter as tk
from tkinter import *
from tkinter import Frame, Label, Button, messagebox
import os
import customtkinter
from datetime import datetime
import sqlite3

def authenticate(userinput, password):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE (user_email = ? or user_contact = ?) AND user_pass = ?;", (userinput, userinput, password))
    user = cursor.fetchone()
    conn.close()
    return user

def open_main():
    os.system('python main.py')


def handle_login(root, loginEntry, loginPass):
    userinput = loginEntry.get()
    password = loginPass.get()

    user = authenticate(userinput, password)
    if user:
        root.destroy()  # Close the login window
        open_main()  # Open the main application
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")
    



def create_event_card(parent, post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, part_count, status, author):
    
    
    Events = Frame(parent, borderwidth=5, relief="groove", bg="#f0f0f0", width=280, height=180)
    Events.pack_propagate(False)
    Events.pack(side="left", expand=True, padx=20, pady=20)
    
    # Store post_id as an attribute of the Events frame
    Events.post_id = post_id
    
    date_from_formatted = datetime.strptime(date_from, "%Y-%m-%d").strftime("%B %d, %Y")
    date_until_formatted = datetime.strptime(date_until, "%Y-%m-%d").strftime("%B %d, %Y")
    time_from_formatted = datetime.strptime(time_from, "%H:%M:%S").strftime("%I:%M %p")
    time_until_formatted = datetime.strptime(time_until, "%H:%M:%S").strftime("%I:%M %p")
    
    EventAuthor = Label(Events, text=f"{author} (Admin)", font=("Krub", 9), fg="#8d9e36", bg="#f0f0f0")
    EventAuthor.pack(side="top", anchor="w", padx=5, pady=(5, 0))
    
    EventTitle = Label(Events, text=title, font=("Krub", 13), fg="#000000", bg="#f0f0f0")
    EventTitle.pack(side="top", anchor="w", padx=5)
    EventDate = Label(Events, text=f"{date_from_formatted} - {date_until_formatted} ", font=("krub", 8), bg="#f0f0f0")
    EventDate.pack(side="top", anchor="w", padx=5)
    EventTime = Label(Events, text=f"{time_from_formatted} - {time_until_formatted}", font=("krub", 8), bg="#f0f0f0")
    EventTime.pack(side="top", anchor="w", padx=5)

    # Container for bottom part of the card
    PartiFrame = Frame(Events, bg="#f0f0f0")
    PartiFrame.pack(side="bottom", anchor="s", fill="x", expand=True, padx=5, pady=(10, 5))
    
    EventParticipants = Label(PartiFrame, text=f"Participants: {part_count}", font=("krub", 8, "italic"), fg="gray", bg="#f0f0f0")
    EventParticipants.pack(side="left")
    
    
    def show_modal():
        modal = Toplevel(parent, padx=20, pady=10, bg="#ffffff")
        modal.title("Event Details")
        modal.geometry("700x400")
        
        topLayer = Frame(modal, height=50, bg="#ffffff")
        topLayer.pack(side="top", fill="x", pady=10)
        Label(topLayer, text=f"{title}", font=("Krub", 17), bg="#ffffff").pack(side="left", anchor="w")
        
        if status == "ongoing":
            Label(topLayer, text="Ongoing", font=("Krub", 12), bg="#ffffff").pack(side="right")
        elif status == "upcoming":
            Label(topLayer, text="Upcoming", font=("Krub", 12), bg="#ffffff").pack(side="right")
        elif status == "ended":
            Label(topLayer, text="Ended", font=("Krub", 12), bg="#ffffff").pack(side="right")
        
        Label(topLayer, text="Status: ", font=("Krub", 12), bg="#ffffff").pack(side="right")
        
        Label(modal, text=f"Posted by: {author} (Admin)", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(modal, text=f"Date: {date_from_formatted} - {date_until_formatted}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(modal, text=f"Time: {time_from_formatted} - {time_until_formatted}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(modal, text=f"Description: {desc}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(modal, text=f"Location: {location}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(modal, text=f"Landmark: {landmark}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        
        bottomLayer = Frame(modal, bg="#ffffff")
        bottomLayer.pack(side="bottom", fill="x")
        Label(bottomLayer, text=f"Participants: {part_count}", font=("Krub", 12, "italic"), bg="#ffffff", fg="gray").pack(side="left", anchor="w")
        minBtn = Button(bottomLayer, text="Minimize", font=("krub", 12), command=modal.destroy, border=0, width=20, bg="#737c29", fg="#ffffff", activebackground="#666E24", activeforeground="#ffffff", cursor="hand2")
        minBtn.pack(side="bottom", anchor="e")
                
    if status == "ongoing" or status == "ended":
        Expand = Button(PartiFrame, text="Expand", font=("krub", 9), width=8, command=show_modal, fg="#737c29", bg="#f0f0f0",activeforeground="#666E24", border=0, cursor="hand2")
        Expand.pack(side="right", padx=5)
    else:
        EventBtn = Button(PartiFrame, text="Participate", font=("krub", 9), bg="#737c29", fg="white", activebackground="#666E24", activeforeground="white", border=0, cursor="hand2")
        EventBtn.pack(side="right")
        Expand = Button(PartiFrame, text="Expand", font=("krub", 9), width=8, command=show_modal, fg="#737c29", bg="#f0f0f0",activeforeground="#666E24", border=0, cursor="hand2")
        Expand.pack(side="right", padx=5)
    
def add_event_cards(container, cards, max_columns):
    row_frame = None
    for i, card in enumerate(cards):
        if i % max_columns == 0:
            row_frame = Frame(container, bg="#ffffff")
            row_frame.pack(side="top", expand=True)
        create_event_card(row_frame, *card)

def fetch_events(status):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT post_id, post_name, post_desc, post_from, post_until, time_from, time_until, post_location, post_landmark, post_part_count, post_status, post_author 
        FROM posts
        WHERE post_status = ?
    """, (status,))
    rows = cursor.fetchall()

    conn.close()

    return rows