import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from tkinter import ttk
import customtkinter
from pages.modules.functions import table_insert_users, populate_entries, admin_add_user, admin_update_user, clear_entries, admin_delete_user

class AccManagePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.controller = controller
        self.logged_in_user = self.controller.logged_in_user
        
        accountFrame = Frame(self, bg="#ffffff")
        accountFrame.pack(fill="both", expand=True)
        
        titleFrame = Frame(accountFrame, bg="#ffffff")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Accounts Manager", font=("Krub", 25), bg="#ffffff").pack(side="left", padx=10, pady=10)
        
        managerFrame = Frame(accountFrame, bg="#ffffff")
        managerFrame.pack(side="top", fill="both", expand=True, padx=10)
        
        
        style = ttk.Style()
        style.configure("Treeview", font=("Krub", 10), rowheight=25,)
        style.configure("Treeview.heading", font=("Krub", 11, "bold"))
        
        tableFrame = Frame(managerFrame, bg="#ffffff", borderwidth=5, relief="groove", height=200)
        tableFrame.pack(fill='x',pady=10)
        
        scroller = customtkinter.CTkScrollbar(tableFrame, bg_color="#ffffff", button_color="#8d9e36", button_hover_color="#6d7a2a")
        scroller.pack(side="right", fill="y")
        
        records = ttk.Treeview(tableFrame, yscrollcommand=scroller.set, selectmode="extended")
        records.pack(fill="x")
        
        scroller.configure(command=records.yview)
        
        records['columns'] = ("ID", "Firstname", "Lastname", "Contact", "Email", "Password", "Role")
        records.column("#0", width=0, stretch="no")
        records.column("ID", anchor="center", width=5)
        records.column("Firstname", anchor="center", width=20)
        records.column("Lastname", anchor="center", width=20)
        records.column("Contact", anchor="center", width=15)
        records.column("Email", anchor="center", width=25)
        records.column("Password", anchor="center", width=25)
        records.column("Role", anchor="center", width=10)
        
        records.heading("#0", text="", anchor="w")
        records.heading("ID", text="ID", anchor="center")
        records.heading("Firstname", text="Firstname", anchor="center")
        records.heading("Lastname", text="Lastname", anchor="center")
        records.heading("Contact", text="Contact", anchor="center")
        records.heading("Email", text="Email", anchor="center")
        records.heading("Password", text="Password", anchor="center")
        records.heading("Role", text="Role", anchor="center")

        # Fetch and insert user data
        table_insert_users(records)
        
        data_frame = Frame(managerFrame, bg="#ffffff")
        data_frame.pack(side="top", fill="both", expand=True, pady=(0, 10))
        
        Label(data_frame, text="User Data", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w", padx=10, pady=10)
        
        nameContainer = Frame(data_frame, bg="#ffffff")
        nameContainer.pack(side="left", fill="x", expand=True, padx=(20,0))
        
        fnameCont = Frame(nameContainer, bg="#ffffff")
        fnameCont.pack(side="top", fill="x", expand=True)
        
        fnamelbl = Label(fnameCont, text="Firstname: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        fnameEntry = customtkinter.CTkEntry(fnameCont, width=200, font=("krub",13), text_color="#000000", fg_color="#ffffff", bg_color="#ffffff", border_width=1)
        fnameEntry.pack(side="right", anchor="e", expand=True)
        
        lnameCont = Frame(nameContainer, bg="#ffffff")  
        lnameCont.pack(side="top", fill="x", expand=True)   
        
        lnamelbl = Label(lnameCont, text="Lastname: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True, pady=(5,0)) 
        lnameEntry = customtkinter.CTkEntry(lnameCont, width=200, font=("krub",13), text_color="#000000", fg_color="#ffffff", bg_color="#ffffff", border_width=1)
        lnameEntry.pack(side="right", anchor="e", expand=True, pady=(5,0))  
        
        emailnumContainer = Frame(data_frame, bg="#ffffff")
        emailnumContainer.pack(side="left", fill="x", expand=True, padx=20)
        
        emailCont = Frame(emailnumContainer, bg="#ffffff")
        emailCont.pack(side="top", fill="x", expand=True)
        emaillbl = Label(emailCont, text="Email: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        emailEntry = customtkinter.CTkEntry(emailCont, width=200, font=("krub",13), text_color="#000000", fg_color="#ffffff", bg_color="#ffffff", border_width=1)
        emailEntry.pack(side="right", anchor="e", expand=True)
        
        numCont = Frame(emailnumContainer, bg="#ffffff")
        numCont.pack(side="top", fill="x", expand=True)
        numlbl = Label(numCont, text="Contact: ", bg="#ffffff", font=("Krub", 10)).pack(side="left",  anchor="w", expand=True, pady=(5,0))
        numEntry = customtkinter.CTkEntry(numCont, width=200, font=("krub",13), text_color="#000000", fg_color="#ffffff", bg_color="#ffffff", border_width=1)
        numEntry.pack(side="right", anchor="e", expand=True, pady=(5,0))  
            
        passroleContainer = Frame(data_frame, bg="#ffffff")
        passroleContainer.pack(side="left", fill="x", expand=True, padx=(0,20))
        
        passCont = Frame(passroleContainer, bg="#ffffff")
        passCont.pack(side="top", fill="x", expand=True)
        passlbl = Label(passCont, text="Password: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        passEntry = customtkinter.CTkEntry(passCont, width=200, font=("krub",13), text_color="#000000", fg_color="#ffffff", bg_color="#ffffff", border_width=1)
        passEntry.pack(side="right", anchor="e", expand=True)
        
        roleCont = Frame(passroleContainer, bg="#ffffff")
        roleCont.pack(side="top", fill="x", expand=True)
        rolelbl = Label(roleCont, text="Role: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True, pady=(5,0))
        roleEntry = customtkinter.CTkEntry(roleCont, width=200, font=("krub",13), text_color="#000000", fg_color="#ffffff", bg_color="#ffffff", border_width=1)
        roleEntry.pack(side="right", anchor="e", expand=True, pady=(5,0))

        records.bind("<<TreeviewSelect>>", lambda event: populate_entries(event, records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))

        action_Frame = Frame(managerFrame, bg="#ffffff")
        action_Frame.pack(side="top", fill="x", expand=True)
        
        buttonCont = Frame(action_Frame, bg="#ffffff")
        buttonCont.pack(anchor="center")
        # addBtn = customtkinter.CTkButton(action_Frame, text="Add", width=10, height=1, command=lambda: table_insert_users(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        updateBtn = Button(buttonCont, text="Update Record", width=15, height=1, font=("Krub", 9), border=0, command=lambda: admin_update_user(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        updateBtn.pack(side="left", fill="x", padx=10, pady=(0,30))
        
        addBtn = Button(buttonCont, text="Add Record", width=15, height=1, font=("Krub", 9), border=0, command=lambda: admin_add_user(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        addBtn.pack(side="left", fill="x", padx=10, pady=(0,30))
        
        deleteBtn = Button(buttonCont, text="Delete Record", width=15, height=1, font=("Krub", 9), border=0, command=lambda: admin_delete_user(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        deleteBtn.pack(side="left", fill="x", padx=10, pady=(0,30))
        
        clearBtn = Button(buttonCont, text="Clear Entries", width=15, height=1, font=("Krub", 9), border=0, command=lambda: clear_entries(fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        clearBtn.pack(side="left", fill="x", padx=10, pady=(0,30))
        
        