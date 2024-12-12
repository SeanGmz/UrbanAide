import tkinter as tk
from tkinter import *
from tkinter import Frame, Label, Button, messagebox
import os
import customtkinter
from datetime import datetime
import sqlite3
from pages.modules.navbar import create_navbar

def authenticate(userinput, password):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE (user_email = ? or user_contact = ?) AND user_pass = ?;", (userinput, userinput, password))
    user = cursor.fetchone()
    conn.close()
    return user

def open_main(controller):
    if controller.logged_in_user:
        print("Opening main application")
        controller.create_navbar_and_show_initial_frame()
    else:
        messagebox.showerror("Error", "User is not logged in.")

def handle_login(controller, loginEntry, loginPass):
# Comment out the login validation logic
    # userinput = loginEntry.get()
    # password = loginPass.get()

    # user = authenticate(userinput, password)
    # if user:
    #     controller.logged_in_user = user  # Store the logged-in user
    #     controller.is_admin = user[6] == "admin"  # Check if the role is "admin"
    #     print(f"Login successful: {controller.logged_in_user}, is_admin: {controller.is_admin}")
    #     open_main(controller)  # Open the main application
    # else:
    #     messagebox.showerror("Login Failed", "Invalid email or password")

    # Directly set the logged_in_user and is_admin flags for testing
    controller.logged_in_user = ("test_user", "Test", "User", "test@example.com", "1234567890", "password", "admin")
    controller.is_admin = True  # Set to True for admin, False for non-admin
    open_main(controller)  # Open the main application

def handle_signup(parent, first_name, last_name, email, contact, password, role):
    if not first_name or not last_name or not email or not contact or not password:
        messagebox.showerror("Error", "All fields are required", parent = parent)
        return False

    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO USERS (user_fname,  user_lname, user_email, user_contact, user_pass, user_role) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, email, contact, password, role))
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Account created successfully")
    return True

def handle_participation(user_id, post_id):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()

    # Check if the user has already participated in the post
    cursor.execute("SELECT * FROM participation WHERE part_user = ? AND part_post = ?", (user_id, post_id))
    participation = cursor.fetchone()

    if participation:
        # If the user has already participated, remove the participation (unlike)
        cursor.execute("DELETE FROM participation WHERE part_user = ? AND part_post = ?", (user_id, post_id))
        cursor.execute("UPDATE posts SET post_part_count = post_part_count - 1 WHERE post_id = ?", (post_id,))
        conn.commit()
        conn.close()
        return "unliked"
    else:
        # If the user has not participated, add the participation (like)
        cursor.execute("INSERT INTO participation (part_user, part_post) VALUES (?, ?)", (user_id, post_id))
        cursor.execute("UPDATE posts SET post_part_count = post_part_count + 1 WHERE post_id = ?", (post_id,))
        conn.commit()
        conn.close()
        return "liked"

def fetch_user_participation(user_id):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT part_post FROM participation WHERE part_user = ?", (user_id,))
    participating_user = cursor.fetchall()
    conn.close()
    return [p[0] for p in participating_user] 


def create_event_card(parent, post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, part_count, status, author, user_id, user_participation):
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
        expandedPart = Label(bottomLayer, text=f"Participants: {part_count}", font=("Krub", 12, "italic"), bg="#ffffff", fg="gray")
        expandedPart.pack(side="left", anchor="w")
        minBtn = Button(bottomLayer, text="Minimize", font=("krub", 12), command=modal.destroy, border=0, width=20, bg="#737c29", fg="#ffffff", activebackground="#666E24", activeforeground="#ffffff", cursor="hand2")
        minBtn.pack(side="bottom", anchor="e")
                
    def participate():
        nonlocal part_count
        result = handle_participation(user_id, post_id)
        if result == "liked":
            part_count += 1
            EventBtn.config(text="Cancel", width=11, bg="#777777", fg="#ffffff", activebackground="#9e9e9e", activeforeground="#ffffff")
            
        else:
            part_count -= 1
            EventBtn.config(text="Participate", width=11,font=("krub", 9), bg="#737c29", fg="#ffffff", activebackground="#666E24", activeforeground="#ffffff", border=0, cursor="hand2", command=participate)
            
        EventParticipants.config(text=f"Participants: {part_count}")
        expandedPart.config(text=f"Participants: {part_count}")

    if status == "ongoing" or status == "ended":
        Expand = Button(PartiFrame, text="Expand", font=("krub", 9), command=show_modal, fg="#737c29", bg="#f0f0f0",activeforeground="#666E24", border=0, cursor="hand2")
        Expand.pack(side="right", padx=5)
    else:
        EventBtn = Button(PartiFrame, text="Participate", font=("krub", 9), width=11, bg="#737c29", fg="#ffffff", activebackground="#666E24", activeforeground="#ffffff", border=0, cursor="hand2", command=participate)
        if post_id in user_participation:
            EventBtn.config(text="Cancel", font=("krub", 9), width=11, bg="#777777", fg="#ffffff", activebackground="#9e9e9e", activeforeground="#ffffff")
        EventBtn.pack(side="right")
        Expand = Button(PartiFrame, text="Expand", font=("krub", 9), command=show_modal, fg="#737c29", bg="#f0f0f0",activeforeground="#666E24", border=0, cursor="hand2")
        Expand.pack(side="right", padx=5)
    
    
    
