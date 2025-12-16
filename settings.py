class Settings:
    """Класс для хранения всех настроек"""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (164, 197, 234)
        # Настройка корабля
        self.ship_speed = 20
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 20.0
        self.bullet_width = 13
        self.bullet_height = 25
        self.bullet_color = (255, 154, 0)
        self.bullets_allowed = 3
        self.alien_speed = 7
        self.fleet_drop_speed = 20
        # self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 7.7
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 10.0
        self.bullet_speed_factor = 10.0
        self.alien_speed_factor = 10.0

        self.fleet_direction = 1

        # подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)