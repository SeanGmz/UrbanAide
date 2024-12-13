import tkinter as tk
from tkinter import Frame
from pages.modules.navbar import create_navbar
from pages.events import EventsPage
from pages.about import AboutPage
from pages.profile import ProfilePage
from pages.login import LoginPage  # Import the LoginPage class
from pages.accounts import AccManagePage
from pages.posts import EvManagePage
import os

class UrbanAidApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("UrbanAid")
        self.geometry("1280x650")
        self.resizable(False, False)
        self.configure(bg="#ffffff")

        self.logged_in_user = None
        self.is_admin = False  # Add a flag to indicate if the user is an admin


        # # Directly set the logged_in_user and is_admin flags for testing
        # self.logged_in_user = ("test_user", "Test", "User", "test@example.com", "1234567890", "password", "admin")
        # self.is_admin = False  # Set to True for admin, False for non-admin
        
        # Create a container for the navigation bar and frames
        self.navbar_container = Frame(self, width=270, bg="#333333", height=600, relief="raised", borderwidth=2)
        self.navbar_container.pack_propagate(False)

        # Create a container for the frames
        self.container = Frame(self, bg="#ffffff")
        self.container.pack(side="right", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold the frames
        self.frames = {}

        # Dictionary to hold the navigation buttons
        self.buttons = {}

        # Function to show a frame for the given page name
        def show_frame(page_name):
            print(f"Showing frame: {page_name} with user: {self.logged_in_user}")
            frame = self.frames[page_name]
            if page_name == "ProfilePage" or page_name == "EventsPage":
                frame.update_user_details()
            if page_name == "LoginPage":
                frame.reset_entries()
            frame.tkraise()
            # Update the navbar to highlight the active page
            for btn_page, button in self.buttons.items():
                if btn_page == page_name:
                    button.config(bg="#8d9e36")
                else:
                    button.config(bg="#6d7a2a")

            # Conditionally show or hide the navbar
            if page_name == "LoginPage":
                print("Hiding navbar")
                self.navbar_container.pack_forget()
            else:
                print("Showing navbar")
                self.navbar_container.pack(side="left", fill="y")

        self.show_frame = show_frame

        def destroy_navbar():
            for widget in self.navbar_container.winfo_children():
                widget.destroy()

        self.destroy_navbar = destroy_navbar

        # Function to logout
        def logout():
            self.logged_in_user = None
            self.is_admin = False  # Reset the admin flag
            print("Logging out and hiding navbar")
            self.destroy_navbar()  # Destroy the existing navbar
            self.navbar_container.pack_forget()  # Hide the navbar container
            self.show_frame("LoginPage")
            # Optionally, you can perform other cleanup actions here

        self.logout = logout

        # Create frames for different pages
        for F in (LoginPage, ProfilePage, AboutPage, EventsPage, AccManagePage, EvManagePage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        if self.logged_in_user is None:
            print("No user logged in, showing LoginPage")
            self.show_frame("LoginPage")
        else:
            print(f"User logged in, is_admin: {self.is_admin}")
            self.create_navbar_and_show_initial_frame()
                
    def create_navbar_and_show_initial_frame(self):
        # Clear existing buttons
        self.buttons.clear()

        # Create the navbar based on the user's role
        if self.is_admin:
            print("Admin User logged in, showing Accounts Manager page")
            create_navbar(self.navbar_container, self.show_frame, "AccManagePage", self.buttons, self.logout, is_admin=self.is_admin)
            self.show_frame("AccManagePage")
        else:
            print("User logged in, showing EventsPage")
            create_navbar(self.navbar_container, self.show_frame, "EventsPage", self.buttons, self.logout, is_admin=self.is_admin)
            self.show_frame("EventsPage")


if __name__ == "__main__":
    app = UrbanAidApp()
    app.mainloop()