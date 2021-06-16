import pygame
import random

# make sure these have the same values as in game_window_class.py
WIN_HEIGHT = 700
WIN_WIDTH = 1100

CELL_SIZE = 10 # width and height of each cell
DEAD_COLOUR = (33,33,33)
ALIVE_COLOUR = (184, 153, 141)
BORDER_WIDTH = 1


class Cell:
    def __init__(self, surface, grid_x, grid_y):
        self.alive = random.choice([True, False, False, False, False, False, False, False, False])#False #random.choice([True, False])
        self.surface = surface
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.neighbours = []
        self.alive_neighbours = 0


    def update(self):
        self.rect.topleft = (self.grid_x*CELL_SIZE, self.grid_y*CELL_SIZE)


    def draw(self):
        if self.alive:
            self.image.fill(DEAD_COLOUR) # for border
            pygame.draw.rect(self.image, ALIVE_COLOUR, (BORDER_WIDTH, BORDER_WIDTH, CELL_SIZE-(2*BORDER_WIDTH), CELL_SIZE-(2*BORDER_WIDTH)))
        else:
            self.image.fill(DEAD_COLOUR)
        self.surface.blit(self.image, (self.grid_x*CELL_SIZE, self.grid_y*CELL_SIZE))


    def get_neighbours(self, grid):
        neighbour_list = [[1,1], [1,0], [1,-1], [0,1], [0,-1], [-1,1], [-1,0], [-1,-1]]
        for neighbour in neighbour_list:
            neighbour[0] += self.grid_x
            neighbour[1] += self.grid_y
        # wrapping: consider cells on other side of screen neighbours
        nb_cells_wide = WIN_WIDTH//CELL_SIZE
        nb_cells_high = WIN_HEIGHT//CELL_SIZE
        for neighbour in neighbour_list:
            if neighbour[0] < 0:
                neighbour[0] += nb_cells_wide
            if neighbour[1] < 0:
                neighbour[1] += nb_cells_high
            if neighbour[1] > (nb_cells_high-1):
                neighbour[1] -= nb_cells_high
            if neighbour[0] > (nb_cells_wide-1):
                neighbour[0] -= nb_cells_wide

        for neighbour in neighbour_list:
            try:
                self.neighbours.append(grid[neighbour[1]][neighbour[0]])
            except:
                print(neighbour)


    def live_neighbours(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.alive:
                count += 1

        self.alive_neighbours = count
