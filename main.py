import pygame
import sys
from settings import *
from boundary import Boundary
from particle import Particle


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        
        self.walls = []
        self.walls.append(Boundary(182,100,300,50))
        self.walls.append(Boundary(150,50,100,300))
        self.walls.append(Boundary(125,500,450,500))
        self.walls.append(Boundary(600,120,350,220))
        self.walls.append(Boundary(700, 120, 250, 520))
        self.walls.append(Boundary(450,500,150,50))
        self.walls.append(Boundary(-1,-1,RES[0],0)) # top side
        self.walls.append(Boundary(RES[0],0,RES[0],RES[1])) # right side
        self.walls.append(Boundary(-1,-1,0,RES[1])) # left side
        self.walls.append(Boundary(0,RES[1],RES[0],RES[1])) # bottom side
        self.particle = Particle(self.window)

    def update(self):
        pygame.display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.window.fill('black')
        for wall in self.walls: wall.draw(self.window)
        for rays in self.particle.rays: rays.draw(self.window)
        self.particle.look(self.walls)


    def check_events(self):
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        for rays in self.particle.rays: rays.update(mx, my)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
