# based on A Plus Coding's tutorial at: https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2

import pygame
import sys
from game_window_class import *
from button_class import *


FPS = 60 # max frames per second
EVALUATE_DAMPER = 10 # decrease to fo evaluations faster
WIDTH = 1150
HEIGHT = 800
GAME_WIN_X = 25
GAME_WIN_Y = 75
BG_COLOUR = (59, 55, 53)

RUN_BUTTON_COLOUR = (72, 107, 79)
RUN_BUTTON_HOVER_COLOUR = (82, 125, 91)
RUN_BUTTON_BORDER_COLOUR = (0,0,0) # (33,33,33)

PAUSE_BUTTON_COLOUR = (130, 113, 77)
PAUSE_BUTTON_HOVER_COLOUR = (150, 130, 87)
PAUSE_BUTTON_BORDER_COLOUR = (0,0,0)

RESET_BUTTON_COLOUR = (110, 69, 69)
RESET_BUTTON_HOVER_COLOUR = (135, 84, 84)
RESET_BUTTON_BORDER_COLOUR = (0,0,0)

#--------------------  SETTING FUNCTIONS  --------------------#
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def draw():
    window.fill(BG_COLOUR)
    for button in buttons:
        button.draw()
    game_window.draw()

#--------------------  RUNNING FUNCTIONS  --------------------#
def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)
    if frame_count%(FPS//EVALUATE_DAMPER) == 0:
        game_window.evaluate()

def running_draw():
    window.fill(BG_COLOUR)
    for button in buttons:
        button.draw()
    game_window.draw()

#--------------------  PAUSED FUNCTIONS  --------------------#
def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()

def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)

def paused_draw():
    window.fill(BG_COLOUR)
    for button in buttons:
        button.draw()
    game_window.draw()


def mouse_on_grid(pos):
    if (pos[0] > GAME_WIN_X) and (pos[0] < WIDTH-GAME_WIN_X):
        if (pos[1] > GAME_WIN_Y) and (pos[1] < GAME_WIN_Y+WIN_HEIGHT):
            return True
    return False


def click_cell(pos):
    grid_pos = [pos[0]-GAME_WIN_X, pos[1]-GAME_WIN_Y]
    grid_pos[0] = grid_pos[0]//CELL_SIZE
    grid_pos[1] = grid_pos[1]//CELL_SIZE
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True


def make_buttons():
    buttons = []
    # RUN
    buttons.append(Button(window, WIDTH//2-50, 25, 100, 30, text='RUN',
                         colour=RUN_BUTTON_COLOUR, hover_colour=RUN_BUTTON_HOVER_COLOUR,
                         border_colour=RUN_BUTTON_BORDER_COLOUR, bold_text=True, 
                         function=run_game, state='setting'))
    # PAUSE
    buttons.append(Button(window, WIDTH//2-50, 25, 100, 30, text='PAUSE',
                         colour=PAUSE_BUTTON_COLOUR, hover_colour=PAUSE_BUTTON_HOVER_COLOUR,
                         border_colour=PAUSE_BUTTON_BORDER_COLOUR, bold_text=True, 
                         function=pause_game, state='running'))
    # RESUME
    buttons.append(Button(window, WIDTH//5-50, 25, 100, 30, text='RESUME',
                         colour=RUN_BUTTON_COLOUR, hover_colour=RUN_BUTTON_HOVER_COLOUR,
                         border_colour=RUN_BUTTON_BORDER_COLOUR, bold_text=True, 
                         function=run_game, state='paused'))
    # RESET
    buttons.append(Button(window, WIDTH//1.25-50, 25, 100, 30, text='RESET',
                         colour=RESET_BUTTON_COLOUR, hover_colour=RESET_BUTTON_HOVER_COLOUR,
                         border_colour=RESET_BUTTON_BORDER_COLOUR, bold_text=True, 
                         function=reset_grid, state='paused'))
    return buttons

def run_game():
    global state
    state = 'running'


def pause_game():
    global state
    state = 'paused'


def reset_grid():
    global state
    state = 'setting'
    game_window.reset_grid()


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = GameWindow(window, GAME_WIN_X, GAME_WIN_Y)
buttons = make_buttons()
state = 'setting'
frame_count = 0


running = True
while running:
    frame_count += 1
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
