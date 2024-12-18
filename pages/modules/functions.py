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
    userinput = loginEntry.get()
    password = loginPass.get()

    user = authenticate(userinput, password)
    if user:
        controller.logged_in_user = user  # Store the logged-in user
        controller.is_admin = user[6] == "admin"  # Check if the role is "admin"
        print(f"Login successful: {controller.logged_in_user}, is_admin: {controller.is_admin}")
        open_main(controller)  # Open the main application
    else:
        messagebox.showerror("Login Failed", "Invalid email or password")

    # ## Directly set the logged_in_user and is_admin flags for testing
    # controller.logged_in_user = ("test_user", "Test", "User", "test@example.com", "1234567890", "password", "admin")
    # controller.is_admin = True  # Set to True for admin, False for non-admin
    # open_main(controller)  # Open the main application

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
        
        modal.grab_set()
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
        

def fetch_all_events():
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT post_id, post_name, post_desc, post_from, post_until, time_from, time_until, post_location, post_landmark, post_part_count, post_status, post_author FROM posts")
    events = cursor.fetchall()
    conn.close()
    return events
        
        
        
def admin_event_card(parent, post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, part_count, status, refresh_callback):
    Event = Frame(parent, borderwidth=5, relief="flat", bg="#f0f0f0", width=800, height=100)
    Event.pack(side="top", fill="x", expand=True, padx=30, pady=15)
    
    Event.post_id = post_id
    
    date_from_formatted = datetime.strptime(date_from, "%Y-%m-%d").strftime("%B %d, %Y")
    date_until_formatted = datetime.strptime(date_until, "%Y-%m-%d").strftime("%B %d, %Y")
    time_from_formatted = datetime.strptime(time_from, "%H:%M:%S").strftime("%I:%M %p")
    time_until_formatted = datetime.strptime(time_until, "%H:%M:%S").strftime("%I:%M %p")
    
    eventDets = Frame(Event, bg="#f0f0f0", width=500)
    eventDets.pack(side="left", fill="x", expand=True)
    eventTitle = Label(eventDets, text=title, font=("Krub", 17), bg="#f0f0f0")
    eventTitle.pack(side="top", anchor="w", padx=10)
    eventDate = Label(eventDets, text=f"{date_from_formatted} - {date_until_formatted}", font=("Krub", 11), bg="#f0f0f0")
    eventDate.pack(side="top", anchor="w", padx=10)
    eventTime = Label(eventDets, text=f" {time_from_formatted} - {time_until_formatted}", font=("Krub", 11), bg="#f0f0f0")
    eventTime.pack(side="top", anchor="w", padx=10)
    
    partstatusCont = Frame(Event, bg="#f0f0f0")
    partstatusCont.pack(side="left", fill="x", expand=True)
    eventStatus = Label(partstatusCont, text=f"Status: {status}", font=("Krub", 13), bg="#f0f0f0", width=20)
    eventStatus.pack(side="top", anchor="w")
    eventParticipants = Label(partstatusCont, text=f"Participants: {part_count}", font=("Krub", 13), bg="#f0f0f0", fg="gray", width=20)
    eventParticipants.pack(side="top", anchor="w")

    btnCont = Frame(Event, bg="#f0f0f0", width=100)
    btnCont.pack(side="right", fill="both")
    
    viewBtn = Button(btnCont, text="View", font=("Krub", 13), bg="#f0f0f0", fg="#737c29", activeforeground="#666E24", activebackground="#f0f0f0", border=0, width=8, height=1, command=lambda: view_event_modal(parent, post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, status, refresh_callback))
    viewBtn.pack(side="left", padx=(10, 0))
    deleteBtn = Button(btnCont, text="Delete", font=("Krub", 13), bg="#f0f0f0", fg="red", activeforeground="darkred", activebackground="#f0f0f0", border=0, width=8, height=1, command=lambda: delete_event(post_id, refresh_callback))
    deleteBtn.pack(side="left", padx=(10, 0))
    
