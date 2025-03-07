from colors import TerminalColors

rishi_dialogue = {
  "dialogue": f"Want to smell {TerminalColors.GREEN}good{TerminalColors.RESET} like me?",
  "responses": {
    "You stink Rishi.": {
      "dialogue": "I don't kid.",
      "responses": "END2"
    },
    "Yes, great smelling guy!": {
      "dialogue": f"Here's some of my {TerminalColors.BROWN}scum spray{TerminalColors.RESET}, you can use it to smell great like me!",
      "responses": "END1"
    }
  }
}