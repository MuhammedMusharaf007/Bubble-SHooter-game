import math
import pygame
import copy
import time
import sys
import os
import random
import pygame.gfxdraw
from pygame.locals import *

FPS =                       120
window_width =              940
window_height =             740
text_height =               20
bubble_radius =             20
bubble_width =              bubble_radius * 2
bubble_layers =             5
bubble_adjust =             5
str_X =                     window_width / 2
str_Y =                     window_height - 26
ary_width =                 25
ary_height =                20

RIGHT =     'right'
LEFT =      'left'
blank =     '.'

very_blue =     (51, 255, 255)
black =         (0, 0, 0)
white =         (255, 255, 255)
grey =          (100, 100, 100)
blue =          (0, 0, 255)
red =           (255, 0, 0)
pink =          (255, 192, 203)
light_pink =    (255, 192, 203)
hot_pink =      (255, 105, 180)
deep_pink =     (255, 20, 147)
cyan =          (0, 255, 255)
peacock_blue =  (0, 164, 180)
grape_colour =  (128, 49, 167)
amber =         (255, 198, 0)
comic =         (0, 174, 239)
light_grey =    (217, 217, 217)
peach =         (255, 229, 180)
green =         (0, 255, 0)
GRAY =          (100, 100, 100)

background_color = very_blue
color_list = [black, white, grey, blue, red, pink, light_pink, hot_pink, deep_pink, cyan, peacock_blue, grape_colour, amber, comic, light_grey, peach, green]

class Bubble(pygame.sprite.Sprite):
    def __init__(self, color, row = 0, col = 0):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = int(str_X)
        self.rect.centery = str_Y
        self.speed = 10
        self.color=  color
        self.radius = bubble_radius
        self.angle = 0
        self.row = row
        self.col = col
    
    def update(self):
        if self.angle == 90:
            xmove = 0
            ymove = self.speed * -1
        elif self.angle < 90:
            xmove = self.xcalc(self.angle)
            ymove = self.ycalc(self.angle)
        elif self.angle > 90:
            xmove = self.xcalc(180 - self.angle) * -1
            ymove = self.ycalc(180 - self.angle)

        self.rect.x += int(xmove)
        self.rect.y += int(ymove)

    def draw(self):
        pygame.gfxdraw.filled_circle(
            dispsurf, self.rect.centerx, self.rect.centery, self.radius, self.color
        )
        pygame.gfxdraw.aacircle(
            dispsurf, self.rect.centerx, self.rect.centery,self.radius, GRAY
        )
    
    def xcalc(self, angle):
        radians = math.radians(angle)
        xmove = math.cos(radians) * self.speed
        return xmove
    
    def ycalc(self, angle):
        radians = math.radians(angle)
        ymove = math.sin(radians) * self.speed
        return ymove
    

class Ary(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.angle = 90
        arrimg = pygame.image.load('Arrow.png')
        arrimg.convert_alpha()

        arrowRect = arrimg.get_rect()
        self.image = arrimg
        self.transformImage = self.image
        self.rect = arrowRect
        self.rect.centerx = int(str_X)
        self.rect.centery = str_Y
    
    def update(self, dir):
        if (dir == LEFT and self.angle < 180):
            self.angle += 2
        elif (dir == RIGHT and self.angle > 0):
            self.angle -=2
    
        self.transformImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.transformImage.get_rect()
        self.rect.centerx = int(str_X)
        self.rect.centery = str_Y
    
    def draw(self):
        dispsurf.blit(self.transformImage, self.rect)
        