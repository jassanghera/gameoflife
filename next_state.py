NEIGHBOR_OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def next_board_state(state):
    
    height = len(state)
    width = len(state[0])

    new_state = [[0] * width for _ in range(height)]

    for r in range(height):
        for c in range(width):
            # count live neighbours
            neighbours = 0
            for dr, dc in NEIGHBOR_OFFSETS:
                rr = r + dr # add "% height" to wrap around edges
                cc = c + dc # add "% width" to wrap around edges
                if 0 <= rr < height and 0 <= cc < width:
                    neighbours += state[rr][cc]
            
            # Conway's rules
            if state[r][c] == 1:                                        # live cell
                new_state[r][c] = 1 if neighbours in (2, 3) else 0
            else:                                                       # dead cell
                new_state[r][c] = 1 if neighbours == 3 else 0
    
    return new_state


# next_board_state([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])


# Conway's Game of Life rules:
    # 1. Underpopulation: live cell with <2 neighbours dies
    # 2. Overpopulation: live cell with >3 neighbours dies
    # 3. Survival: live cell with 2 or 3 neighbours lives on
    # 4. Reproduction: dead cell with exactly 3 neighbours becomes alive

