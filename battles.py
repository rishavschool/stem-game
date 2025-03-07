import time
import random
import re
import math
from colors import TerminalColors
from throwables import throwables, throwable_colors
from abilities import ability_colors
from helper import clear_terminal, select_from_choices

battle_text = f"""{TerminalColors.BOLD} _____                                                                _____ 
( ___ )--------------------------------------------------------------( ___ )
 |   |                                                                |   | 
 |   |  ______        _     _________  _________  _____     ________  |   | 
 |   | |_   _ \      / \   |  _   _  ||  _   _  ||_   _|   |_   __  | |   | 
 |   |   | |_) |    / _ \  |_/ | | \_||_/ | | \_|  | |       | |_ \_| |   | 
 |   |   |  __'.   / ___ \     | |        | |      | |   _   |  _| _  |   | 
 |   |  _| |__) |_/ /   \ \_  _| |_      _| |_    _| |__/ | _| |__/ | |   | 
 |   | |_______/|____| |____||_____|    |_____|  |________||________| |   | 
 |___|                                                                |___| 
(_____)--------------------------------------------------------------(_____)
{TerminalColors.RESET}"""

lost_text = f"""{TerminalColors.BOLD}{TerminalColors.RED} ____  ____   ___   _____  _____    _____       ___     ______   _________ 
|_  _||_  _|.'   `.|_   _||_   _|  |_   _|    .'   `. .' ____ \ |  _   _  |
  \ \  / / /  .-.  \ | |    | |      | |     /  .-.  \| (___ \_||_/ | | \_|
   \ \/ /  | |   | | | '    ' |      | |   _ | |   | | _.____`.     | |    
   _|  |_  \  `-'  /  \ \__/ /      _| |__/ |\  `-'  /| \____) |   _| |_   
  |______|  `.___.'    `.__.'      |________| `.___.'  \______.'  |_____|  {TerminalColors.RESET}"""

won_text = f"""{TerminalColors.BOLD}{TerminalColors.BLUE} ____  ____   ___   _____  _____   ____      ____   ___   ____  _____ 
|_  _||_  _|.'   `.|_   _||_   _| |_  _|    |_  _|.'   `.|_   \|_   _|
  \ \  / / /  .-.  \ | |    | |     \ \  /\  / / /  .-.  \ |   \ | |  
   \ \/ /  | |   | | | '    ' |      \ \/  \/ /  | |   | | | |\ \| |  
   _|  |_  \  `-'  /  \ \__/ /        \  /\  /   \  `-'  /_| |_\   |_ 
  |______|  `.___.'    `.__.'          \/  \/     `.___.'|_____|\____|{TerminalColors.RESET}"""

def get_item_damage(item, strength, enemy_charisma):
  charisma_factor = 1 - (enemy_charisma / 100)
  return math.ceil(throwables[item] * (strength / 100 + 1) * charisma_factor)

def get_ability_damage(damage, strength, enemy_charisma):
  charisma_factor = 1 - (enemy_charisma / 100)
  return math.ceil(damage * (strength / 100 + 1) * charisma_factor)

def create_user_name_str(user):
  if type(user).__name__== "Unc":
    return f"YOU: {TerminalColors.BOLD}{TerminalColors.BLUE}{TerminalColors.UNDERLINE}Unc {user.name}{TerminalColors.RESET}"
  else:
    return f"YOU: {TerminalColors.BOLD}{TerminalColors.BLUE}{TerminalColors.UNDERLINE}{user.name} {type(user).__name__}{TerminalColors.RESET}"

def create_enemy_name_str(enemy):
  return f"ENEMY: {TerminalColors.BOLD}{TerminalColors.RED}{TerminalColors.UNDERLINE}{enemy.name}{TerminalColors.RESET}"


def display_stats(user, enemy, user_health, enemy_health):
  print(battle_text)
  print(create_user_name_str(user))
  print(f"{TerminalColors.BOLD}Health:{TerminalColors.RESET} {TerminalColors.BRIGHT_GREEN}{user_health}/{user.max_health}{TerminalColors.RESET}")
  print("")
  print(create_enemy_name_str(enemy))
  print(f"{TerminalColors.BOLD}Health:{TerminalColors.RESET} {TerminalColors.BRIGHT_GREEN}{enemy_health}/{enemy.max_health}{TerminalColors.RESET}")
  print("")



