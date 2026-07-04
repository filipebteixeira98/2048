import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("comicsans", 60, bold=True)

MOVE_VELOCITY = 20

pygame.display.set_caption("2048")

def main(window) -> None:
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                break
    
    pygame.quit()


if __name__ == "__main__":
    main(WINDOW)
