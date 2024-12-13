# FILE: navbar.py

from tkinter import Frame, Button

def create_navbar(parent, show_frame, active_page, buttons, logout, is_admin = False):
    print("Creating navbar")
    # Create a frame for the navigation bar with increased width
    navbar = Frame(parent, width=270, bg="#333333", height=600, relief="raised", borderwidth=2)
    navbar.pack_propagate(False)
    navbar.pack(side="left", fill="y")

    nav_items = Frame(navbar, bg="#333333")
    nav_items.pack(expand=True, fill="x")

    # Function to create a navigation button
    def create_nav_button(text, page_name):
        bg_color = "#555555" if active_page == page_name else "#333333"
        button = Button(nav_items, text=text, font=("Krub", 12), bg=bg_color, fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=lambda: show_frame(page_name))
        button.pack(fill="x", pady=10)
        buttons[page_name] = button


    if is_admin:
        create_nav_button("Accounts Manager", "AccManagePage")
        create_nav_button("Event Manager", "EvManagePage")
    else:  
        # Add buttons to the navigation bar
        create_nav_button("Events", "EventsPage")
        create_nav_button("About Us", "AboutPage")
        create_nav_button("Profile", "ProfilePage")

    # Add the logout button at the bottom
    logout_button = Button(navbar, text="Logout", font=("Krub", 12), bg="#333333", fg="#ffffff", activebackground="#555555", activeforeground="#ffffff", border=0, command=logout)
    logout_button.pack(side="bottom", fill="x", pady=10)