from colors import TerminalColors

#potdar family dialogue
unc_dialogue_potdar = {
  "dialogue": "Hey why are you in my hut, bastard?",
  "audio": "inmyhut.mp3",
  "responses": {
    f"I was looking for {TerminalColors.YELLOW}Delilah{TerminalColors.RESET}": {
      "dialogue": f"{TerminalColors.YELLOW}Delilah{TerminalColors.RESET} is my wife, I am also looking for her!",
      "responses": {
        f"I think {TerminalColors.YELLOW}Delilah{TerminalColors.RESET} is long dead unc": {
          "dialogue": f"Don't ever say that about my sweet {TerminalColors.YELLOW}Delilah{TerminalColors.RESET}.",
          "responses": "END1"
        },

        f"{TerminalColors.YELLOW}Delilah{TerminalColors.RESET} is top 10 great guys in the world": {
          "dialogue": "Thank you, great guy.",
          "audio": "thankyougreatguy.mp3",
          "responses": "END2"
        }
      }
    },

    "I got lost, sorry unc": {
      "dialogue": "Ohh.... where's shreyan when you need him, say you kind of look like shreyan.",
      "audio": "wheresshreyanwhenu.mp3",
      "responses": {
        "Thats because shreyan is my deep cousin, I'm a great relative of his.": {
          "dialogue": "Ohhh shreyann.... ohhhh mangesh...",
          "responses": "END2"
        }
      }
    }
  }
}

#ravikanth family dialogue
unc_dialogue_ravikanth = {
  "dialogue": "I know your family...",
  "responses": {
    "What?": {
      "dialogue": "I'm going to cook you",
      "responses": "END1"
    }
  }
}

#unc family dialogue
unc_dialogue_unc = {
  "dialogue": "Hey, who are you...",
  "responses": {
    "Are you an unc? I am also an unc": {
      "dialogue": f"Wow... I am looking for my wife {TerminalColors.YELLOW}Delilah{TerminalColors.RESET}, have you seen her?",
      "responses": {
        f"No, who is {TerminalColors.YELLOW}Delilah{TerminalColors.RESET}?": {
          "dialogue": "You are not a real unc...",
          "responses": "END2"
        },
        f"{TerminalColors.YELLOW}Delilah{TerminalColors.RESET}? She is also my wife": {
          "dialogue": f"No.. {TerminalColors.YELLOW}Delilah{TerminalColors.RESET} is my true love, I have her statue here in my boiler room hut.",
          "responses": {
            "Liar... she is my deep wife since the cretaceous period.": {
              "dialogue": "...",
              "responses": "END1"
            }
          }
        }
      }
    }
  }
}

#sleep on uncs rock dialogue
unc_dialogue_rock = {
  "dialogue": f"Don't lay on my rock.. Thats where {TerminalColors.YELLOW}Delilah{TerminalColors.RESET} used to sleep.",
  "responses": "END1"
}