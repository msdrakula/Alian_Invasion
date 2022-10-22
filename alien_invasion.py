import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()  #Ссылка на класс Settings - настройки

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #Отслеживание событий клавиатуры и мыши
            self._check_events()

            self.ship.update()

            #При каждом проходе цикла перерисовывается экран
            self._update_screen()


    def _check_events(self):
        """Обрабатывает нажатие цикла перерисовывается экран"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Выход из игры, нажатием на закрытие окна
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #переместить корабль вправо
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # переместить корабль в лево
                    self.ship.moving_left = True

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)  # Заполнение цветом фона методом fill

        self.ship.blitme()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()