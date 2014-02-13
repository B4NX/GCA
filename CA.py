#!/usr/bin/env python

#Cellular Automata Visualiser
#(inspired by Wolfram's New Kind of Science)
#Vadim Kataev 2005
#vkataev at gmail.com

#Modifications by Andrew Chronister and Nikko Rush
#2014

import sys,pygame, random, testCA
from pygame.locals import *

CA_SCREEN_WIDTH  = 400
CA_SCREEN_HEIGHT = 800

rows = [[1],]
steps = 0

color_cell = (45,45,45)
color_background = (255,255,255)

ruleNum = 214
ruleSet = ()

sy = 0
x_half = CA_SCREEN_WIDTH / 2

fixedwidth = False

def makeRule(ruleNum):
    digits = bin(ruleNum)[2:]
    digits = ''.join(["0" for i in range(8 - len(digits))]) + digits
    rule = ((1,1,1,int(digits[0])), (1,1,0,int(digits[1])), (1,0,1,int(digits[2])), (1,0,0,int(digits[3])), (0,1,1,int(digits[4])), (0,1,0,int(digits[5])), (0,0,1,int(digits[6])), (0,0,0,int(digits[7])))
    return rule

def rule(left, center, right, rule_set):
    for r in rule_set:
        if left == r[0] and center == r[1] and right == r[2]:
            return r[3]
    print("ERROR in Rule")
    sys.exit()

def rrule(top, left, center, right, rule_set):
    for r in rule_set:
        if left == r[0] and center == r[1] and right == r[2]:
            if (top == 0): return r[3]
            else: return 1 - r[3]

def r_build_next_row(prerow, preprerow, step = 0):
    global ruleSet
    row = []
    l = len(prerow)
    for i in range(-1,l+1 if step >= 0 else l - 1):
        if i == -1:
            row.append(0)
            continue
        if i == l:
            row.append(0)
            continue

        if i == 0: left = 0
        else: left = prerow[i-1]
        center = prerow[i]
        if i == (l-1): right = 0
        else: right = prerow[i+1]

        if ((i == 0 or i == (l - 1)) and step >= 0):
            top = 0
        else:
            top = preprerow[i - 1]

        row.append(rrule(top, left, center, right, ruleSet))
    return row

def build_next_row(prerow):
    global ruleSet
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

        cell = rule(left, right, center, ruleSet)
        
        if (fixedwidth):
            if (i == 0): 
                row[0] = cell
                continue
            if (i == l - 1): 
                row[l - 2] = cell
                continue
        row.append(cell)
    return row

#def build_prev_row(nextrow):


def update_screen(r):
    global sy, x_half
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
    global rows, steps
    rows.append(r_build_next_row(rows[-1], rows[-2]))
    rows = rows[-2:]
    steps += 1
    #rows[-1] = trim_list(rows[-1])

def r_update_rows():
    global rows, steps
    rows.append(r_build_next_row(rows[-1], rows[-2], steps))
    rows = rows[-2:]
    steps += 1

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
    r_initCA()

def initCA():
    global rows, ruleSet
    ruleSet = makeRule(ruleNum)
    irow = seed_rows()
    rows = [irow, irow]
    steps = 0

def r_initCA():
    global rows, ruleSet
    ruleSet = makeRule(ruleNum)
    irow = r_seed_rows()
    rows = [irow[1], irow[0]]
    steps = -5

###REWRITE ME for GA-controlled initial conditions
def seed_rows():
    #return [random.randint(0,1) * random.randint(0,1) for i in range(CA_SCREEN_WIDTH - 4)]
    return [1] #[0 for i in range(int(CA_SCREEN_WIDTH / 2 - 1))] + [1] + [0 for i in range(int(CA_SCREEN_WIDTH / 2 - 1))]

def r_seed_rows():
    return (testCA.iRow1, testCA.iRow2)
 
def CAmain():
    global rows, steps
    while 1:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    if event.type==pygame.KEYDOWN:
                        pass
                            #pygame.quit()
                            #sys.exit()

            r_update_rows()
            update_screen(rows[-1])
            if (steps == 5): 
                print(rows[-2])
                print(rows[-1])
            pygame.display.flip()

init()
update_screen(rows[0])
update_screen(rows[1])
CAmain()