from time import sleep
from random import randint
import pygame
import keyboard

pygame.init()
width = 1280
height = 960
screen = pygame.display.set_mode((width, height), flags=pygame.FULLSCREEN)
black = (0, 0, 0)
white = (255, 255, 255)
screen.fill(black)
size = 4


def create_grid(x, y):
    grid = [[0 for i in range(x)] for j in range(y)]
    return grid


def change_cardinal(current, color, x, y):
    # change cardinal dir clockwise
    if color == white:
        switcher = {
            1: x + 1,  # NORTH
            2: y + 1,  # EAST
            3: x - 1,  # SOUTH
            4: y - 1   # WEST
        }
        return switcher[current]

    # change cardinal dir anti-clockwise
    else:
        switcher = {
            1: x - 1,  # NORTH
            2: y - 1,  # EAST
            3: x + 1,  # SOUTH
            4: y + 1   # WEST
        }
        return switcher[current]


def draw_circle(x, y, color):
    x *= size
    y *= size
    center = ((x + (size // 2)), (y + (size // 2)))
    pygame.draw.circle(screen, color, center, size // 2)


def main():
    cardinal_dir = 1
    xlen = width // size
    ylen = height // size
    x = xlen // 2
    y = ylen // 2
    grid = create_grid(xlen, ylen)

    while True:

        # press Q to exit program
        if keyboard.is_pressed('q'):
            pygame.quit()
            exit()

        # runs if value is 1 (circle is white)
        if grid[x][y]:

            # change value in grid from 1 -> 0
            grid[x][y] = 0
            draw_circle(x, y, black)

            # change cardinal direction of the ant
            if cardinal_dir == 1 or cardinal_dir == 3:
                x = change_cardinal(cardinal_dir, white, x, y)
            else:
                y = change_cardinal(cardinal_dir, white, x, y)

            # checks if var is not overflowing
            if cardinal_dir < 4:
                cardinal_dir += 1
            else:
                cardinal_dir = 1

        # runs if value is 0 (circle is black)
        else:

            # change value in grid from 0 -> 1
            grid[x][y] = 1

            # draw white circle
            draw_circle(x, y, white)

            # change cardinal direction of the ant
            if cardinal_dir == 1 or cardinal_dir == 3:
                x = change_cardinal(cardinal_dir, black, x, y)
            else:
                y = change_cardinal(cardinal_dir, black, x, y)

            # checks if var is not overflowing
            if cardinal_dir > 1:
                cardinal_dir -= 1
            else:
                cardinal_dir = 4

        # updates screen
        pygame.display.flip()
        # sleep(0.0001)


# running main program
if __name__ == '__main__':
    main()
