import math
import random
from helper import random_between
from colors import TerminalColors

class Enemy():
  def __init__(self):
    self.name = "Enemy"
    self.max_health = 0
    self.strength = 0
    self.charisma = 0
    self.xp = 0
    self.money = 0
    self.abilities = {
      "Default": 10
    }
    self.drops = {

    }
  
  def _weighted_random_drop(self):
    total_weight = sum(self.drops.values())
    to_add = 100 - total_weight

    if total_weight == 0:
      return None

    rand_choice = random.randint(1, 100)

    if rand_choice > total_weight:
      return None

    cumulative_weight = 0
    for item, weight in self.drops.items():
      cumulative_weight += weight
      if rand_choice <= cumulative_weight:
        return item

    return None

  def get_drops(self):
    if len(self.drops) == 0:
      return []
    
    drop_amount = random_between(1, 3)
    drop_results = []

    for _ in range(drop_amount):
      drop = self._weighted_random_drop()
      if drop:
        drop_results.append(drop)

    return drop_results
        
  

class Unc(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Unc"
    self.max_health = 200
    self.strength = 50
    self.charisma = 10
    self.xp = 100
    self.abilities = {
      f"{TerminalColors.RED}Diablo{TerminalColors.RESET}": 15,
      f"{TerminalColors.PINK}Liver Shot{TerminalColors.RESET}": 25
    }
    self.drops = {
      "diablo sauce": 20
    }

class Freddy(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Sir Frederick Digby"
    self.max_health = 100
    self.strength = 25
    self.charisma = 50
    self.xp = 50
    self.money = 10
    self.abilities = {
      f"{TerminalColors.BRIGHT_YELLOW}5th Symphony{TerminalColors.RESET}": 7,
      f"{TerminalColors.BRIGHT_WHITE}Abraham{TerminalColors.RESET}": 10,
      f"{TerminalColors.RED}Revolution{TerminalColors.RESET}": 12,
    }
    self.drops = {
      "monacle": 10,
      "ruff": 5,
    }

class Rishi(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rishi"
    self.max_health = 50
    self.strength = 25
    self.charisma = 0
    self.xp = 25
    self.abilities = {
      f"{TerminalColors.BROWN}Stench{TerminalColors.RESET}": 5,
      f"{TerminalColors.YELLOW}Rotten Banana{TerminalColors.RESET}": 7,
      f"{TerminalColors.CYAN}Versace Eros{TerminalColors.RESET}": 10
    }
    self.drops = {
      "scum spray": 50
    }

class JJ(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "JJ"
    self.max_health = 100
    self.strength = 10
    self.charisma = 25
    self.xp = 50
    self.money = 5
    self.abilities = {
      f"{TerminalColors.LIGHT_GRAY}Gravel{TerminalColors.RESET}": 10,
      f"{TerminalColors.TEAL}Espanol{TerminalColors.RESET}": 12,
    }
    self.drops = {
      "gravel": 100
    }

class TPod(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "TPod"
    self.max_health = 300
    self.strength = 0
    self.charisma = 0
    self.xp = 200
    self.money = 20
    self.abilities = {
      f"{TerminalColors.LIGHT_BLUE}No Mezz{TerminalColors.RESET}": 15,
      f"{TerminalColors.RED}DelCo{TerminalColors.RESET}": 20,
      f"{TerminalColors.BRIGHT_YELLOW}MEA{TerminalColors.RESET}": 25,
      f"{TerminalColors.PINK}Smiley{TerminalColors.RESET}": 45
    }

class Hari(Enemy):
  def __init__(self):
    self.name = "Hari"
    self.max_health = 200
    self.strength = 20
    self.charisma = 30
    self.xp = 150
    self.money = -5
    self.abilities = {
      f"{TerminalColors.RED}RAGE{TerminalColors.RESET}": 20,
      f"{TerminalColors.CYAN}Seep{TerminalColors.RESET}": 15,
      f"{TerminalColors.YELLOW}Glaze{TerminalColors.RESET}": 12,
      f"{TerminalColors.GREEN}Yo can I have some money{TerminalColors.RESET}": 15,
      f"{TerminalColors.MAGENTA}Polyester whip{TerminalColors.RESET}": 10
    }
    self.drops = {
      "polyester scraps": 35,
    }