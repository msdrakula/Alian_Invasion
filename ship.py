import pygame

class Ship():
	"""Класс для управления кораблем"""
	def __init__(self, ai_game):
		"""Инициализирует корабль и задает его начальную позицию"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/spaceship.bmp')
		self.rect = self.image.get_rect()

		#Каждый новый корабль появляется у нижнего края экрана
		self.rect.midbottom = self.screen_rect.midbottom

		#Сохраняет вещественной координаты центра корабля
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Флаг премещения
		self.moving_right = False # Перемещение вправо
		self.moving_left = False # Перемещение влево
		self.moving_up = False # Перемещение вверх
		self.moving_down = False # Перемещение вниз

	def update(self):
		"""Обновляет позицию корабля с учетом флага"""
		#Обновляется атрибут x, не rect.
		if self.moving_right and self.rect.right < self.screen_rect.right: # Перемещение вправо
			self.x += self.settings.ship_speed # Скорость перемещения

		if self.moving_left and self.rect.left > 0: # Перемещение влево
			self.x -= self.settings.ship_speed # Скорость перемещения

		if self.moving_up and self.screen_rect.top < self.rect.top: # Перемещение вверх
			self.y -= self.settings.ship_speed # Скорость перемещения

		if self.moving_down and self.screen_rect.bottom > self.rect.bottom: # Перемещение вниз
			self.y += self.settings.ship_speed # Скорость перемещения

		#Обновление атрибута rect на основании self.x
		self.rect.x = self.x

		#Обновление атрибута rect на основании self.x
		self.rect.y = self.y


	def blitme(self):
		"""Рисует корабль в текущей позиции"""
		self.screen.blit(self.image, self.rect)