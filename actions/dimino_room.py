from helper import select_from_choices
from dialogues.jj import jj_dialogue
from dialogue_parser import parse_dialogue
from battles import init_battle
from enemies import JJ

def handle_result(result, user):
  if result == "END1": #fight
    init_battle(user, JJ())
  elif result == "END2": #gravel
    user.inventory["gravel"] += 1

#end1 fight end2 gravel
def handle_action(user):
  choice = select_from_choices(["Speak to JJ"])

  if choice == "Speak to JJ":
    end = parse_dialogue("JJ", jj_dialogue, user)
    handle_result(end, user)
