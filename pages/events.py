import tkinter as tk
from tkinter import Frame, Label, Button
import customtkinter


class EventsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        eventFrame = customtkinter.CTkScrollableFrame(self, width=800, height=560, fg_color="white")
        eventFrame.pack(expand=True, fill="both")
        
        # Container for page title: Events Page
        titleFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Events Page", font=("Krub", 25)).pack(side="left", padx=10, pady=10)
        
        # Container for Ongoing Events section
        ongoingFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        ongoingFrame.pack(side="top", fill="x", expand=True)
        Label(ongoingFrame, text="Ongoing Events", font=("Krub", 15)).pack(side="top", anchor='w', padx=10, pady=10)
        
        # Container for Ongoing events
        ogEventframe = Frame(ongoingFrame, borderwidth=5, relief="groove", height=400, width=100)
        ogEventframe.pack(side="bottom", fill="both", expand=True)
        
        # Ongoing event card####################################################
        ogEvents = Frame(ogEventframe, borderwidth=5, relief="groove", bg="red", width=260, height=160)
        ogEvents.pack_propagate(False)
        ogEvents.pack(side="bottom", expand=True, padx=20, pady=20)
        
        ogEventAuthor = Label(ogEvents, text="Admin ", font=("Krub", 9))
        ogEventAuthor.pack(side="top", anchor="w", padx=5, pady=(5    , 0))
        
        ogEventTitle = Label(ogEvents, text="Event Title", font=("Krub", 12))
        ogEventTitle.pack(side="top", anchor="w", padx=5)
        
        ogEventDate = Label(ogEvents, text="Date from - Date to", font=("krub", 8))
        ogEventDate.pack(side="top", anchor="w", padx=5)
        
        # Container for bottom part of the card
        ogPartiFrame = Frame(ogEvents)
        ogPartiFrame.pack(side="bottom", anchor="s", fill="x", expand=True, padx=5, pady=(0, 5))
        
        ogEventParticipants = Label(ogPartiFrame, text="Participants: 11", font=("krub", 8, "italic"))
        ogEventParticipants.pack(side="left")
        
        ogEventBtn = Button(ogPartiFrame, text="Participate", font=("krub", 8), bg="green", fg="white", activebackground="green", activeforeground="white")
        ogEventBtn.pack(side="right")
        
        ogExpand = Button(ogPartiFrame, text="Expand", font=("krub", 8), bg="green", fg="white", activebackground="green", activeforeground="white")
        ogExpand.pack(side="right", padx=5)
        
        ########################################################################
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Container for events: Upcoming Events
        upcomingFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        upcomingFrame.pack(side="top", fill="x", expand=True)
        Label(upcomingFrame, text="Upcoming Events", font=("Krub", 15)).pack(side="left", anchor="nw", padx=10, pady=10)
        
        # Container for events: Ended Events
        endedFrame = Frame(eventFrame, borderwidth=5, relief="groove")
        endedFrame.pack(side="top", fill="x", expand=True)
        Label(endedFrame, text="Ended Events", font=("Krub", 15)).pack(side="left", anchor="nw", padx=10, pady=10)