import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game, scale=1.0):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ufo1.png')

        base_width, base_height = 230, 130
        self.image = pygame.transform.scale(
            self.image,
            (int(base_width * scale), int(base_height * scale))
        )

        self.rect = self.image.get_rect()

        # Только основной корабль ставим вниз
        if scale == 1.0:
            self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут х не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # обновление атрибута рект на основание селф.х
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
