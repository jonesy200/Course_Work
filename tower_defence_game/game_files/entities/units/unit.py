import pygame
from game_files.utils.settings import ANIMATION_FPS, HITBOXES, PARTICLE_DIR
from game_files.entities.entity import Entity
from game_files.systems.spritesheet import Spritesheet

def draw_health_bar(surface, pos, size, borderC, backC, healthC, progress):
    pygame.draw.rect(surface, backC, (*pos, *size))
    pygame.draw.rect(surface, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+1, pos[1]+1)
    innerSize = ((size[0]-2) * progress, size[1]-2)
    rect = (round(innerPos[0]), round(innerPos[1]), round(innerSize[0]), round(innerSize[1]))
    pygame.draw.rect(surface, healthC, rect)

class Unit(Entity):
    def __init__(self, game, x, y, max_health=100, speed=2, groups=None):
        if groups is None:
            groups = []

        super().__init__(game, None, x, y, [game.units, *groups])

        self.max_health = max_health
        self.health = max_health
        self.speed = speed

        self.direction = 1
        self.moving = False

        self.dead = False
        self.death_finished = False
        self.death_pos = None

        self.state = "idle"
        self.frame_index = 0
        self.last_frame_time = 0

        self.animations = {
            "idle": [],
            "walk": [],
            "attack": [],
            "death": []
        }

        self.death_effect = Spritesheet('Dust_02.png', PARTICLE_DIR)
        self.animations['death'] = self.death_effect.get_frames_row(0, 64, 64, 10)


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

        if self.health <= 0 and self.state != "death":
            self.death_pos = self.rect.center
            self.set_state("death")
            self.dead = True

        if self.state == "death" and self.frame_index == len(self.animations["death"]) - 1:
            self.death_finished = True


    def draw(self, screen):
        if not self.animations.get(self.state):
            return

        frame = self.animations[self.state][self.frame_index]

        if self.direction == -1:
            frame = pygame.transform.flip(frame, True, False)

        if self.state == "death":
            draw_rect = frame.get_rect(center=self.death_pos)
        else:
            draw_rect = frame.get_rect(topleft=(self.x, self.y))

        screen.blit(frame, draw_rect.topleft)
        bound = frame.get_bounding_rect()
        self.rect = bound.move(draw_rect.x, draw_rect.y)

        if HITBOXES:
            self.show_hitbox(screen, self.hitbox_colour)

    def draw_health(self, screen):
        health_rect = pygame.Rect(0, 0, 96, 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        max_health = self.max_health
        draw_health_bar(screen, health_rect.topleft, health_rect.size,
                        (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / max_health)

    def show_hitbox(self, screen, colour):
        pygame.draw.rect(screen, colour, self.rect, 2)

    def move(self, dx, dy):
        if self.health <= 0:
            return

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

