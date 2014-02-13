#!/usr/bin/env python

#Cellular Automata Visualiser
#(inspired by Wolfram's New Kind of Science)
#Vadim Kataev 2005
#vkataev at gmail.com

#Modifications by Andrew Chronister and Nikko Rush
#2014

import sys,pygame, random
from pygame.locals import *

CA_SCREEN_WIDTH  = 1280
CA_SCREEN_HEIGHT = 1024

rows = [[1],]
color_cell = (45,45,45)
color_background = (255,255,255)

rule_110 = ((1,1,1,0), (1,1,0,1), (1,0,1,1), (1,0,0,0), (0,1,1,1), (0,1,0,1), (0,0,1,1), (0,0,0,0))
rule_30 = ((1,1,1,0), (1,1,0,0), (1,0,1,0), (1,0,0,1), (0,1,1,1), (0,1,0,1), (0,0,1,1), (0,0,0,0))

sy = 0
x_half = CA_SCREEN_WIDTH / 2

fixedwidth = True

def rule(left, center, right, rule_num):
    for r in rule_num:
        if left == r[0] and center == r[1] and right == r[2]:
            return r[3]
    print("ERROR in Rule")
    sys.exit()

def build_next_row(prerow):
    row = []
    l = len(prerow)
    for i in range(-1,l+1):
        if i == -1:
            if (not(fixedwidth)):
                row.append(0)
            else:
                row.append(prerow[-1])
            continue
        if i == l:
            if (not(fixedwidth)):
                row.append(0)
            else:
                row.append(prerow[0])
            continue

        if i == 0:
            left = prerow[-2]
        else:
            left = prerow[i-1]
        center = prerow[i]
        if i == (l-1):
            right = prerow[1]
        else:
            right = prerow[i+1]

        cell = rule(left, right, center, rule_110)
        
        if (fixedwidth):
            if (i == 0): 
                row[0] = cell
                continue
            if (i == l - 1): 
                row[l - 2] = cell
                continue
        row.append(rule(left, right, center, rule_110))
    return row

def update_screen():
    global sy, x_half
    r = rows[-1]
    x = x_half - len(r)/2
    for elem in r:
        if elem:
            screen.set_at((int(x),sy), color_cell)
        else:
            screen.set_at((int(x),sy), color_background)
        x+=1
    sy+=1
    if sy == CA_SCREEN_HEIGHT:
        sy = 0
#		screen.fill(color_background)

def update_rows():
    global rows
    rows.append(build_next_row(rows[-1]))
    rows = rows[1:]
    rows[-1] = trim_list(rows[-1])

def trim_list(row):
    nrow = row[:]
    excess = int((len(nrow) - (CA_SCREEN_WIDTH - 4)) / 2)
    nrow = row[excess:-excess]
    nrow = [row[-(excess - 1)]] + nrow + [row[excess - 1]]
    return nrow

def getLastRow():
    return rows[-1]

def init():
    global background, screen
    pygame.init()
    screen = pygame.display.set_mode((CA_SCREEN_WIDTH,CA_SCREEN_HEIGHT))
    pygame.display.set_caption("Cellular automata")
    screen.fill(color_background)

def initCA():
    global rows
    rows = seed_rows()

###REWRITE ME for GA-controlled initial conditions
def seed_rows():
    return [[random.randint(0,1) for i in range(1279)],]
 
def CAmain():
    while 1:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    if event.type==pygame.KEYDOWN:
                            pygame.quit()
                            sys.exit()

            update_rows()
            update_screen()
            pygame.display.flip()