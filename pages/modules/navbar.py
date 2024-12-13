from tkinter import Frame, Button

def create_navbar(parent, show_frame, active_page, buttons, logout, is_admin = False):
    print("Creating navbar")
    # Create a frame for the navigation bar with increased width
    navbar = Frame(parent, width=270, bg="#6d7a2a", height=600, relief="flat", borderwidth=1)
    navbar.pack_propagate(False)
    navbar.pack(side="left", fill="y")

    nav_items = Frame(navbar, bg="#6d7a2a")
    nav_items.pack(expand=True, fill="x")

    # Function to create a navigation button
    def create_nav_button(text, page_name):
        bg_color = "#8d9e36" if active_page == page_name else "#6d7a2a"
        button = Button(nav_items, text=text, font=("Krub", 12), bg=bg_color, fg="#ffffff", activebackground="#8d9e36", activeforeground="#ffffff", border=0, command=lambda: show_frame(page_name))
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
    logout_button = Button(navbar, text="Logout", font=("Krub", 12), bg="#6d7a2a", fg="#ffffff", activebackground="#8d9e36", activeforeground="#ffffff", border=0, command=logout)
    logout_button.pack(side="bottom", fill="x", pady=10)