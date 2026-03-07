import pygame
from board import random_state
from next_state import next_board_state
from patterns import board_with_pattern, pattern_names

def draw_grid(screen, grid_width, grid_height, cell_size, header_height, sidebar_width):
    """draw grid lines"""

    GRID_COLOUR = (240, 240, 240)

    # vertical lines 
    for x in range(grid_width + 1):
        px = sidebar_width + x * cell_size
        pygame.draw.line(
            screen, 
            GRID_COLOUR,
            (px, header_height), 
            (px, header_height + grid_height * cell_size),
            1
        )    
    
    # horizontal lines
    for y in range(grid_height + 1):
        py = header_height + y * cell_size
        pygame.draw.line(
            screen,
            GRID_COLOUR,
            (0, py),
            (grid_width * cell_size, py),
            1
        )


def draw_state(screen, current_state, preview_state, cell_size, header_height, sidebar_width, dark_mode):
    """ loops over state[r][c] and draws a cell if it's alive or a faded cell if it will be alive next generation. """

    ALIVE_COLOUR = (64, 224, 208) # blue
    PREVIEW_COLOUR = (201, 255, 250)

    DARK_MODE_BACKGROUND = (60, 60, 60) # Grey
    DARK_MODE_PREVIEW = (110, 9, 125) # Dark Purple
    DARK_MODE_ALIVE = (207,79,227) # Purple

    LIGHT_MODE_BACKGROUND = (255, 255, 255)
    LIGHT_MODE_PREVIEW = (201, 255, 250)
    LIGHT_MODE_ALIVE = (64, 224, 208)

    if dark_mode:
        ALIVE_COLOUR = DARK_MODE_ALIVE
        PREVIEW_COLOUR = DARK_MODE_PREVIEW
        BACKGROUND = DARK_MODE_BACKGROUND
    else:
         ALIVE_COLOUR = LIGHT_MODE_ALIVE
         PREVIEW_COLOUR = LIGHT_MODE_PREVIEW
         BACKGROUND = LIGHT_MODE_BACKGROUND
    
    # screen.fill((255, 255, 255)) # fill the screen with white
    screen.fill(BACKGROUND) # fill screen with black

    for r, row in enumerate(current_state):
        for c, cell in enumerate(row):
            x = sidebar_width + c * cell_size
            y = header_height + r * cell_size
            rect = pygame.Rect(
                x, 
                y, 
                cell_size - 1, 
                cell_size - 1
            )

            if cell == 1:
                # draw a white square at the appropriate position
                pygame.draw.rect(screen, ALIVE_COLOUR, rect)
            
            elif preview_state[r][c] == 1:
                # draw a faded preview of the next live cell
                pygame.draw.rect(screen, PREVIEW_COLOUR, rect)
    
    

def draw_text(screen, font, pattern_name, running, generation): 
    """Draw status text at top of window."""

    status = "Running" if running else "Paused"
    text = (180, 180, 180)
    x = 10
    y = 50
    line_spacing = 30

    side_bar_text = [ # instructions for user 
        f"Controls:",
        f"Space = Run/Pause",
        f"Right = Step",
        f"R = Reset",
        f"0-4 = Pattern",
        f"Esc = Quit",
        f"D = Toggle Dark Mode"
    ]

    header_line = f"Pattern: {pattern_name} | Status: {status} | Generation: {generation}"

    text1 = font.render(header_line, True, (180, 180, 180))

    screen.blit(text1, (10, 10))

    for i in side_bar_text: # render each line of sidebar text and blit to screen
        line = font.render(i, True, text)
        screen.blit(line, (x, y))
        y += line_spacing


def main():

    pygame.init()

    # grid settings
    grid_width = 60 # grid_w, grid_h (cells)
    grid_height = 60
    cell_size = 10  # cell_size (pixels per cell)
    header_height = 40
    sidebar_width = 200

    window_width = sidebar_width + grid_width * cell_size
    window_height = header_height + grid_height * cell_size

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # simulation settings
    running = False
    step_ms = 100 # time between generations when running (ms)
    last_step_time = 0
    generation = 0
    dark_mode = False

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
                if event.key == pygame.K_ESCAPE:
                    done = True

                elif event.key == pygame.K_SPACE:
                    running = not running # toggle run/pause

                elif event.key == pygame.K_d:
                    dark_mode = not dark_mode

                elif event.key == pygame.K_RIGHT:
                    state = next_board_state(state) # step forward one gen
                    generation += 1

                elif event.key == pygame.K_r:
                    generation = 0
                    last_step_time = pygame.time.get_ticks()
                    if pattern_name == "random":
                        state = random_state(grid_width, grid_height, p_alive=0.30) # reset to new random board
                    else:
                        state = board_with_pattern(grid_width, grid_height, pattern_name) # reset to original pattern

                elif event.key == pygame.K_0:
                    pattern_name = "random"
                    generation = 0
                    last_step_time = pygame.time.get_ticks()
                    state = random_state(grid_width, grid_height, p_alive=0.3)

                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    index = event.key - pygame.K_1
                    pattern_name = pattern_names()[index]
                    generation = 0
                    last_step_time = pygame.time.get_ticks()
                    state = board_with_pattern(grid_width, grid_height, pattern_name)
        
        # update state if running and enough time has passed
        if running and now - last_step_time >= step_ms:
            state = next_board_state(state)
            generation += 1
            last_step_time = now

        # preview next state
        preview_state = next_board_state(state)
        
        # draw current state
        draw_state(screen, state, preview_state, cell_size, header_height, sidebar_width, dark_mode)
        # draw_grid(screen, grid_width, grid_height, cell_size, header_height)
        draw_text(screen, font, pattern_name, running, generation)
        pygame.display.flip() # update the display

        # cap event loop to 60 fps
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
                