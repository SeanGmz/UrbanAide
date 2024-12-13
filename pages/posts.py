import tkinter as tk
from tkinter import Frame, Label, Button, Toplevel, Entry, messagebox
import customtkinter
from pages.modules.functions import fetch_all_events, fetch_events, admin_display_event, admin_event_card, insert_event
from datetime import datetime

class EvManagePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.logged_in_user = self.controller.logged_in_user
        
        postsFrame = customtkinter.CTkScrollableFrame(self, width=800, height=580, fg_color="white", scrollbar_button_color="#8d9e36", scrollbar_button_hover_color="#6d7a2a")
        postsFrame.pack(expand=True, fill="both")
        
        # Container for page title: Events Page
        titleFrame = Frame(postsFrame, bg="#ffffff")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Events Manager", font=("Krub", 25), bg="#ffffff").pack(side="left", padx=10, pady=10)

        # Search bar for events
    
        postsCont = Frame(postsFrame, bg="#ffffff")
        postsCont.pack(side="top", fill="both", expand=True)
        postHeader = Frame(postsCont, bg="#ffffff", padx=10)
        postHeader.pack(side="top", fill="x")
        
        searchFrame = Frame(postHeader, bg="#ffffff")
        searchFrame.pack(side="left", fill="x", expand=True)
        Label(searchFrame, text="Search:", font=("Krub", 15), bg="#ffffff").pack(side="left", pady=10)
        self.searchEntry = customtkinter.CTkEntry(searchFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="gray", border_width=1)
        self.searchEntry.pack(side="left", fill="x", expand=True, padx=(0,50), pady=10)

        self.searchEntry.insert(0, "Search events...")
        self.searchEntry.bind("<FocusIn>", self.clear_placeholder)
        self.searchEntry.bind("<FocusOut>", self.add_placeholder)
        self.searchEntry.bind("<KeyRelease>", self.search_events)
        
        addEventbtn = Button(postHeader, text="Create Event", font=("Krub", 12), bg="#8d9e36", fg="#ffffff", width=15, border=0, activebackground="#6d7a2a", activeforeground="#ffffff", cursor='hand2', command=self.create_event_modal)
        addEventbtn.pack(side="right", padx=(20,10))
        
        sortOptions = ["All", "Ongoing", "Upcoming", "Ended"]
        sortFrame = customtkinter.CTkOptionMenu(postHeader, values=sortOptions, width=120, height=30, font=("Krub", 16), dropdown_font=("Krub", 16), dropdown_fg_color="#e8e8e8", fg_color="#e8e8e8", button_color="#e8e8e8", text_color="#000000", dropdown_text_color="#000000", button_hover_color="#dddddd", dropdown_hover_color="#dddddd", command=self.sort_events)
        sortFrame.pack(side="right", padx=(0,20), pady=10)
        sortLabel = Label(postHeader, text="Sort by:", font=("Krub", 12), bg="#ffffff")
        sortLabel.pack(side="right", pady=10)
        
        self.eventsCont = Frame(postsCont, bg="#ffffff")
        self.eventsCont.pack(side="bottom", fill="both", expand=True)
        
        # Fetch and display events
        self.refresh_events()
        
    def clear_placeholder(self, event):
        if self.searchEntry.get() == "Search events...":
            self.searchEntry.delete(0, tk.END)
            self.searchEntry.configure(text_color="#000000")
    
    def add_placeholder(self, event):
        if self.searchEntry.get() == "":
            self.searchEntry.insert(0, "Search events...")
            self.searchEntry.configure(text_color="gray")
    
    def refresh_events(self, status=None):
        for widget in self.eventsCont.winfo_children():
            widget.destroy()
            
        if status == "All" or status is None:
            events = fetch_all_events()
        elif status == "Ongoing":
            events = fetch_events("ongoing")
        elif status == "Upcoming":
            events = fetch_events("upcoming")
        elif status == "Ended":
            events = fetch_events("ended")
        else:
            events = fetch_all_events() 

        admin_display_event(self.eventsCont, events, self.refresh_events)
        
    def sort_events(self, selected_status):  
        self.refresh_events(selected_status)  
        
    def search_events(self, event=None):
        query = self.searchEntry.get().lower()
        all_events = fetch_all_events()
        filtered_events = [event for event in all_events if query in event[1].lower()]
        self.display_filtered_events(filtered_events)
    
    def display_filtered_events(self, events):
        for widget in self.eventsCont.winfo_children():
            widget.destroy()
        admin_display_event(self.eventsCont, events, self.refresh_events)
        
    def create_event_modal(self):
        modal = Toplevel(self, bg="#ffffff")
        modal.title("Create Event")
        modal.geometry("700x500")
        
        modal.grab_set()
        Label(modal, text="Create an Event", font=("Krub", 18), bg="#ffffff").pack(side="top", anchor="w", pady=(10,20), padx=10)
        
        topContainer = Frame(modal, bg="#ffffff")
        topContainer.pack(side="top", fill="x")
        
        leftContainer = Frame(topContainer, bg="#ffffff")
        leftContainer.pack(side="top", fill="x", expand=True)
        
        titleFrame = Frame(leftContainer, bg="#ffffff")
        titleFrame.pack(side="top", fill="x")
    
        Label(titleFrame, text="Title:", font=("Krub", 12), bg="#ffffff").pack(side="left", anchor="w", padx=10, pady=5)
        titleEntry = customtkinter.CTkEntry(titleFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        titleEntry.pack(side="left", fill="x", expand=True, padx=(0,20))
        
        locationFrame = Frame(leftContainer, bg="#ffffff")
        locationFrame.pack(side="top", fill="x")
        
        Label(locationFrame, text="Location:", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10, pady=5)
        locationEntry = customtkinter.CTkEntry(locationFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        locationEntry.pack(side="left", fill="x", expand=True, padx=(0,20))
        
        landmarkFrame = Frame(leftContainer, bg="#ffffff")
        landmarkFrame.pack(side="top", fill="x")
        Label(landmarkFrame, text="Landmark:", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10, pady=5)
        landmarkEntry = customtkinter.CTkEntry(landmarkFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        landmarkEntry.pack(side="left", fill="x", expand=True, padx=(0,20))
        
        
        
        # right side of top layer
        rightContainer = Frame(topContainer, bg="#ffffff")
        rightContainer.pack(side="top", fill="x", expand=True)
        
        dateContainer = Frame(rightContainer, bg="#ffffff",)
        dateContainer.pack(side="left", fill="x", expand=True)
        
        dateFromFrame = Frame(dateContainer, bg="#ffffff")
        dateFromFrame.pack(side="top", fill="x", expand=True)
        Label(dateFromFrame, text="Date From (YYYY-MM-DD):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)     
        dateFromEntry = customtkinter.CTkEntry(dateFromFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        dateFromEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
        dateUntilFrame = Frame(dateContainer, bg="#ffffff")
        dateUntilFrame.pack(side="top", fill="x")
        Label(dateUntilFrame, text="Date Until (YYYY-MM-DD):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)
        dateUntilEntry = customtkinter.CTkEntry(dateUntilFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        dateUntilEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
        timeContainer = Frame(rightContainer, bg="#ffffff")
        timeContainer.pack(side="left", fill="x", expand=True)
        
        timeFromFrame = Frame(timeContainer, bg="#ffffff")
        timeFromFrame.pack(side="top", fill="x", expand=True)
        Label(timeFromFrame, text="Time From (HH:MM):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)
        timeFromEntry = customtkinter.CTkEntry(timeFromFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        timeFromEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
        timeUntilFrame = Frame(timeContainer, bg="#ffffff")
        timeUntilFrame.pack(side="top", fill="x")
        Label(timeUntilFrame, text="Time Until (HH:MM):", font=("Krub", 12), bg="#ffffff").pack(side="left",anchor="w", padx=10)
        timeUntilEntry = customtkinter.CTkEntry(timeUntilFrame, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        timeUntilEntry.pack(side="left", fill="x", padx=(0,20), pady=5, expand=True)
        
        
        
        # bottom layer
        bottomContainer = Frame(modal, bg="#ffffff")
        bottomContainer.pack(side="top", fill="both", expand=True)
        
        Label(bottomContainer, text="Description:", font=("Krub", 12), bg="#ffffff").pack(side="left", anchor="n", padx=10, pady=5)
        descEntry = customtkinter.CTkTextbox(bottomContainer, height=10, fg_color="#ffffff", bg_color="#ffffff", font=("Krub", 16), text_color="#000000", border_width=1)
        descEntry.pack(side="left", fill="both", expand=True, padx=(0,20), pady=5)
        

        submitBtn = Button(modal, text="Post Event", font=("Krub", 12), bg="#8d9e36", fg="#ffffff", width=15, border=0, activebackground="#6d7a2a", activeforeground="#ffffff", cursor='hand2', command=lambda: self.submit_event(titleEntry, descEntry, dateFromEntry, dateUntilEntry, timeFromEntry, timeUntilEntry, locationEntry, landmarkEntry, modal))
        submitBtn.pack(side="right", pady=20, padx=20)
        cancelBtn = Button(modal, text="Cancel", font=("Krub", 12), bg="#ffffff", fg="#737c29", width=15, border=0, activebackground="#ffffff", activeforeground="#666E24", cursor='hand2', command=modal.destroy)
        cancelBtn.pack(side="right", pady=20, padx=20)
        
    def submit_event(self, titleEntry, descEntry, dateFromEntry, dateUntilEntry, timeFromEntry, timeUntilEntry, locationEntry, landmarkEntry, modal):
        title = titleEntry.get()
        desc = descEntry.get("1.0", "end-1c").strip()
        dateFrom = dateFromEntry.get()
        dateUntil = dateUntilEntry.get()
        timeFrom = timeFromEntry.get()
        timeUntil = timeUntilEntry.get()
        location = locationEntry.get()
        landmark = landmarkEntry.get()
        
        if not all([title, desc, dateFrom, dateUntil, timeFrom, timeUntil, location, landmark]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            datetime.strptime(dateFrom, "%Y-%m-%d")
            datetime.strptime(dateUntil, "%Y-%m-%d")
            timeFrom = datetime.strptime(timeFrom, "%H:%M").strftime("%H:%M:%S")
            timeUntil = datetime.strptime(timeUntil, "%H:%M").strftime("%H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format")
            return
        
        print(title)
        print(desc)
        print(dateFrom)
        print(dateUntil)
        print(timeFrom)
        print(timeUntil)
        print(location)
        print(landmark)
        
    
        insert_event(title, desc, dateFrom, dateUntil, timeFrom, timeUntil, location, landmark)
        messagebox.showinfo("Success", "Event posted successfully")
        self.refresh_events()
        modal.destroy()
        