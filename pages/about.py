import tkinter as tk
from tkinter import Frame, Label

class AboutPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        aboutFrame = Frame(self, bg="#ffffff")
        aboutFrame.pack_propagate(False)
        aboutFrame.pack(side="top", fill="both", expand=True)
        
        Label(aboutFrame, text="TBA hihihi", font=("Krub", 25)).pack(fill="both", expand=True)