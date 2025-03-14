from helper import select_from_choices
from dialogues.hari import hari_dialogue
from dialogue_parser import parse_dialogue
from enemies import Hari
from battles import init_battle

def handle_result(result, user):
  if result == "END1": #nothing
    return
  elif result == "END2": #give hari 5 dollars
    user.money -= 5
    user.inventory["polyester scraps"] += 1
  elif result == "END3": #fight
    init_battle(user, Hari())


def handle_action(user):
  choice = select_from_choices(["Speak to Hari"])
  
  if choice == "Speak to Hari":
    end = parse_dialogue("Hari", hari_dialogue, user)
    handle_result(end, user)
    