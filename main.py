import tkinter as tk
from tkinter import Frame
from pages.modules.navbar import create_navbar
from pages.events import EventsPage
from pages.about import AboutPage
from pages.profile import ProfilePage

root = tk.Tk()
root.title("UrbanAid")
root.geometry("1080x600")
root.configure(bg="#ffffff")


# Create a container for the frames
container = Frame(root, height=1080)
container.pack(side="right", fill="both", expand=True)

# Dictionary to hold the frames
frames = {}

# Dictionary to hold the navigation buttons
buttons = {}

# Function to show a frame for the given page name
def show_frame(page_name):
    frame = frames[page_name]
    frame.tkraise()
    # Update the navbar to highlight the active page
    for btn_page, button in buttons.items():
        if btn_page == page_name:
            button.config(bg="#555555")
        else:
            button.config(bg="#333333")

# Function to logout
def logout():
    root.destroy()
    # Optionally, you can redirect to a login screen or perform other cleanup actions here

# Create the navigation bar
create_navbar(root, show_frame, "EventsPage", buttons)

# Create frames for different pages
for F in (ProfilePage, AboutPage, EventsPage):
    page_name = F.__name__
    frame = F(parent=container, controller=root)
    frames[page_name] = frame
    frame.grid(row=0, column=0, sticky="nsew")

# Show the initial frame
show_frame("EventsPage")

root.mainloop()