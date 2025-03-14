from helper import select_from_choices
from dialogue_parser import parse_dialogue
from battles import init_battle
from dialogues.agava import agava_dialogue

def handle_result(result, user):
  if result == "END1": 
    pass
  elif result == "END2":
    pass

def handle_action(user):
  choice = select_from_choices(["Speak to Agava"])

  if choice == "Speak to Agava":
    end = parse_dialogue("Agava", agava_dialogue, user)
    handle_result(end, user)
