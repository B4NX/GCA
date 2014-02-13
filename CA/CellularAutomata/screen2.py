import sys, pygame, math
import globals

black = 0, 0, 0

class Screen:
	def __init__(self, w=1024, h=768, t='window'):
		pygame.init()
		
		self.w=w
		self.h=h
		self.cw=w/2
		self.ch=h/2
		self.t=t
		self.fade_speed=220

		self.pic = pygame.Surface((self.w, self.h), globals.rgbbits)				
		
		if self.t == 'window':
			self.dst = pygame.display.set_mode((self.w, self.h), pygame.DOUBLEBUF, globals.rgbbits)
			# pygame.DOUBLEBUF|
		else:
			self.dst = pygame.display.set_mode((self.w, self.h),pygame.FULLSCREEN|pygame.DOUBLEBUF, globals.rgbbits)
		self.fonts = {}
		
		
		self.dst.fill(black)
		
	def render(self):
		pygame.display.flip()
		#self.dst.fill(black)		
	
	def fade_in(self, synchro):
		self.pic.blit(self.dst, (0, 0, -1, -1))
		for i in range(0, 255, 5):
			synchro(self.fade_speed)
			self.pic.set_alpha(i)
			self.dst.fill(black)		
			self.dst.blit(self.pic, (0, 0, -1, -1))
			self.render()
			
	def fade_out(self, synchro):
		self.pic.blit(self.dst, (0, 0, -1, -1))
		for i in range(255, 0, -5):
			synchro(self.fade_speed)
			self.pic.set_alpha(i)
			self.dst.fill(black)		
			self.dst.blit(self.pic, (0, 0, -1, -1))
			self.render()



class Image:
	def __init__(self, name, dst, transprgb=-1):
		self.image = pygame.image.load(globals.GFXPATH + name).convert(globals.rgbbits, pygame.RLEACCEL) #WARNING: maybe without options is faster
		if transprgb != -1:
			self.image.set_colorkey(transprgb, pygame.RLEACCEL)
		self.rect = self.image.get_rect()
		self.dst = dst
		self.buffer = self.image
		
	def scale(self, x, y=-1):
		if y==-1:
			s = x
			x = int(self.rect[2] * s)
			y = int(self.rect[3] * s)
		self.buffer = pygame.transform.scale(self.image, (x, y))
	def render(self, x=0, y=0):
		rect = (x, y, -1, -1)
		self.dst.blit(self.buffer, rect)


class UImage:
	def __init__(self, name, dst, transprgb=-1):
		self.image = pygame.image.load(globals.GFXPATH + 'units/' + name).convert(globals.rgbbits, pygame.RLEACCEL) #WARNING: maybe without options is faster
		if transprgb != -1:
			self.image.set_colorkey(transprgb, pygame.RLEACCEL)
		self.rect = self.image.get_rect()
		self.dst = dst
		self.buffer = self.image
		
	def scale(self, x, y=-1):
		if y==-1:
			s = x
			x = int(self.rect[2] * s)
			y = int(self.rect[3] * s)
		self.buffer = pygame.transform.scale(self.image, (x, y))
	def render(self, x=0, y=0):
		rect = (x, y, -1, -1)
		self.dst.blit(self.buffer, rect)


class ImageForCard(Image):
	def __init__(self, name, dst, transprgb=-1):
		#we use full path here
		self.image = pygame.image.load(name).convert(globals.rgbbits, pygame.RLEACCEL) #WARNING: maybe without options is faster
		if transprgb != -1:
			self.image.set_colorkey(transprgb, pygame.RLEACCEL)
		self.rect = self.image.get_rect()
		self.dst = dst
		self.buffer = self.image


class Font:
	def __init__(self, name, size, dst, rgb=black, italic=False, bold=False, antialias=1):
		self.font = pygame.font.Font(globals.FNTPATH + name, size)
		self.name = name.split('/')[-1]
		self.name = self.name.split('.')[0]
		self.dst = dst
		self.antialias = antialias
		self.rgb = rgb
		self.font.set_italic(italic)
		self.font.set_bold(bold)
	def render(self, text, x, y, rgb=(-1, -1, -1)):
		if rgb == (-1, -1, -1): rgb = self.rgb
		self.image = self.font.render(text, self.antialias, rgb)
		self.dst.blit(self.image, (x, y))
	def render_by_center(self, text, centerx, centery, scale=1.0, rgb=(-1, -1, -1)):
		if rgb == (-1, -1, -1): rgb = self.rgb
		size = self.font.size(text)
		x = centerx - size[0]*scale / 2 
		y = centery - size[1]*scale / 2 
		self.image = self.font.render(text, self.antialias, rgb)
		self.image = pygame.transform.scale(self.image, (int(size[0]*scale), int(size[1]*scale)))
		self.dst.blit(self.image, (x, y))


class FontAnimColors(Font):
	def __init__(self, name, size, dst, rgb=black, italic=False, bold=False, antialias=1):
		#Font.__init__(self, name, size, dst, rgb, italic, bold, antialias)
		self.font = pygame.font.Font(globals.FNTPATH + name, size)
		self.dst = dst
		self.antialias = antialias
		self.rgb = rgb
		self.rgb_lim = 30
		self.font.set_italic(italic)
		self.font.set_bold(bold)
	def render(self, text, x, y, rgb=(-1, -1, -1), animate=False):
		if rgb == (-1, -1, -1): rgb = self.rgb
		rgbf=list(rgb)
		if animate == True:
			rgbf[0] = rgb[0]
			rgbf[1] = rgb[1] - math.cos(globals.count/math.pi/10)*self.rgb_lim
			rgbf[2] = rgb[2]
		Font.render(self, text, x, y, rgbf)
	def render_by_center(self, text, centerx, centery, scale=1.0, rgb=(-1, -1, -1), animate=False):
		if rgb == (-1, -1, -1): rgb = self.rgb
		rgbf=list(rgb)
		size = self.font.size(text)
		x = centerx - size[0]*scale / 2 
		y = centery - size[1]*scale / 2 
		
		if animate == True:
			rgbf[0] = rgb[0]
			rgbf[1] = rgb[1] - math.cos(globals.count/math.pi/10)*self.rgb_lim
			rgbf[2] = rgb[2]

		self.image = self.font.render(text, self.antialias, rgbf)
		self.image = pygame.transform.scale(self.image, (int(size[0]*scale), int(size[1]*scale)))
		self.dst.blit(self.image, (x, y))
	def render_periodic_by_center(self, text, centerx, centery, dscale=0.2, rgb=(-1, -1, -1), animate=False):
		if rgb == (-1, -1, -1): rgb = self.rgb
		scale = 1.0 + math.cos(globals.count/math.pi/5) * dscale
		self.render_by_center(text, centerx, centery, scale, rgb, animate)




class Music:
	def __init__(self, name):
		self.name = name
		pygame.mixer.music.load(globals.SNDPATH + name)
	def add(self, name):
		pygame.mixer.music.queue(name)
	def play(self):
		pygame.mixer.music.play(-1)
	

class Sound:
	def __init__(self, name, start=100, cycle=100, vol=0.5):
		self.name = name
		self.cycle = cycle
		self.start = start
		self.vol = vol
		self.sound = pygame.mixer.Sound(globals.SNDPATH + name)
	def play(self):
		self.sound.set_volume(self.vol)
		self.sound.play()
	def play_if_need(self):
		if ((globals.count - self.start) % self.cycle) == 0:
			self.sound.set_volume(self.vol)
			self.sound.play()


