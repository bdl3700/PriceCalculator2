from typing import Union, Tuple, List, Optional
import customtkinter as ctk
import tkinter.messagebox
import copy
from os.path import isdir

from settings_model import Settings, SharedSettings

class SettingsFrame(ctk.CTkFrame):
  def __init__(self, master: any, settings: Settings, width: int = 200, height: int = 200, corner_radius: Optional[Union[int, str]] = None, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = None, border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
    super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
    self.settings = settings
    self.old_settings = copy.deepcopy(settings)

    self.settings_label = ctk.CTkLabel(self, width=380, height=60, text='Settings', font=ctk.CTkFont(size=48, underline=True))
    self.settings_label.grid(row=0, column=1, columnspan=3, pady=(0, 5))

    self.shared_path_label = ctk.CTkLabel(self, text='Shared Settings Path:', height=28)
    self.shared_path_label.grid(row=1, column=1, padx=(0,0), pady=(0,0), sticky='nsew')

    path_vcmd = self.register(self.shared_path_validate)
    self.shared_path_entry = ctk.CTkEntry(self, width=140, height=24, placeholder_text='Path to shared settings', validate='focusout', validatecommand=(path_vcmd))
    self.shared_path_entry.grid(row=1, column=2, padx=(10, 0), pady=(0, 0), sticky="nsew")
    self.shared_path_entry._entry_focus_out(lambda : print(self.shared_path_entry.get()))

    # print(settings.shared_path, '<-- is the path to shared settings')
    # print('Tax Rate: ', settings.shared_settings.tax_rate)

    self.shared_settings_label = ctk.CTkLabel(self, width=380, height=60, text='Shared Settings', font=ctk.CTkFont(size=36, underline=True))
    self.shared_settings_label.grid(row=2, column=1, columnspan=3, pady=(10,0), sticky='nsew')

    self.tax_rate_label = ctk.CTkLabel(self, text='Tax Rate:', height=28)
    self.tax_rate_label.grid(row=3, column=1, padx=(0, 0), pady=(0, 0), sticky='nsew')

    tax_vcmd = self.register(self.tax_rate_validate)
    self.tax_rate_entry = ctk.CTkEntry(self, width=140, height=24, placeholder_text='0.00%', validate="focusout", validatecommand=(tax_vcmd, '%P'))
    self.tax_rate_entry.grid(row=3, column=2, padx=(10, 0), pady=(0, 0), sticky="nsew")
    
    self.save_button = ctk.CTkButton(self, width=140, height=28, text='Save', command=self.save_settings)
    self.save_button.grid(row=4, column=1, columnspan=3, padx=(10, 10), pady=(10, 10), sticky='nsew')


    # bring in previously stored values
    self.tax_rate_entry.insert(0, str(round(settings.shared_settings.tax_rate, 4)))
    self.shared_path_entry.insert(0, settings.shared_path)

  def tax_rate_validate(self, P):
    val = self.tax_rate_entry.get()
    if val.replace('.', '').isnumeric() and val.count('.') <= 1 and float(val) >= 0:
      self.settings.shared_settings.tax_rate = float(val)  #TODO: make the user authenticate before shared settings are saved
      print(f'The tax rate: {val}% will be calculated by multiplying inputs by {self.settings.shared_settings.tax_rate}')
      return True
    if val == '':
      return True
    
    tkinter.messagebox.showwarning('Invalid Tax Rate', f'The input tax rate ({val}) is not valid.\r\nPlease represent the tax rate as a positive percentage.\r\nEX: input 7.25 when tax is calculated by multiplying a retail price by 1.0725.')
    self.tax_rate_entry.focus()
    self.tax_rate_entry.select_range(0, len(self.tax_rate_entry.get()))
    print(val)
    return False

  def shared_path_validate(self):
    v = isdir(self.shared_path_entry.get())
    print(f'{self.shared_path_entry.get()} is a valid folder: {v}')
    if v:
      self.settings.shared_path = self.shared_path_entry.get()  #TODO: make this conditional on authentication
    return v
  
  def save_settings(self):
    self.save_button.focus()
    print('Save button pressed')
    self.settings.save()


if __name__ == "__main__":
  ctk.set_appearance_mode('dark')
  ctk.set_default_color_theme('blue')

  root = ctk.CTk()
  root.title('Settings Testing')
  root.geometry(f'{380}x{780}')
  root.resizable(width=False, height=False)

  s = Settings()
  sf = SettingsFrame(master=root, settings=s)
  sf.pack()

  root.mainloop()
