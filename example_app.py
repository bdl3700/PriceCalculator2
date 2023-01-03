import customtkinter as ctk

root = ctk.CTk()
lbllst = dict()
rmbtnlst = dict()
id = 0

def addlabel():
    global id
    i = id
    print(f'adding account with id: {id}')
    id += 1
    account = ctk.CTkLabel(account_frame, text="Account Nr"+str(len(lbllst)+1), font=ctk.CTkFont('Helvetica', 34))
    account.place(relx=0.01, rely=0.125*(len(lbllst)+1))
    lbllst[i] = account
    

    rem_button = ctk.CTkButton(account_frame, text='X', width=20, command=lambda: remove_account(i))
    rem_button.place(relx=.75, rely=0.125*(len(lbllst)+.1))
    rmbtnlst[i] = rem_button

def remove_account(i: int):
    print(f'attempting to remove account {i}')
    lbllst.pop(i).destroy()
    rmbtnlst.pop(i).destroy()
    for key in lbllst.keys():
        lbllst[key]
    pass

#Account_Frame
account_frame = ctk.CTkFrame(root, width=300, height=700)
account_frame.pack(side='right')
add_account_button = ctk.CTkButton(account_frame, text="Add Account", command=addlabel)
add_account_button.place(relx=0.26, rely=0.03)

root.mainloop()
