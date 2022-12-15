import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
  def __init__(self) -> None:
    super().__init__()
     
    # configure window
    self.title("Price Calculator")
    self.geometry(f'{400}x{800}')

    # add a tab control
    self.tabview = ctk.CTkTabview(self, width=self._current_width - 20, height=self._current_height - 20)
    self.tabview.grid(row=0, column=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
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
    self.label_tab_2 = ctk.CTkLabel(self.tabview.tab("Settings"), text="CTkLabel on Tab 2")
    self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)






if __name__ == "__main__":
    app = App()
    app.mainloop()
