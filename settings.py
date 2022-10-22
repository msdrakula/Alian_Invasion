class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion"""
	def __init__(self):
		"""Инициализирует настройки игры"""
		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (173, 216, 230)

		#Настройки корабля
		self.ship_speed = 1.5

		# Параметры снаряда
		self.bullet_speed = 3 #Скорость снаряда
		self.bullet_width = 4 #Ширина снаряда
		self.bullet_height = 17 #Длина снаряда
		self.bullet_color = (255, 0, 255) # Цвет снаряда
		self.bullets_allowed = 50 # Количество доступных выстрелов одновременно

		#Настройки пришельцев
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10 #Величина снижения флота
		# fleet_direction = 1 обозначает движение вправо, а -1 влево
		self.fleet_direction = 1
