import math
import os
from item_stats import item_stats
from throwables import throwables
from colors import TerminalColors


class Family():
  def __init__(self, name):
    self.name = name
    self.family = "Family"
    self.level = 1
    self.xp = 0
    self.wisdom: int = 0
    self.strength: int = 0
    self.charisma: int = 0
    self.max_health: int = 100
    self.money: int = 0
    self.age: int = 0
    self.score = 0
    self.defects = []
    self.buffs = []
    self.abilities = {
      f"punch": 10
    }
  
  @staticmethod
  def init_inventory(self):
    self.inventory = {
      "mayo": 0,
      "sugar": 0,
      "sweetener": 0,
      "chips": 0,
      "soda": 0,
      "polyester scraps": 0,
      "youngla jeans": 0,
      "monacle": 0,
      "ruff": 0,
      "sigma shirt": 0,
      "tight ahh joggers": 0,
      "gravel": 0,
      "scum spray": 0,
      "diablo sauce": 20,
    }
    self.equipped = {
      "shoes": "none",
      "pants": "none",
      "shirt": "none",
      "hat": "none"
    }

  def create_inventory_str(self):
    inventory_str = f"{TerminalColors.BOLD}{TerminalColors.BROWN}Inventory:{TerminalColors.RESET} [\n"
    stat_to_color = {
      "charisma": f"{TerminalColors.YELLOW}charisma{TerminalColors.RESET}",
      "wisdom": f"{TerminalColors.PURPLE}wisdom{TerminalColors.RESET}",
      "strength": f"{TerminalColors.RED}strength{TerminalColors.RESET}"
    }

    for item, quantity in self.inventory.items():
      if quantity > 0:
        inventory_str += f"    {item.capitalize()}: "

        if item in item_stats.keys():
          stat = item_stats[item][1]
          inventory_str += f"({TerminalColors.BOLD}Amount:{TerminalColors.RESET} {quantity}) | ({TerminalColors.BOLD}Stat:{TerminalColors.RESET} +{item_stats[item][0]} {stat_to_color[stat]}),\n"
        elif item in throwables.keys():
          stat = throwables[item]
          inventory_str += f"({TerminalColors.BOLD}Amount:{TerminalColors.RESET} {quantity}) | ({TerminalColors.BOLD}Damage:{TerminalColors.RESET} {TerminalColors.RED}{stat}{TerminalColors.RESET}),\n"
        else:
          inventory_str += f"({TerminalColors.BOLD}Amount:{TerminalColors.RESET} {quantity}),\n"

    inventory_str = inventory_str.rstrip(',\n') + "\n"

    return inventory_str

  def give_xp(self, amount):
    self.xp += amount
    
    while self.xp >= self.get_xp_for_level():
      self.xp -= self.get_xp_for_level()
      self.level += 1
      self.max_health = math.floor(100 * ((self.level / 5) + 1))

  def get_xp_for_level(self):
    return 2 * self.level ** 2 + 50 * self.level + 48

  def __create_xp_str(self):
    max_xp = self.get_xp_for_level()
    current_xp = self.xp
    
    progress = current_xp / max_xp
    bar_length = 40
    
    filled_length = int(bar_length * progress)
    
    bar = f"{TerminalColors.BLUE}{TerminalColors.BOLD}" + '#' * filled_length + f"{TerminalColors.RESET}" + '-' * (bar_length - filled_length)
    xp_str = f"[{bar}] {current_xp}/{max_xp} XP ({int(progress * 100)}%)"
    
    return xp_str

  def __create_name_str(self):
    if type(self).__name__== "Unc":
      return f"Unc {self.name}"
    else:
      return f"{self.name} {type(self).__name__}"

  def __repr__(self):
    return f"""
{TerminalColors.BOLD}Name:{TerminalColors.RESET} {self.__create_name_str()}

{TerminalColors.BOLD}Level:{TerminalColors.RESET} {self.level}
{TerminalColors.BOLD}Experience:{TerminalColors.RESET} {self.__create_xp_str()}

{TerminalColors.BOLD}Age:{TerminalColors.RESET} {self.age} years old

{TerminalColors.BOLD}Buffs:{TerminalColors.RESET} {", ".join(self.buffs)}
{TerminalColors.BOLD}Defects:{TerminalColors.RESET} {", ".join(self.defects)}

{TerminalColors.BOLD}{TerminalColors.BRIGHT_GREEN}Health:{TerminalColors.RESET} {self.max_health}
{TerminalColors.BOLD}{TerminalColors.PURPLE}Wisdom:{TerminalColors.RESET} {self.wisdom}
{TerminalColors.BOLD}{TerminalColors.RED}Strength:{TerminalColors.RESET} {self.strength}
{TerminalColors.BOLD}{TerminalColors.YELLOW}Charisma:{TerminalColors.RESET} {self.charisma}

{TerminalColors.BOLD}Money:{TerminalColors.RESET} {TerminalColors.GREEN}${self.money}{TerminalColors.RESET}

{TerminalColors.BOLD}{TerminalColors.BROWN}Equipped:{TerminalColors.RESET} [
  {TerminalColors.BOLD}Hat:{TerminalColors.RESET} {self.equipped["hat"].capitalize()},
  {TerminalColors.BOLD}Shirt:{TerminalColors.RESET} {self.equipped["shirt"].capitalize()},
  {TerminalColors.BOLD}Pants:{TerminalColors.RESET} {self.equipped["pants"].capitalize()},
  {TerminalColors.BOLD}Shoes:{TerminalColors.RESET} {self.equipped["shoes"].capitalize()}
]

{self.create_inventory_str()}]"""


class Ravikanth(Family):
  def __init__(self, name):
    super().__init__(name)
    self.family = "Ravikanth"
    self.age: int = 16
    self.defects = ["Scoliosis"]
    self.buffs = ["None"]
    self.abilities.update({"serve": 20})
    super().init_inventory(self)

class Unc(Family):
  def __init__(self, name):
    super().__init__(name)
    self.family = "Unc"
    self.age: int = math.inf
    self.defects = ["Dementia"]
    self.buffs = ["Karate"]
    self.abilities.update({"kick": 30})
    super().init_inventory(self)

class Potdar(Family):
  def __init__(self, name):
    super().__init__(name)
    self.family = "Potdar"
    self.age: int = 15
    self.defects = ["Hair"]
    self.buffs = ["Badminton"]
    self.abilities.update({"mangesh": 20})
    super().init_inventory(self)