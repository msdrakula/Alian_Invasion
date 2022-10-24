class Settings:
	"""Класс для хранения всех настроек игры Alien Invasion"""
	def __init__(self):
		"""Инициализирует настройки игры"""
		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (173, 216, 230)

		#Настройки корабля
		self.ship_limit = 3 # Количество жизней


		self.bullet_width = 4 #Ширина снаряда
		self.bullet_height = 17 #Длина снаряда
		self.bullet_color = (255, 0, 255)  # Цвет снаряда
		self.bullets_allowed = 30  # Количество доступных выстрелов одновременно

		self.fleet_drop_speed = 10  # Величина снижения флота

		self.speedup_scale = 1.1  # Быстрота нарастания скорости

		#Темп роста стоимости прищельцев
		self.score_scale = 1.5


		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Инициализируте настройки, изменяющиеся в ходе игры"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		#fleet_direction = 1 обозначает движение вправо, а -1 влево
		self.fleet_direction = 1

		#Подсчет очков
		self.alien_points = 50


	def increase_speed(self):
		"""Увеличение настройки сокрости и стоимость пришельцев"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)


