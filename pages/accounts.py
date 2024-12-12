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
        
        accountFrame = customtkinter.CTkScrollableFrame(self, fg_color="#ffffff")
        accountFrame.pack(fill="both", expand=True)
        
        titleFrame = Frame(accountFrame, bg="#ffffff", borderwidth=5, relief="groove")
        titleFrame.pack(side="top", fill="x")
        Label(titleFrame, text="Accounts Manager", font=("Krub", 25)).pack(side="left", padx=10, pady=10)
        
        managerFrame = Frame(accountFrame, bg="#ffffff", borderwidth=5, relief="groove")
        managerFrame.pack(side="top", fill="both", expand=True)
        
        
        style = ttk.Style()
        style.configure("Treeview", font=("Krub", 10), rowheight=25,)
        style.configure("Treeview.heading", font=("Krub", 11, "bold"))
        
        tableFrame = Frame(managerFrame, bg="#ffffff", borderwidth=5, relief="groove", height=200)
        tableFrame.pack(fill='x',pady=10)
        
        scroller = customtkinter.CTkScrollbar(tableFrame, bg_color="#ffffff")
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
        
        
        
        
        
            
        data_frame = Frame(managerFrame, bg="#ffffff", borderwidth=5, relief="groove")
        data_frame.pack(side="top", fill="both", expand=True)
        
        Label(data_frame, text="User Data", font=("Krub", 12), bg="#ffffff").pack(side="top", anchor="w", padx=10, pady=10)
        
        nameContainer = Frame(data_frame, bg="#ffffff", borderwidth=5, relief="groove")
        nameContainer.pack(side="left", fill="x", expand=True, padx=(10,0))
        
        fnameCont = Frame(nameContainer, bg="#ffffff", borderwidth=5, relief="groove")
        fnameCont.pack(side="top", fill="x", expand=True)
        
        fnamelbl = Label(fnameCont, text="Firstname: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        fnameEntry = Entry(fnameCont, width=30, font=("krub", 9))
        fnameEntry.pack(side="right", anchor="e", expand=True)
        
        lnameCont = Frame(nameContainer, bg="#ffffff", borderwidth=5, relief="groove")  
        lnameCont.pack(side="top", fill="x", expand=True)   
        
        lnamelbl = Label(lnameCont, text="Lastname: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True) 
        lnameEntry = Entry(lnameCont, width=30, font=("krub", 9))
        lnameEntry.pack(side="right", anchor="e", expand=True)  
        
        emailnumContainer = Frame(data_frame, bg="#ffffff", borderwidth=5, relief="groove")
        emailnumContainer.pack(side="left", fill="x", expand=True)
        
        emailCont = Frame(emailnumContainer, bg="#ffffff", borderwidth=5, relief="groove")
        emailCont.pack(side="top", fill="x", expand=True)
        emaillbl = Label(emailCont, text="Email: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        emailEntry = Entry(emailCont, width=30, font=("krub", 9))
        emailEntry.pack(side="right", anchor="e", expand=True)
        
        numCont = Frame(emailnumContainer, bg="#ffffff", borderwidth=5, relief="groove")
        numCont.pack(side="top", fill="x", expand=True)
        numlbl = Label(numCont, text="Contact: ", bg="#ffffff", font=("Krub", 10)).pack(side="left",  anchor="w", expand=True)
        numEntry = Entry(numCont, width=30, font=("krub", 9))
        numEntry.pack(side="right", anchor="e", expand=True)  
            
        passroleContainer = Frame(data_frame, bg="#ffffff", borderwidth=5, relief="groove")
        passroleContainer.pack(side="left", fill="x", expand=True, padx=(0,10))
        
        passCont = Frame(passroleContainer, bg="#ffffff", borderwidth=5, relief="groove")
        passCont.pack(side="top", fill="x", expand=True)
        passlbl = Label(passCont, text="Password: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        passEntry = Entry(passCont, width=30, font=("krub", 9))
        passEntry.pack(side="right", anchor="e", expand=True)
        
        roleCont = Frame(passroleContainer, bg="#ffffff", borderwidth=5, relief="groove")
        roleCont.pack(side="top", fill="x", expand=True)
        rolelbl = Label(roleCont, text="Role: ", bg="#ffffff", font=("Krub", 10)).pack(side="left", anchor="w", expand=True)
        roleEntry = Entry(roleCont, width=30, font=("krub", 9))
        roleEntry.pack(side="right", anchor="e", expand=True)

        records.bind("<<TreeviewSelect>>", lambda event: populate_entries(event, records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))

        action_Frame = Frame(managerFrame, bg="#ffffff", borderwidth=5, relief="groove")
        action_Frame.pack(side="top", fill="x", expand=True)
        
        buttonCont = Frame(action_Frame, bg="#ffffff")
        buttonCont.pack(anchor="center")
        # addBtn = customtkinter.CTkButton(action_Frame, text="Add", width=10, height=1, command=lambda: table_insert_users(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        updateBtn = Button(buttonCont, text="Update Record", width=15, height=1, font=("Krub", 9), border=0, command=lambda: admin_update_user(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        updateBtn.pack(side="left", fill="x", padx=10, pady=10)
        
        addBtn = Button(buttonCont, text="Add Record", width=15, height=1, font=("Krub", 9), border=0, command=lambda: admin_add_user(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        addBtn.pack(side="left", fill="x", padx=10, pady=10)
        
        deleteBtn = Button(buttonCont, text="Delete Record", width=15, height=1, font=("Krub", 9), border=0, command=lambda: admin_delete_user(records, fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        deleteBtn.pack(side="left", fill="x", padx=10, pady=10)
        
        clearBtn = Button(buttonCont, text="Clear Entries", width=15, height=1, font=("Krub", 9), border=0, command=lambda: clear_entries(fnameEntry, lnameEntry, emailEntry, numEntry, passEntry, roleEntry))
        clearBtn.pack(side="left", fill="x", padx=10, pady=10)
        
        