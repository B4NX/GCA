#!/usr/bin/env python

#Cellular Automata Visualiser
#(inspired by Wolfram's New Kind of Science)
#Vadim Kataev 2005
#vkataev@gmail.com

#Modifications by Andrew Chronister and Nikko Rush
#2014

import sys
import pygame
import random
import testCA
import CAslice
from pygame.locals import *
from CAslice import Slice

CA_SCREEN_WIDTH = 400
CA_SCREEN_HEIGHT = 800

rows = []
steps = 0

color_cell = (45,45,45)
color_background = (255,255,255)

ruleNum = 214
ruleSet = ()

clipSize = 256

sy = 0
x_half = CA_SCREEN_WIDTH / 2

fixedwidth = False

def makeRule(ruleNum):
    digits = bin(ruleNum)[2:]
    digits = ''.join(["0" for i in range(8 - len(digits))]) + digits
    rule = ((1,1,1,int(digits[0])), (1,1,0,int(digits[1])), (1,0,1,int(digits[2])), (1,0,0,int(digits[3])), (0,1,1,int(digits[4])), (0,1,0,int(digits[5])), (0,0,1,int(digits[6])), (0,0,0,int(digits[7])))
    return rule

def rrule(top, left, center, right, rule_set):
    for r in rule_set:
        if left == r[0] and center == r[1] and right == r[2]:
            if (top == 0): return r[3]
            else: return 1 - r[3]

def r_build_next_row(prerow, preprerow, step = 0, trim = -1):
    global ruleSet
    assert isinstance(prerow, Slice) and isinstance(preprerow, Slice)
    row = Slice()
    l = len(prerow)

    def applyRuleTo(index):
        left, right = prerow.getNeighbors(index)
        try: center = prerow[index]
        except IndexError: center = 0
        try: top = preprerow[index]
        except IndexError: top = 0
        return rrule(top, left, center, right, ruleSet)
    
    cellRange = tuple(map(lambda x, y: x + y, prerow.range(), (-2, 2)))  # if (step <= 0) else (0, 0)))
    for i in range(1, cellRange[1]):
        row.append(applyRuleTo(i))
    for i in range(1, -cellRange[0]):
        row.prepend(applyRuleTo(-i))
    row.setCenterIndex(applyRuleTo(0))
    if (trim > 0):
        row.trimTo(trim)
    return row

def update_screen(r):
    global sy, x_half, screen
    rng = r.range()
    for x in range(rng[0], rng[1]):
        try: val = r[x]
        except IndexError:
            val = 0
        if val:
            screen.set_at((int(x + x_half),sy), color_cell)
        else:
            screen.set_at((int(x + x_half),sy), color_background)
        x+=1
    sy+=1
    if sy == CA_SCREEN_HEIGHT:
        sy = 0
#		screen.fill(color_background)
    pygame.display.flip()

def r_update_rows():
    global rows, steps
    rows.append(r_build_next_row(rows[-1], rows[-2], steps, clipSize // 2))
    rows = rows[-2:]
    steps += 1

def getLastRow():
    return rows[-1]

def update():
    r_update_rows()
    return getLastRow()

def init():
    global background, screen
    pygame.init()
    screen = pygame.display.set_mode((CA_SCREEN_WIDTH,CA_SCREEN_HEIGHT))
    pygame.display.set_caption("Cellular automata")
    screen.fill(color_background)
    update_screen(rows[0])
    update_screen(rows[1])

def r_initCA(seed = [1], stepCount = 500):
    global rows, ruleSet, steps
    ruleSet = makeRule(ruleNum)
    irow = r_seed_rows()
    rows = [Slice(seed), Slice(seed)] #step 5, then step 4
    steps = -stepCount

###REWRITE ME for Crypto-controlled initial conditions
def r_seed_rows():
    return (testCA.initialRow1, testCA.initialRow2)
 
def CAmain():
    global rows, steps
    while steps <= 0:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    if event.type == pygame.KEYDOWN:
                        pass
                            #pygame.quit()
                            #sys.exit()

            r_update_rows()
            update_screen(rows[-1])