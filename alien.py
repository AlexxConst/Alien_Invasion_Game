import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализируем пришельца"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/aliens_ship.png')
        self.image = pygame.transform.scale(self.image, (120, 130))
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает Тру если пришелец находится у экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return None

    def update(self):
        """перемещаем пришельцев вправо"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