def view_event_modal(parent, post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, status, refresh_callback):
    modal = Toplevel(parent, bg="#ffffff")
    modal.title("View Event")
    modal.geometry("700x500")
        
    modal.grab_set()
    
    title_var = StringVar(value=title)
    desc_var = StringVar(value=desc)
    date_from_var = StringVar(value=date_from)
    date_until_var = StringVar(value=date_until)
    time_from_var = StringVar(value=time_from)
    time_until_var = StringVar(value=time_until)
    location_var = StringVar(value=location)
    landmark_var = StringVar(value=landmark)
    status_var = StringVar(value=status)
    
    Label(modal, text="View Event", font=("Krub", 18), bg="#ffffff").pack(side="top", anchor="w", pady=(10,20), padx=10)
        
    topContainer = Frame(modal, bg="#ffffff")
    topContainer.pack(side="top", fill="x")
        
    leftContainer = Frame(topContainer, bg="#ffffff")
    leftContainer.pack(side="top", fill="x", expand=True)
        
    titleFrame = Frame(leftContainer, bg="#ffffff")
    titleFrame.pack(side="top", fill="x")
    
    Label(titleFrame, text="Title:", font=("Krub", 12), bg="#ffffff").pack(side="left", anchor="w", padx=10, pady=5)
    titleEntry = customtkinter.CTkEntry(titleFrame, textvariable=title_var, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    titleEntry.pack(side="left", fill="x", expand=True, padx=(0,20))


    Label(titleFrame, text="Status:", font=("Krub", 12), bg="#ffffff").pack(side="left", anchor="w", pady=5)
    statusOptions = ["ongoing", "upcoming", "ended"]
    statusMenu = customtkinter.CTkOptionMenu(titleFrame, variable=status_var, values=statusOptions, width=130, height=40, font=("Krub", 16), dropdown_font=("Krub", 16), dropdown_fg_color="#f0f0f0", fg_color="#f0f0f0", button_color="#f0f0f0", text_color="#000000", dropdown_text_color="#000000", button_hover_color="#dddddd", dropdown_hover_color="#dddddd")
    statusMenu.pack(side="left", fill="x", padx=(0,20), pady=5)

    
    locationFrame = Frame(leftContainer, bg="#ffffff")
    locationFrame.pack(side="top", fill="x")
        
    Label(locationFrame, text="Location:", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10, pady=5)
    locationEntry = customtkinter.CTkEntry(locationFrame, textvariable=location_var, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    locationEntry.pack(side="left", fill="x", expand=True, padx=(0,20))
        
    landmarkFrame = Frame(leftContainer, bg="#ffffff")
    landmarkFrame.pack(side="top", fill="x")
    Label(landmarkFrame, text="Landmark:", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10, pady=5)
    landmarkEntry = customtkinter.CTkEntry(landmarkFrame, textvariable=landmark_var, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    landmarkEntry.pack(side="left", fill="x", expand=True, padx=(0,20))
        
        
        
        # right side of top layer
    rightContainer = Frame(topContainer, bg="#ffffff")
    rightContainer.pack(side="top", fill="x", expand=True)
        
    dateContainer = Frame(rightContainer, bg="#ffffff",)
    dateContainer.pack(side="left", fill="x", expand=True)
        
    dateFromFrame = Frame(dateContainer, bg="#ffffff")
    dateFromFrame.pack(side="top", fill="x", expand=True)
    Label(dateFromFrame, text="Date From (YYYY-MM-DD):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)     
    dateFromEntry = customtkinter.CTkEntry(dateFromFrame, textvariable=date_from_var , fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    dateFromEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
    dateUntilFrame = Frame(dateContainer, bg="#ffffff")
    dateUntilFrame.pack(side="top", fill="x")
    Label(dateUntilFrame, text="Date Until (YYYY-MM-DD):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)
    dateUntilEntry = customtkinter.CTkEntry(dateUntilFrame, textvariable=date_until_var, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    dateUntilEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
    timeContainer = Frame(rightContainer, bg="#ffffff")
    timeContainer.pack(side="left", fill="x", expand=True)
        
    timeFromFrame = Frame(timeContainer, bg="#ffffff")
    timeFromFrame.pack(side="top", fill="x", expand=True)
    Label(timeFromFrame, text="Time From (HH:MM):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)
    timeFromEntry = customtkinter.CTkEntry(timeFromFrame, textvariable=time_from_var, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    timeFromEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
    timeUntilFrame = Frame(timeContainer, bg="#ffffff")
    timeUntilFrame.pack(side="top", fill="x")
    Label(timeUntilFrame, text="Time Until (HH:MM):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)
    timeUntilEntry = customtkinter.CTkEntry(timeUntilFrame, textvariable=time_until_var , fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    timeUntilEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
        
    # bottom layer
    bottomContainer = Frame(modal, bg="#ffffff")
    bottomContainer.pack(side="top", fill="both", expand=True)
        
    Label(bottomContainer, text="Description:", font=("Krub", 12), bg="#ffffff").pack(side="left", anchor="n", padx=10, pady=5)
    descEntry = customtkinter.CTkTextbox(bottomContainer, height=10, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
    descEntry.pack(side="left", fill="both", expand=True, padx=(0,20), pady=5)
    descEntry.insert("1.0", desc)

    submitBtn = Button(modal, text="Update Post", font=("Krub", 12), bg="#8d9e36", fg="#ffffff", width=15, border=0, activebackground="#6d7a2a", activeforeground="#ffffff", cursor='hand2', command=lambda: update_event(post_id, titleEntry, descEntry, dateFromEntry, dateUntilEntry, timeFromEntry, timeUntilEntry, locationEntry, landmarkEntry, status_var.get(), refresh_callback))
    submitBtn.pack(side="right", pady=20, padx=20)
    cancelBtn = Button(modal, text="Cancel", font=("Krub", 12), bg="#ffffff", fg="#737c29", width=15, border=0, activebackground="#ffffff", activeforeground="#666E24", cursor='hand2', command=modal.destroy)
    cancelBtn.pack(side="right", pady=20, padx=20)
        
def update_event(post_id, titleEntry, descEntry, dateFromEntry, dateUntilEntry, timeFromEntry, timeUntilEntry, locationEntry, landmarkEntry, status, refresh_callback):
    title = titleEntry.get()
    desc = descEntry.get("1.0", "end-1c").strip()
    date_from = dateFromEntry.get()
    date_until = dateUntilEntry.get()
    time_from = timeFromEntry.get()
    time_until = timeUntilEntry.get()
    location = locationEntry.get()
    landmark = landmarkEntry.get()

    
    
    if not all([title, desc, date_from, date_until, time_from, time_until, location, landmark, status]):
        messagebox.showerror("Error", "All fields are required")
        return
    
    try:
        datetime.strptime(date_from, "%Y-%m-%d")
        datetime.strptime(date_until, "%Y-%m-%d")
        datetime.strptime(time_from, "%H:%M:%S")
        datetime.strptime(time_until, "%H:%M:%S")
    except ValueError:
        messagebox.showerror("Error", "Invalid date or time format")
        return
 
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE posts SET post_name = ?, post_desc = ?, post_from = ?, post_until = ?, time_from = ?, time_until = ?, post_location = ?, post_landmark = ?,  post_status = ? WHERE post_id = ?", (title, desc, date_from, date_until, time_from, time_until, location, landmark, status, post_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Event updated successfully")
    
    refresh_callback()
    
    titleEntry.master.destroy()



def admin_display_event(container, events, refresh_callback):
    for event in events:
        post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, part_count, status, author = event
        admin_event_card(container, post_id, title, desc, date_from, date_until, time_from, time_until, location, landmark, part_count, status, refresh_callback)
        
def insert_event(title, desc, date_from, date_until, time_from, time_until, location, landmark):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (post_name, post_desc, post_from, post_until, time_from, time_until, post_location, post_landmark, post_part_count, post_status, post_author) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (title, desc, date_from, date_until, time_from, time_until, location, landmark, "0", "upcoming", "2")) # change "2" to user_id
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Event posted successfully")

def delete_event(post_id, refresh_callback):
    conn = sqlite3.connect('urbanaid_db.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE post_id = ?", (post_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Event deleted successfully")
    refresh_callback()