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
        titleFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Events Page", font=("Krub", 25)).pack(side="left", padx=10, pady=10)
        
        # SORT DROPDOWN FOR EVENTS
        sortOptions = ["All", "Ongoing", "Upcoming", "Ended"]
        sortFrame = customtkinter.CTkOptionMenu(titleFrame, values = sortOptions, width=120, height=30, font=("Krub", 16), dropdown_font=("Krub", 16), dropdown_fg_color="#dadada", fg_color="#dadada", button_color="#dadada", text_color ="#000000", dropdown_text_color="#000000", button_hover_color="#d4d4d4", dropdown_hover_color="#d4d4d4")
        sortFrame.pack(side="right", padx=(0,10), pady=10)
        sortLabel = Label(titleFrame, text="Sort by:", font=("Krub", 12))
        sortLabel.pack(side="right", pady=10)
        
        

        # Container for Ongoing Events section
        ongoingFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        ongoingFrame.pack(side="top", fill="x", expand=True)
        Label(ongoingFrame, text="Ongoing Events", font=("Krub", 15)).pack(side="top", anchor='w', padx=10, pady=10)
        
        # Container for Ongoing events
        ogEventframe = Frame(ongoingFrame, borderwidth=5, relief="groove", height=400, width=100)
        ogEventframe.pack(side="bottom", fill="both", expand=True)
        
        
        ongoing_event_cards = fetch_events("ongoing")
        
        # Add event cards to the container
        add_event_cards(ogEventframe, ongoing_event_cards, max_columns=2)
        
        
        
        # Container for events: Upcoming Events
        upcomingFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        upcomingFrame.pack(side="top", fill="x", expand=True)
        Label(upcomingFrame, text="Upcoming Events", font=("Krub", 15)).pack(side="top", anchor="w", padx=10, pady=10)
        
        upEventframe = Frame(upcomingFrame, borderwidth=5, relief="groove", height = 400, width=100)
        upEventframe.pack(side="bottom", fill="both", expand=True)
        
        upcoming_event_cards = fetch_events("upcoming")
        add_event_cards(upEventframe, upcoming_event_cards, max_columns=2)
        
        
        
        # Container for events: Ended Events
        endedFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        endedFrame.pack(side="top", fill="x", expand=True)
        Label(endedFrame, text="Ended Events", font=("Krub", 15)).pack(side="top", anchor="w", padx=10, pady=10)
        
        enEventframe = Frame(endedFrame, borderwidth=5, relief="groove", height = 400, width=100)
        enEventframe.pack(side="bottom", fill="both", expand=True)
        
        ended_event_cards = fetch_events("ended")
        add_event_cards(enEventframe, ended_event_cards, max_columns=2)