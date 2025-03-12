from colors import TerminalColors

jj_dialogue = {
  "dialogue": "Hey!",
  "audio": "heyjj.mp3",
  "responses": {
    "What are you doing?": {
      "dialogue": f"I'm playing {TerminalColors.GREEN}Minecraft{TerminalColors.RESET}!",
      "audio": "playingmc.mp3",
      "responses": {
        "Are you building a house?": {
          "dialogue": f"Yes, I'm building my house out of {TerminalColors.LIGHT_GRAY}gravel{TerminalColors.RESET}!",
          "audio": "gravelhouse.mp3",
          "responses": {
            "Man, you suck at Minecraft...": {
              "dialogue": "Man, you suck at life!",
              "audio": "suckatlife.mp3",
              "responses": "END1"
            },
            f"Can I have some {TerminalColors.LIGHT_GRAY}gravel{TerminalColors.RESET}?": {
              "dialogue": "Sure, I'm a generous guy.",
              "audio": "generousguy.mp3",
              "responses": "END2"
            }
          }
        }
      },
    }
  }
}