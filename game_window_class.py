import pygame
import copy
from cell_class import *


WIN_HEIGHT = 700
WIN_WIDTH = 1100
WINDOW_COLOUR = (74, 60, 55)


vec = pygame.math.Vector2


class GameWindow:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.pos = vec(x, y)
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = int(WIN_HEIGHT/CELL_SIZE)
        self.cols = int(WIN_WIDTH/CELL_SIZE)
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)


    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()


    def draw(self):
        self.image.fill((WINDOW_COLOUR))        
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))


    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)


    def evaluate(self):
        # use old grid to evaluate so that all cells see the same grid for making updates
        new_grid = copy.copy(self.grid)

        # count live neighbours
        for row in self.grid:
            for cell in row:
                cell.live_neighbours()

        # update rules
        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if (cell.alive_neighbours == 2) or (cell.alive_neighbours == 3):
                        new_grid[yidx][xidx].alive = True
                    if cell.alive_neighbours < 2:
                        new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbours > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    if cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True
        # update grid
        self.grid = new_grid
                