import pygame

class Player():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.speed = 5
    self.width = 20
    self.height = 20
    self.color = (255,0,0)
    self.rect = (self.x, self.y, self.width, self.height)

  def move(self, window):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
      self.x -= self.speed

    if keys[pygame.K_RIGHT]:
      self.x += self.speed

    if keys[pygame.K_UP]:
      self.y -= self.speed

    if keys[pygame.K_DOWN]:
      self.y += self.speed

    width, height = window.get_size()
    draw_x = width // 2 - self.width // 2
    draw_y = height // 2 - self.height // 2
    self.rect = (draw_x, draw_y, self.width, self.height)

  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect)