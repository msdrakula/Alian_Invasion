import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()  #Ссылка на класс Settings - настройки

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #Отслеживание событий клавиатуры и мыши
            self._check_events()

            self.ship.update()

            self._update_bullets()


            #При каждом проходе цикла перерисовывается экран
            self._update_screen()


    def _check_events(self): # Обслуживает важные события(нажатия и отпускаяния клавишь)
        """Обрабатывает нажатие цикла перерисовывается экран"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Выход из игры, нажатием на закрытие окна
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
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

                elif event.key == pygame.K_q: # Клавиша выхода из игры 'q'
                    sys.exit()

                elif event.key == pygame.K_SPACE: # Клавиша выстрела 'пробел'
                    self._fire_bullet()

    def _check_keyup_events(self,event):
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляем позиции снарядов и уничтожает старые снаряды"""
        #Обновление позиции снарядов
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) #Проверка на удаление снарядов по достижении верхней части экрана



    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)  # Заполнение цветом фона методом fill

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()




if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()