from helper import select_from_choices, chance, clear_terminal
from colors import TerminalColors
from battles import init_battle
from enemies import TPod


def handle_action(user):
  choice_to_item = {"Steal mayo": "mayo", "Steal sugar": "sugar", "Steal sweetener": "sweetener"}
  choice = select_from_choices(["Steal mayo", "Steal sugar", "Steal sweetener"])

  if not choice in choice_to_item:
    return

  item = choice_to_item[choice]
  if item:
    user.inventory[item] += 1

    if chance(10):
      clear_terminal()
      print(f"{TerminalColors.RED}TPod{TerminalColors.RESET} caught you stealing!")
      print("\nChoices:")
      choice = select_from_choices(["Continue"])

      init_battle(user, TPod())