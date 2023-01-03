import customtkinter as ctk

root = ctk.CTk()
lbllst = dict()
rmbtnlst = dict()
id = 0

def add_label():
  global id
  i = id
  print(f'adding account with id: {id}')
  id += 1
  account = ctk.CTkLabel(account_frame, text="Account Nr"+str(id), font=ctk.CTkFont('Helvetica', 34))
  account.grid(column=0, row= id)
  lbllst[i] = account
  
  rem_button = ctk.CTkButton(account_frame, text='X', width=20, command=lambda: remove_account(i))
  rem_button.grid(column=1, row = id)
  rmbtnlst[i] = rem_button

def remove_account(i: int):
  print(f'attempting to remove account {i}')
  lbllst.pop(i).destroy()
  rmbtnlst.pop(i).destroy()

#Account_Frame
account_frame = ctk.CTkFrame(root, width=300, height=700)
account_frame.pack(side='right')
add_account_button = ctk.CTkButton(account_frame, text="Add Account", command=add_label)
add_account_button.grid(row=0, columnspan=2)

root.mainloop()
