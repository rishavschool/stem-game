import threading
import time
from playsound import playsound

def play_aadi_noise(sound1, sound2):
  audio_file = f"./assets/sounds/{sound1}"
  playsound(audio_file)

  audio_file2 = f"./assets/sounds/{sound2}"

  while True:
    playsound(audio_file2)
    time.sleep(0.1)



def arav_hook(user):
  user.inventory["youngla jeans"] += 1

def aadi_hook(user):
  user.inventory["tight ahh joggers"] += 1
  audio_thread = threading.Thread(target=play_aadi_noise, args=("ionknowhowtobreath.mp3", "aadibreathing.mp3"))
  audio_thread.start()

name_hooks = {
  "Arav": arav_hook,
  "Aadi": aadi_hook,
}