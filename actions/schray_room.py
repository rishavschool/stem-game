import time
from battles import init_battle
from enemies import Freddy
from helper import select_from_choices, clear_terminal
from dialogues.freddy import freddy_dialogue, freddy_happy_dialogue, freddy_mad_dialogue
from dialogue_parser import parse_dialogue
from colors import TerminalColors

def handle_result(result, user):
  if result == "END1": #he is disrespected because you said you dont understand him (old money fight maybe)
    init_battle(user, Freddy())
  elif result == "END2": #you open the digby store
    time.sleep(0.5)
    clear_terminal()
    choice = select_from_choices([f"{TerminalColors.GREEN}$20{TerminalColors.RESET} Monacle", f"{TerminalColors.GREEN}$50{TerminalColors.RESET} Ruff", "Leave"])
    
    if choice == f"{TerminalColors.GREEN}$20{TerminalColors.RESET} Monacle":
      if user.money >= 20:
        user.money -= 20
        user.inventory["monacle"] += 1
        parse_dialogue("Sir Frederick", freddy_happy_dialogue, user)

    elif choice == f"{TerminalColors.GREEN}$50{TerminalColors.RESET} Ruff":
      if user.money >= 50:
        user.money -= 50
        user.inventory["ruff"] += 1
        parse_dialogue("Sir Frederick", freddy_happy_dialogue, user)

    else:
      parse_dialogue("Sir Frederick", freddy_mad_dialogue, user)


def handle_action(user):
  choice = select_from_choices(["Speak to Sir Frederick Digby"])

  if choice == "Speak to Sir Frederick Digby":
    end = parse_dialogue("Sir Frederick", freddy_dialogue, user)
    handle_result(end, user)