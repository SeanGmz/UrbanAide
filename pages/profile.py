import tkinter as tk
from tkinter import Frame, Label, Button
import customtkinter

class ProfilePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        profileFrame = customtkinter.CTkScrollableFrame(self, width=800, height=560, fg_color="white")
        profileFrame.pack(expand=True, fill="both")
        
        titleFrame = Frame(profileFrame, borderwidth=5, relief="groove", bg="#ffffff")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Profile Page", font=("Krub", 25), bg="#ffffff").pack(side="left", padx=10, pady=10)
        
        # PROFILE Details
        profileDetails = Frame(profileFrame, borderwidth=5, relief="groove", bg="#ffffff")
        profileDetails.pack(side="top", fill="x", expand=True)
        
        profileToplayer = Frame(profileDetails, bg="#ffffff")
        profileToplayer.pack(side="top", fill="x", expand=True)
        
        Label(profileToplayer, text="Personal Details:", font=("Krub", 15), bg="#ffffff").pack(side="left", padx=10, pady=10)
        editProfile = Button(profileToplayer, text="Edit Profile", font=("Krub", 11), width=15, bg="#737c29", fg="#ffffff", border=0, activebackground="#666E24", activeforeground="#ffffff", cursor="hand2")
        editProfile.pack(side="right", padx=10, pady=10)
        
        personalDetails = Frame(profileDetails, bg="#ffffff", borderwidth=5, relief="groove")
        personalDetails.pack(side="top", fill="x", expand=True, padx=20, pady=20)
        
        personalDetsCol1 = Frame(personalDetails, bg="#ffffff", borderwidth=5, relief="groove")
        personalDetsCol1.pack(side="left", fill="x", expand=True)
        
        personalDetsCol2 = Frame(personalDetails, bg="#ffffff", borderwidth=5, relief="groove")
        personalDetsCol2.pack(side="left", fill="x", expand=True)
        
        Label(personalDetsCol1, text="Firstname: ", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(personalDetsCol1, text="Lastname: ", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(personalDetsCol2, text="Contact: ", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        Label(personalDetsCol2, text="Email: ", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
        
        # PARTICIPATION HISTORY
        
        partHistory = Frame(profileFrame, borderwidth=5, relief="groove", bg="#ffffff")
        partHistory.pack(side="top", fill="x", expand=True)
        
        Label(partHistory, text="Participation History", font=("Krub", 15), bg="#ffffff").pack(side="top", anchor="w", padx=10, pady=10)

