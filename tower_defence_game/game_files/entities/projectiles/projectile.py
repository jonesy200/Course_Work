import pygame
import math
from game_files.utils.settings import PROJECTILE_VELOCITY, WIDTH, HEIGHT, HITBOXES
from game_files.entities.entity import Entity

class Projectile(Entity):
    def __init__(self, x, y, target_x, target_y, image, damage=67):
        super().__init__(None, x, y)
        self.image = image
        self.damage = damage

        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance == 0:
            self.vel_x = 0
            self.vel_y = 0
        else:
            self.vel_x = (dx / distance) * PROJECTILE_VELOCITY
            self.vel_y = (dy / distance) * PROJECTILE_VELOCITY

        self.z = 0
        self.vel_z = 6.0
        self.gravity = 0.35
        self.alive = True

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        self.z += self.vel_z
        self.vel_z -= self.gravity

        if self.z <= 0:
            self.z = 0
            self.alive = False

    def draw(self, screen):
        angle = math.degrees(math.atan2(-self.vel_y, self.vel_x))

        rotated_image = pygame.transform.rotate(self.image, angle)
        draw_x = int(self.x - rotated_image.get_width() / 2)
        draw_y = int(self.y - self.z - rotated_image.get_height() / 2)

        shadow_w = max(6, int(self.image.get_width() * 0.6))
        shadow_h = max(2, int(self.image.get_height() * 0.2))
        shadow = pygame.Surface((shadow_w, shadow_h), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 100), (0, 0, shadow_w, shadow_h))
        screen.blit(shadow, (int(self.x - shadow_w / 2), int(self.y + 6)))

        screen.blit(rotated_image, (draw_x, draw_y))

        bound = rotated_image.get_bounding_rect()
        self.rect = bound.move(draw_x, draw_y)

        if HITBOXES:
            pygame.draw.rect(screen, self.hitbox_colour, self.rect, 2)

    def is_off_screen(self):
        return (
            self.x < -50 or self.x > WIDTH + 50 or
            self.y < -50 or self.y > HEIGHT + 50
        )