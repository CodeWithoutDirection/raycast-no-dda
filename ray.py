import pygame
import math

class Ray:
    def __init__(self, pos, a):
        self.pos = pygame.math.Vector2(pos[0], pos[1])
        self.dir = pygame.math.Vector2(math.cos(a), math.sin(a))

    def update(self,mx, my):
        self.pos.x = mx
        self.pos.y = my

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0: return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if 0 < t < 1 and u > 0:
            pt = pygame.math.Vector2()
            pt.x = x1 + t*(x2 - x1)
            pt.y = y1 + t*(y2 - y1)
            return pt
        else: return

    def draw(self, window):
        pygame.draw.line(window, 'gray', (self.pos.x, self.pos.y),
                         (self.pos.x + self.dir.x * 10, self.pos.y + self.dir.y * 10))
