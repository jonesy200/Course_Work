import pygame
from game_files.utils.settings import ANIMATION_FPS, HITBOXES

class Unit:
    def __init__(self, x, y, max_health=100, speed=2):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.health = max_health
        self.speed = speed

        self.direction = 1
        self.moving = False

        self.state = "idle"
        self.frame_index = 0
        self.last_frame_time = 0

        self.animations = {
            "idle": [],
            "walk": [],
            "attack": [],
        }

        self.attack_damage = 25
        self.attack_range = 60
        self.attack_cooldown = 1000
        self.last_attack_time = 0

        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def update(self):
        if not self.animations.get(self.state):
            return

        now = pygame.time.get_ticks()
        frame_delay = 1000 // ANIMATION_FPS

        if now - self.last_frame_time >= frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.state])
            self.last_frame_time = now


    def draw(self, screen):
        if not self.animations.get(self.state):
            return

        frame = self.animations[self.state][self.frame_index]

        if self.direction == -1:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (self.x, self.y))
        bound = frame.get_bounding_rect()
        self.rect = bound.move(self.x, self.y)

        if HITBOXES:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def move(self, dx, dy):
        if dx == 0 and dy == 0:
            return

        if dx != 0:
            self.direction = dx / abs(dx)

        self.x += dx
        self.y += dy
        self.moving = True

    def change_direction(self):
        self.direction *= -1

    def set_state(self, new_state):
        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.last_frame_time = 0

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        pass

    def on_attack_finish(self):
        pass

