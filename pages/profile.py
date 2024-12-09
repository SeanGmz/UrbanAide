import tkinter as tk
from tkinter import Frame, Label

class ProfilePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        profileFrame = Frame(self, bg="red", width=800, height=560)
        profileFrame.pack_propagate(False)
        profileFrame.pack(pady=20)
        
        Label(profileFrame, text="Profile Page", font=("Krub", 25)).pack(pady=20)