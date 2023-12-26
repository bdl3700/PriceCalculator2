import json
from os.path import exists
import jsonpickle

from rounder import Rounder
from item_type import ItemType


class Settings():

  local_settings_path = 'c:\\ProgramData\\price_calculator2_localsettings'
  shared_settings_file_name = 'price_calc_shared_settings.json'
  type_file_name = 'price_calc_types.json'

  def __init__(self, _shared_path = 'c:\\ProgramData\\') -> None:
    self.shared_path = _shared_path

    if exists(Settings.local_settings_path):
      with open(Settings.local_settings_path) as file:
        self.shared_path = file.readline()
    
    self.shared_settings = None
    if exists(self.shared_path + self.shared_settings_file_name):
      with open(self.shared_path + self.shared_settings_file_name) as file:
        json_string = file.read()
        self.shared_settings = jsonpickle.decode(json_string)
    else:
      self.shared_settings = SharedSettings(7.25, [ItemType('item1', .73, 1.1)], Rounder(), "411")

    pass

  def save(self):
    with open(self.shared_path + self.shared_settings_file_name, 'w') as file:
      json_string = jsonpickle.encode(self.shared_settings)
      file.write(json_string)
    with open(Settings.local_settings_path, 'w') as file:
      file.write(self.shared_path)

class SharedSettings():
  def __init__(self, _tax_rate: float, _types: list[ItemType], _rounder: Rounder, _passcode: str) -> None:
    self.tax_rate = _tax_rate
    self.types = _types
    self.rounder = _rounder
    self.passcode = _passcode
    pass


if __name__ == '__main__':
  s = Settings()
  # print(jsonpickle.encode(s))
  s.save()

  f = Settings()
  assert jsonpickle.encode(f) == jsonpickle.encode(s)

  print('PASSED: loaded settings are the same as saved settings')
