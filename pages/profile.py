import tkinter as tk
from tkinter import Frame, Label

class ProfilePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="Profile Page", font=("Krub", 25)).pack(pady=20)