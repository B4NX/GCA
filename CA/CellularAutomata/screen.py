import sys, pygame, math

black = 0, 0, 0
rgbbits = 8

class Screen:
	def __init__(self, w=1024, h=768, t='window'):
		pygame.init()
		
		self.w=w
		self.h=h
		self.cw=w/2
		self.ch=h/2
		self.t=t
		self.fade_speed=220

		self.pic = pygame.Surface((self.w, self.h), rgbbits)				
		
		if self.t == 'window':
			self.dst = pygame.display.set_mode((self.w, self.h), pygame.DOUBLEBUF, globals.rgbbits)
			# pygame.DOUBLEBUF|
		else:
			self.dst = pygame.display.set_mode((self.w, self.h),pygame.FULLSCREEN|pygame.DOUBLEBUF, globals.rgbbits)
		self.fonts = {}
		self.dst.fill(black)
		

