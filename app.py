import customtkinter as ctk
import settings_elements
import settings_model
import sys

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
  def __init__(self) -> None:
    super().__init__()
     
    # configure window
    self.title("Price Calculator")
    self.geometry(f'{400}x{800}')
    self.resizable(width= False, height= False)

    # add a tab control
    self.tabview = ctk.CTkTabview(self, width=self._current_width - 20, height=self._current_height - 20)
    self.tabview.grid(row=0, column=2, padx=(5, 5), pady=(0, 0), sticky="nsew")
    self.tabview.add("Calculate")
    self.tabview.add("Type Config")
    self.tabview.add("Settings")

    self.tabview.tab("Type Config").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
    self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)

    self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("Type Config"), dynamic_resizing=False,
                                                    values=["Value 1", "Value 2", "Value Long Long Long"])
    self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
    self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("Type Config"),
                                                values=["Value 1", "Value 2", "Value Long....."])
    self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
    
    s = settings_model.Settings()
    self.settings_frame = settings_elements.SettingsFrame(self.tabview.tab('Settings'), s)
    self.settings_frame.pack()






if __name__ == "__main__":
    # redirect stdout to file for logs
    sys.stdout = open('C:\\ProgramData\\price_calc.log', 'a')

    # start app
    app = App()
    app.mainloop()
