import pygame
from player import Player

window = None

def setup_window():
  global window
  window_size = (1600, 900)
  icon = pygame.image.load("assets/images/icons/stem_icon.png")

  window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
  pygame.display.set_caption("Scum of Stem")
  pygame.display.set_icon(icon)


def draw_window(window, plr):
  window.fill((0,0,0))
  plr.draw(window)
  pygame.display.update()

def main():
  run = True
  clock = pygame.time.Clock()
  plr = Player()

  while run:
    global window
    clock.tick(60)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        return
      elif event.type == pygame.VIDEORESIZE:
        width, height = event.size
        width = max(width, 1120)
        height = max(height, 630)
        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    plr.move(window)  
    draw_window(window, plr)

setup_window()
main()  