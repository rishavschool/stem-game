from colors import TerminalColors

jj_dialogue = {
  "dialogue": "Hey!",
  "responses": {
    "What are you doing?": {
      "dialogue": "I'm playing Minecraft!",
      "responses": {
        "Are you building a house?": {
          "dialogue": "Yes, I'm building my house out of gravel!",
          "responses": {
            "Man, you suck at Minecraft...": {
              "dialogue": "Man, you suck at life!",
              "responses": "END1"
            },
            "Can I have some gravel?": {
              "dialogue": "Sure, I'm a generous guy.",
              "responses": "END2"
            }
          }
        }
      },
    }
  }
}