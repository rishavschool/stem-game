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