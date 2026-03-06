import pygame
from board import dead_state, random_state
from next_state import next_board_state
from patterns import board_with_pattern, pattern_names

def draw_state(screen, state, cell_size):
    """ loops over state[r][c] and draws a cell if it's alive, otherwise leaves it blank. """
    screen.fill((0, 0, 0)) # fill the screen with black

    for r, row in enumerate(state):
        for c, cell in enumerate(row):
            if cell == 1:
                # draw a white square at the appropriate position
                rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect)

def main():

    pygame.init()

    # grid settings
    grid_width = 60 # grid_w, grid_h (cells)
    grid_height = 60
    cell_size = 10  # cell_size (pixels per cell)

    window_width = grid_width * cell_size
    window_height = grid_height * cell_size

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    # simulation settings
    running = False
    step_ms = 100 # time between generations when running (ms)
    last_step_time = 0
    generation = 0

    pattern_name = "random" # default
    state = random_state(grid_width, grid_height, p_alive=0.3)

    # main loop
    done = False
    while not done:
        now = pygame.time.get_ticks()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running # toggle run/pause

                elif event.key == pygame.K_RIGHT:
                    state = next_board_state(state) # step forward one gen while paused
                    generation += 1

                elif event.key == pygame.K_r:
                    generation = 0
                    if pattern_name == "random":
                        state = random_state(grid_width, grid_height, p_alive=0.30) # reset to new random board
                    else:
                        state = board_with_pattern(grid_width, grid_height, pattern_name) # reset to original pattern

                elif event.key == pygame.K_0:
                    pattern_name = "random"
                    generation = 0
                    state = random_state(grid_width, grid_height, p_alive=0.3)

                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    index = event.key - pygame.K_1
                    pattern_name = pattern_names()[index]
                    generation = 0
                    state = board_with_pattern(grid_width, grid_height, pattern_name)
        
        # update state if running and enough time has passed
        if running and now - last_step_time >= step_ms:
            state = next_board_state(state)
            generation += 1
            last_step_time = now

        # draw current state
        draw_state(screen, state, cell_size)
        pygame.display.flip()

        # cap event loop to 60 fps
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
                














    screen.fill((0, 0, 0)) # fill the screen with black
    
    font = pygame.font.SysFont('Times New Roman', 30)
    text = font.render('Hello, World!', True, (255, 255, 255))

    screen.blit(text, (200, 100))   # draw the text at position (200, 100)
    pygame.display.flip()

