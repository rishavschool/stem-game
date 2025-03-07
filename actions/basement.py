from helper import select_from_choices
from dialogue_parser import parse_dialogue
from dialogues.rishi import rishi_dialogue

def handle_result(result, user):
  if result == "END1":
    pass

def handle_action(user):
  choice = select_from_choices(["Speak to Rishi"])
  
  if choice == "Speak to Rishi":
    end = parse_dialogue("Rishi", rishi_dialogue, user)
    handle_result(end, user)
