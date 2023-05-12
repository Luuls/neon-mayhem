import pygame
import random

class Blast():

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        self.lane = random.randint(1, 4)
    
    def blast_position(self):
        if self.lane == 1:
            self.position_x = 400
            self.position_y = 0
        
        if self.lane == 2:
            self.position_x = 800
            self.position_y = 300
        
        if self.lane == 3:
            self.position_x = 400
            self.position_y = 600
        
        if self.lane == 4:
            self.position_x = 0
            self.position_y = 300
        
    def draw_blast(self, g_screen):
        pygame.draw.circle(g_screen, self.color, (self.position_x, self.position_y), 20)
