from colors import TerminalColors

hari_dialogue = {
  "dialogue": f"Do you have {TerminalColors.GREEN}$5{TerminalColors.RESET} bro?",
  "audio": "5dollar.mp3",
  "responses": {
    "Stay broke Hari": {
      "audio": "imgonnarage.mp3",
      "dialogue": f"I'm gonna {TerminalColors.RED}rage{TerminalColors.RESET}!",
      "responses": "END3"
    },
    "I don't have any money, sorry great guy": {
      "audio": "gimmelater.mp3",
      "dialogue": "Alright bro just give me it later.",
      "responses": "END1"
    },
    f"Alright, here's {TerminalColors.GREEN}$5{TerminalColors.RESET}": {
      "audio": "polyesterforyourtroubles.mp3",
      "dialogue": f"Thanks bro, your heem. Here's some {TerminalColors.MAGENTA}polyester{TerminalColors.RESET} for your troubles!",
      "responses": "END2",
      "condition": "user.money >= 5"
    }
  }
}  