import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event 
import random

class Asteroid(CircleShape):
  def __init__(self, x: float, y: float, radius: float) -> None:
    super().__init__(x, y, radius)

  def draw(self, screen : pygame.Surface) -> None:
    pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      log_event('asteroid_split')
      random_rotation = random.uniform(20, 50)
      split_a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      split_a.velocity = self.velocity.rotate(random_rotation) * 1.2
      split_b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      split_b.velocity = self.velocity.rotate(random_rotation * -1) * 1.2

  def update(self, dt : float) -> None:
    self.position += self.velocity * dt
