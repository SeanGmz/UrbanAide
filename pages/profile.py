import tkinter as tk
from tkinter import Frame, Label, Button
import customtkinter
from pages.modules.functions import add_event_cards, fetch_user_history

class ProfilePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
    
        self.controller = controller
        
        profileFrame = customtkinter.CTkScrollableFrame(self, fg_color="white", scrollbar_button_color="#8d9e36", scrollbar_button_hover_color="#6d7a2a")
        profileFrame.pack(expand=True, fill="both")
        
        titleFrame = Frame(profileFrame, bg="#ffffff")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Profile Page", font=("Krub", 25), bg="#ffffff").pack(side="left", padx=10, pady=10)
        
        # PROFILE Details
        self.profileDetails = Frame(profileFrame, borderwidth=5, relief="groove", bg="#ffffff")
        self.profileDetails.pack(side="top", fill="x", expand=True)
        
        profileToplayer = Frame(self.profileDetails, bg="#ffffff")
        profileToplayer.pack(side="top", fill="x", expand=True)
        
        Label(profileToplayer, text="Personal Details:", font=("Krub", 15), bg="#ffffff").pack(side="left", padx=10, pady=10)
        editProfile = Button(profileToplayer, text="Edit Profile", font=("Krub", 11), width=15, bg="#737c29", fg="#ffffff", border=0, activebackground="#666E24", activeforeground="#ffffff", cursor="hand2")
        editProfile.pack(side="right", padx=10, pady=10)
        
        self.personalDetails = Frame(self.profileDetails, bg="#ffffff", borderwidth=5, relief="groove")
        self.personalDetails.pack(side="top", fill="x", expand=True, padx=20, pady=20)
        
        self.personalDetsCol1 = Frame(self.personalDetails, bg="#ffffff", borderwidth=5, relief="groove")
        self.personalDetsCol1.pack(side="left", fill="x", expand=True)
        
        self.personalDetsCol2 = Frame(self.personalDetails, bg="#ffffff", borderwidth=5, relief="groove")
        self.personalDetsCol2.pack(side="left", fill="x", expand=True)
        
        
        self.partHistory = Frame(profileFrame, bg="#ffffff")
       
        self.partHistory.pack(side="top", fill="x", expand=True)
        
        Label(self.partHistory, text="Participation History", font=("Krub", 15), bg="#ffffff").pack(side="top", anchor="w", padx=10, pady=10)
        self.cont = Frame(self.partHistory, bg="#ffffff", borderwidth=5, relief="groove")
        self.cont.pack(side="top", fill="both", expand=True)
    def update_user_details(self):
        logged_in_user = self.controller.logged_in_user
        print(f"Updating user details for: {logged_in_user}")
        
        if logged_in_user is not None:
             # Clear existing labels
            for widget in self.personalDetsCol1.winfo_children():
                widget.destroy()
            for widget in self.personalDetsCol2.winfo_children():
                widget.destroy()
            print(f"{logged_in_user}")
            Label(self.personalDetsCol1, text=f"Firstname: {logged_in_user[1]}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
            Label(self.personalDetsCol1, text=f"Lastname: {logged_in_user[2]}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
            Label(self.personalDetsCol2, text=f"Contact: {logged_in_user[3]}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
            Label(self.personalDetsCol2, text=f"Email: {logged_in_user[4]}", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w")
            
            for widget in self.cont.winfo_children():
                if isinstance(widget, Frame):
                    widget.destroy()
                    
            participation_history = fetch_user_history(logged_in_user[0])
            add_event_cards(self.cont, participation_history, max_columns=3, user_id=logged_in_user[0])
        else:
            print("User not logged in")
            
        