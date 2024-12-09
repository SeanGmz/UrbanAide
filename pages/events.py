import tkinter as tk
from tkinter import Frame, Label

class EventsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="Events Page", font=("Krub", 25)).pack(pady=20)