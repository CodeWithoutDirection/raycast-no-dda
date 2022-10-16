import pygame
from settings import *
from ray import Ray
import math


class Particle:
    def __init__(self, window):
        self.window = window
        self.pos = pygame.math.Vector2(RES[0]//2,RES[1]//2)
        self.rays = []
        for a in range(0, 360, 1): self.rays.append(Ray((self.pos.x, self.pos.y), a))

    def look(self, walls):
        closest_point = []
        closest_distance = []
        for rays in self.rays:
            for wall in walls:
                pt = rays.cast(wall)
                if pt:
                    closest_point.append(pt)
                    closest_distance.append(math.sqrt((pt.y-rays.pos.y)**2 + (pt.x-rays.pos.x)**2))
                    # closest_distance.append(rays.pos.distance_to(pt))

            if closest_point:
                pygame.draw.line(self.window, 'white', rays.pos, closest_point[closest_distance.index(min(closest_distance))])
            closest_distance.clear()
            closest_point.clear()

