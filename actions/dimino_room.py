from helper import select_from_choices
from dialogues.jj import jj_dialogue
from dialogue_parser import parse_dialogue

def handle_action(user):
  choice = select_from_choices(["Speak to JJ"])

  if choice == "Speak to JJ":
    end = parse_dialogue("JJ", jj_dialogue, user)
