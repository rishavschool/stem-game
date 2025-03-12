import math
from colors import TerminalColors

class Enemy():
  def __init__(self):
    self.name = "Enemy"
    self.max_health = 0
    self.strength = 0
    self.charisma = 0
    self.xp = 0
    self.abilities = {
      "Default": 10
    }


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

class Freddy(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Sir Frederick Digby"
    self.max_health = 100
    self.strength = 25
    self.charisma = 50
    self.xp = 50
    self.abilities = {
      f"{TerminalColors.BRIGHT_YELLOW}5th Symphony{TerminalColors.RESET}": 7,
      f"{TerminalColors.BRIGHT_WHITE}Abraham{TerminalColors.RESET}": 10,
      f"{TerminalColors.RED}Revolution{TerminalColors.RESET}": 12,
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