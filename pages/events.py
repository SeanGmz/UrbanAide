import tkinter as tk
from tkinter import Frame, Label, Button
import customtkinter
from pages.modules.functions import create_event_card, add_event_cards, fetch_events

class EventsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        eventFrame = customtkinter.CTkScrollableFrame(self, width=800, height=560, fg_color="white")
        eventFrame.pack(expand=True, fill="both")
        
        # Container for page title: Events Page
        titleFrame = Frame(eventFrame, borderwidth=5, relief="groove", bg="#ffffff")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Events Page", font=("Krub", 25), bg="#ffffff").pack(side="left", padx=10, pady=10)
        
        # SORT DROPDOWN FOR EVENTS
        sortOptions = ["All", "Ongoing", "Upcoming", "Ended"]
        sortFrame = customtkinter.CTkOptionMenu(titleFrame, values = sortOptions, command=self.sort_events, width=120, height=30, font=("Krub", 16), dropdown_font=("Krub", 16), dropdown_fg_color="#e8e8e8", fg_color="#e8e8e8", button_color="#e8e8e8", text_color ="#000000", dropdown_text_color="#000000", button_hover_color="#dddddd", dropdown_hover_color="#dddddd")
        sortFrame.pack(side="right", padx=(0,10), pady=10)
        sortLabel = Label(titleFrame, text="Sort by:", font=("Krub", 12), bg="#ffffff")
        sortLabel.pack(side="right", pady=10)
        


        # Container for Ongoing Events section
        self.ongoingFrame = Frame(eventFrame, borderwidth=5, relief="groove", bg="#ffffff")
        self.ongoingFrame.pack(side="top", fill="x", expand=True)
        Label(self.ongoingFrame, text="Ongoing Events", font=("Krub", 15), bg="#ffffff").pack(side="top", anchor='w', padx=10, pady=10)
        
        # Container for Ongoing events
        ogEventframe = Frame(self.ongoingFrame, borderwidth=5, relief="groove", height=400, width=100, bg="#ffffff")
        ogEventframe.pack(side="bottom", fill="both", expand=True)
        
        
        ongoing_event_cards = fetch_events("ongoing")
        
        # Add event cards to the container
        add_event_cards(ogEventframe, ongoing_event_cards, max_columns=2)
        
        
        
        # Container for events: Upcoming Events
        self.upcomingFrame = Frame(eventFrame, borderwidth=5, relief="groove", bg="#ffffff")
        self.upcomingFrame.pack(side="top", fill="x", expand=True)
        Label(self.upcomingFrame, text="Upcoming Events", font=("Krub", 15), bg="#ffffff").pack(side="top", anchor="w", padx=10, pady=10)
        
        upEventframe = Frame(self.upcomingFrame, borderwidth=5, relief="groove", height = 400, width=100, bg="#ffffff")
        upEventframe.pack(side="bottom", fill="both", expand=True)
        
        upcoming_event_cards = fetch_events("upcoming")
        add_event_cards(upEventframe, upcoming_event_cards, max_columns=2)
        
        
        
        # Container for events: Ended Events
        self.endedFrame = Frame(eventFrame, borderwidth=5, relief="groove", bg="#ffffff")
        self.endedFrame.pack(side="top", fill="x", expand=True)
        Label(self.endedFrame, text="Ended Events", font=("Krub", 15), bg="#ffffff").pack(side="top", anchor="w", padx=10, pady=10)
        
        enEventframe = Frame(self.endedFrame, borderwidth=5, relief="groove", height = 400, width=100, bg="#ffffff")
        enEventframe.pack(side="bottom", fill="both", expand=True)
        
        ended_event_cards = fetch_events("ended")
        add_event_cards(enEventframe, ended_event_cards, max_columns=2)
        
    def sort_events(self, selection):
        if selection == "All":
            self.ongoingFrame.pack(side="top", fill="x", expand=True)
            self.upcomingFrame.pack(side="top", fill="x", expand=True, after=self.ongoingFrame)
            self.endedFrame.pack(side="top", fill="x", expand=True, after=self.upcomingFrame)
        elif selection == "Ongoing":
            self.ongoingFrame.pack(side="top", fill="x", expand=True)
            self.upcomingFrame.pack_forget()
            self.endedFrame.pack_forget()
        elif selection == "Upcoming":
            self.ongoingFrame.pack_forget()
            self.upcomingFrame.pack(side="top", fill="x", expand=True)
            self.endedFrame.pack_forget()
        elif selection == "Ended":
            self.ongoingFrame.pack_forget()
            self.upcomingFrame.pack_forget()
            self.endedFrame.pack(side="top", fill="x", expand=True)
            