def add_event_cards(container, cards, max_columns, user_id):
    user_participation = fetch_user_participation(user_id)
    row_frame = None
    for i, card in enumerate(cards):
        if i % max_columns == 0:
            row_frame = Frame(container, bg="#ffffff")
            row_frame.pack(side="top", expand=True)
        create_event_card(row_frame, *card, user_id, user_participation)



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

def fetch_user_history(user_id):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT posts.post_id, posts.post_name, posts.post_desc, posts.post_from, posts.post_until, posts.time_from, posts.time_until, posts.post_location, posts.post_landmark, posts.post_part_count, posts.post_status, posts.post_author
        FROM posts
        JOIN participation ON posts.post_id = participation.part_post
        WHERE participation.part_user = ?
    """, (user_id,))
    
    events = cursor.fetchall()
    conn.close()
    return events


def table_insert_users(treeview):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, user_fname, user_lname, user_contact, user_email, user_pass, user_role FROM users")
    users = cursor.fetchall()
    conn.close()

    for count, user in enumerate(users):
        tag = 'evenrow' if count % 2 == 0 else 'oddrow'
        treeview.insert("", "end", values=user, tags=(tag,))

    treeview.tag_configure("evenrow", background="#f0f0f0")
    treeview.tag_configure("oddrow", background="#ffffff")
        

def populate_entries(event, treeview, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry):
    selected = treeview.focus()
    values = treeview.item(selected, 'values')
    if values:
        fnameEntry.delete(0, tk.END)
        fnameEntry.insert(0, values[1])
        lnameEntry.delete(0, tk.END)
        lnameEntry.insert(0, values[2])
        emailEntry.delete(0, tk.END)
        emailEntry.insert(0, values[4])
        numEntry.delete(0, tk.END)
        numEntry.insert(0, values[3])
        passEntry.delete(0, tk.END)
        passEntry.insert(0, values[5])
        roleEntry.delete(0, tk.END)
        roleEntry.insert(0, values[6])
        
def clear_entries(fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry):
    fnameEntry.delete(0, tk.END)
    lnameEntry.delete(0, tk.END)
    emailEntry.delete(0, tk.END)
    numEntry.delete(0, tk.END)
    passEntry.delete(0, tk.END)
    roleEntry.delete(0, tk.END) 
        
    
def admin_add_user(treeview, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_fname, user_lname, user_contact, user_email, user_pass, user_role) VALUES (?, ?, ?, ?, ?, ?)",
                   (fnameEntry.get(), lnameEntry.get(), numEntry.get(), emailEntry.get(), passEntry.get(), roleEntry.get()))
    conn.commit()
    new_user_id = cursor.lastrowid
    conn.close()
    treeview.insert("", "end", values=(new_user_id, fnameEntry.get(), lnameEntry.get(), numEntry.get(), emailEntry.get(), passEntry.get(), roleEntry.get()))
    messagebox.showinfo("Success", "User added successfully")
    
    clear_entries(fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry)

def admin_update_user(treeview, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry):
    selected = treeview.focus()
    values = treeview.item(selected, 'values')
    if values:
        conn = sqlite3.connect('urbanaid_db.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET user_fname = ?, user_lname = ?, user_contact = ?, user_email = ?, user_pass = ?, user_role = ? WHERE user_id = ?",
                       (fnameEntry.get(), lnameEntry.get(), numEntry.get(), emailEntry.get(), passEntry.get(), roleEntry.get(), values[0]))
        conn.commit()
        conn.close()
        treeview.item(selected, values=(values[0], fnameEntry.get(), lnameEntry.get(), numEntry.get(), emailEntry.get(), passEntry.get(), roleEntry.get()))
        messagebox.showinfo("Success", "User updated successfully")
        clear_entries(fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry)

def admin_delete_user(treeview, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry):
    selected = treeview.focus()
    values = treeview.item(selected, 'values')
    if values:
        conn = sqlite3.connect('urbanaid_db.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE user_id = ?", (values[0],))
        conn.commit()
        conn.close()
        treeview.delete(selected)
        messagebox.showinfo("Success", "Record deleted successfully")
        clear_entries(fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry)