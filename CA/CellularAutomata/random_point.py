#!/usr/bin/env python
#Vadim Kataev 2007
#vkataev at gmail.com

import sys,pygame, random
from pygame.locals import *

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 1024

color_cell = (45,45,45)
color_background = (255,255,255)

CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

point_coords = []

xy = [CENTER_X, CENTER_Y]
(dir_x,dir_y) = (0,0)


def rule():
	global point_coords, dir_x, dir_y, xy
	if random.randint(0,100) == 0:
		L = random.randint(1,150)
		xy[0] = CENTER_X + random.randint(-L,L)
		xy[1] = CENTER_Y + random.randint(-L,L)

	L = random.randint(1,5)
	dir_x = random.randint(-L,L)#random.randint(0, point_coords[-1][0])
	dir_y = random.randint(-L,L)#random.randint(0, point_coords[-1][1])
	#point_coords.append([dir_x, dir_y])
	

def update_screen():
	global xy
	#c = point_coords[-1]
	xy[0] += dir_x
	xy[1] += dir_y
	screen.fill(color_cell,(xy[0],xy[1],1,1))
	#screen.fill(color_background,(sx,sy,1,1))
	#screen.fill(color_background)
	return

def init():
	global screen, point_coords
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN)
	pygame.display.set_caption("Random")
	screen.fill(color_background)
	point_coords.append([random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)])
 
def main():
	while 1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type==pygame.KEYDOWN:
				pygame.quit()
				sys.exit()
		update_screen()
		rule()
		pygame.display.flip()

init()
main()

