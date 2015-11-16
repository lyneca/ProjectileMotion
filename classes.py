__author__ = 'wing2048'
from constants import *

objects = pygame.sprite.Group()

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, mass, elastic, vx=0, vy=0):
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()

        self.playing = False

        self.mass = mass
        self.x = x
        self.y = SCREEN_HEIGHT - y
        self.start_x = self.x
        self.start_y = self.y
        self.vx = vx
        self.vy = -vy
        self.start_vx = self.vx
        self.start_vy = self.vy

        self.rect.x = self.x
        self.rect.y = self.y
        pygame.sprite.Sprite.__init__(self)
        objects.add(self)

    def add_velocity(self, vx, vy):
        self.vx += vx
        self.vy += vy

    def update(self):
        if not self.playing:
            return
        self.vy += GRAVITY / FRAMERATE
        self.vx *= AIR_RESISTANCE_MULTIPLIER
        self.vy *= AIR_RESISTANCE_MULTIPLIER
        self.x += self.vx
        self.y += self.vy
        if self.x >= SCREEN_WIDTH - self.rect.width:
            self.reset()
        if self.x <= 0:
            self.reset()
        if self.y >= SCREEN_HEIGHT - self.rect.height:
            self.reset()
        if self.y <= 0:
            self.reset()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_path(self):
        for x in range((SCREEN_WIDTH - self.x) / DOT_GAP):
            Dot(self.x + x * DOT_GAP, self.get_pos(self.x + x * DOT_GAP))

    def get_pos

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vx = self.start_vx
        self.vy = self.start_vy