def items_action(user, enemy):
  clear_terminal()
  print("Items:")

  items = []

  for item, quantity in user.inventory.items():
    if quantity > 0 and item in throwables:
      items.append(f"{throwable_colors[item] if throwable_colors.get(item) else TerminalColors.WHITE}{item.title()}{TerminalColors.RESET}: Amount: {quantity} | Damage: {get_item_damage(item, user.strength, enemy.charisma)}")
  items.append("Back")

  choice = select_from_choices(items)

  if choice == "Back" or choice is None:
    return "Back"
  else:
    clean_text = re.sub(r'\033\[[0-9;]*m', '', choice)
    item = re.match(r"^(.*?)(?=:)", clean_text)
    item = item.group(1).strip().lower()

    user.inventory[item] -= 1
    clear_terminal()
    print(f"You used {throwable_colors[item] if throwable_colors.get(item) else TerminalColors.WHITE}{item.title()}{TerminalColors.RESET} and dealt {get_item_damage(item, user.strength, enemy.charisma)} damage!")

    return item

def abilities_action(user, enemy):
  clear_terminal()
  print("Abilities:")
  abilities = []

  for ability in user.abilities.keys():
    abilities.append(f"{ability_colors[ability] if ability_colors.get(ability) else TerminalColors.WHITE}{ability.title()}{TerminalColors.RESET}: Damage: {get_ability_damage(user.abilities[ability], user.strength, enemy.charisma)}")
  abilities.append("Back")

  choice = select_from_choices(abilities)

  if choice == "Back" or choice is None:
    return "Back"
  else:
    clean_text = re.sub(r'\033\[[0-9;]*m', '', choice)
    ability = re.match(r"^(.*?)(?=:)", clean_text)
    ability = ability.group(1).strip().lower()

    clear_terminal()
    print(f"You used {ability_colors[ability] if ability_colors.get(ability) else TerminalColors.WHITE}{ability.title()}{TerminalColors.RESET} and dealt {get_ability_damage(user.abilities[ability], user.strength, enemy.charisma)} damage!")

    return ability

#repeats until a valid action is selected
def action(*args):
  actions = ["Abilities", "Items"]

  print(f"It is currently {TerminalColors.BOLD}YOUR{TerminalColors.RESET} turn:")
  choice = select_from_choices(actions)
  
  return choice

def battle_loop(user, enemy, user_health, enemy_health):
  choice = action(user, enemy, user_health, enemy_health) #abilities or items

  if choice == "Abilities":
    result = abilities_action(user, enemy)

    if result == "Back":
      clear_terminal()
      display_stats(user, enemy, user_health, enemy_health)
      return battle_loop(user, enemy, user_health, enemy_health)
    else:
      enemy_health -= get_ability_damage(user.abilities[result], user.strength, enemy.charisma)

  elif choice == "Items":
    result = items_action(user, enemy)

    if result == "Back": #go back to choice screen
      clear_terminal()
      display_stats(user, enemy, user_health, enemy_health)
      return battle_loop(user, enemy, user_health, enemy_health)
    else:
      enemy_health -= get_item_damage(result, user.strength, enemy.charisma) #deal damage

  else:
    clear_terminal()
    display_stats(user, enemy, user_health, enemy_health)
    return battle_loop(user, enemy, user_health, enemy_health)

  if enemy_health <= 0: #user wins
    clear_terminal()
    print(won_text)
    print("\nRewards:")
    print(f"+{enemy.xp} {TerminalColors.BLUE}XP{TerminalColors.RESET}")
    user.give_xp(enemy.xp)
    print("\nChoices:")
    choice = select_from_choices(["Continue"])
    return 

  #enemy turn
  print("\nChoices:")
  choice = select_from_choices(["Continue"])

  clear_terminal()
  random_ability = random.choice(list(enemy.abilities.keys()))
  print(f"{enemy.name} used {random_ability} and dealt {get_ability_damage(enemy.abilities[random_ability], enemy.strength, user.charisma)} damage!")
  user_health -= get_ability_damage(enemy.abilities[random_ability], enemy.strength, user.charisma)
  time.sleep(2)

  if user_health <= 0: #enemy wins
    clear_terminal()
    print(lost_text)
    print("\nChoices:")
    choice = select_from_choices(["Continue"])
    return

  #continue loop
  clear_terminal()
  display_stats(user, enemy, user_health, enemy_health)
  return battle_loop(user, enemy, user_health, enemy_health)


def init_battle(user, enemy):
  user_health = user.max_health
  enemy_health = enemy.max_health
  clear_terminal()
  display_stats(user, enemy, user_health, enemy_health)
  battle_loop(user, enemy, user_health, enemy_health)