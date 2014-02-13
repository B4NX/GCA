#!/usr/bin/env python

#Cellular Automata Visualiser
#(inspired by Wolfram's New Kind of Science)
#Vadim Kataev 2005
#vkataev at gmail.com

import sys,pygame, random
from pygame.locals import *

#import psyco
#psyco.full()

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 1024

init_row = [[random.randint(0,1) for i in range(80)],]
rows = init_row[:]

color_cell = (45,45,45)
color_background = (255,255,255)

#rule_110 = ((1,1,1,0), (1,1,0,1), (1,0,1,1), (1,0,0,0), (0,1,1,1), (0,1,0,1), (0,0,1,1), (0,0,0,0))
#rule_30 = ((1,1,1,0), (1,1,0,0), (1,0,1,0), (1,0,0,1), (0,1,1,1), (0,1,0,1), (0,0,1,1), (0,0,0,0))

sy = 0
x_half = SCREEN_WIDTH / 2

def rule(left, center, right, rule_num):
	#for r in rule_num:
	#	if left == r[0] and center == r[1] and right == r[2]:
	#		return r[3]
	#print "ERROR in Rule"
	#sys.exit()
	sum = left + center + right + rule_num
	if sum == 3:
		sum = 0
	sum *= 20000
	r = random.randint(0, sum)# 0 or 1 or 2
	if r > 0:
		r = 1
	else:
		r = 0
	#if r > 0: 
	#	print left
	return r

def build_next_row(prerow):
	row = []
	l = len(prerow)
	for i in range(-1,l+1):
		if i == -1:
			row.append(0)
			continue
		if i == l:
			row.append(0)
			continue

		if i == 0:
			left = 0
		else:
			left = prerow[i-1]
		center = prerow[i]
		if i == (l-1):
			right = 0
		else:
			right = prerow[i+1]
		#print left, center, right
		r = rule(left, center, right, 0)
		row.append(r)
	return row

def update_screen():
	global sy, x_half
	r = rows[-1]
	x = x_half - len(r)/2
	for elem in r:
		if elem:
			screen.fill(color_cell,(x,sy,1,1))
		else:
			screen.fill(color_background,(x,sy,1,1))
		x+=1
	sy+=1
	if sy == SCREEN_HEIGHT:
		sy = 0
#		screen.fill(color_background)

def update_rows():
	global rows, sy, init_row
	rows.append(build_next_row(rows[-1]))
	rows = rows[1:]

	#check either row has nothing
	sum = 0
	for i in rows[0]:
		sum += i

	if sum == 0:
		print rows
		rows[:] = init_row[:]
		sy = 0
		screen.fill(color_background)
		#print 'x ',

	update_screen()

def init():
    global background, screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN)
    pygame.display.set_caption("Cellular automata")
    screen.fill(color_background)
 
def main():
    angle=0
    while 1:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    if event.type==pygame.KEYDOWN:
                            pygame.quit()
                            sys.exit()

            update_rows()
            pygame.display.flip()


init()
main()

#import profile
#profile.run('main()')
