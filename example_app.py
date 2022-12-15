import customtkinter as ctk

root = ctk.CTk()
lbllst = []

def addlabel():
    account = ctk.CTkLabel(account_frame, text="Account Nr"+str(len(lbllst)+1), font=ctk.CTkFont('Helvetica', 34))
    account.place(relx=0.01, rely=0.125*(len(lbllst)+1))
    lbllst.append(account)

#Account_Frame
account_frame = ctk.CTkFrame(root, width=300, height=700)
account_frame.pack(side='right')
add_account_button = ctk.CTkButton(account_frame, text="Add Account", command=addlabel)
add_account_button.place(relx=0.26, rely=0.03)

root.mainloop()
