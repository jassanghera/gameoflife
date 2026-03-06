from board import dead_state

# represent patterns as a list of live cell coordinates (row, col) relative to an origin (0,0)
PATTERNS = {
    # Classic 3x3 glider (moves diagonally)
    "glider": [
        (0, 1),
        (1, 2),
        (2, 0), (2, 1), (2, 2),
    ],
    # Simple oscillator (period 2)
    "blinker": [
        (0, 0), (0, 1), (0, 2),
    ],
    # Another oscillator (period 2)
    "toad": [
        (0,1), (0,2), (0,3),
        (1,0), (1,1), (1,2),
    ],
    # still life, doesnt change
    "block": [
        (0,0), (0,1),
        (1,0), (1,1)
    ],
}

def stamp_pattern(state, cells, top, left):
    """
    Turn on cells in 'state' at positions offset by (top, left), 
    ignoring any cells that would fall out of bounds (bounded board)
    """

    height = len(state)
    width = len(state[0])

    for dr, dc in cells:
        r = top + dr
        c = left + dc
        if 0 <= r < height and 0 <= c < width:
            state[r][c] = 1

def board_with_pattern(width, height, pattern_name):
    """Create a new board with a pattern centered on it."""
    state = dead_state(width, height)

    cells = PATTERNS.get(pattern_name)
    if cells is None:
        raise ValueError(f"Unknown pattern: {pattern_name}")

    # Calculate top-left corner to center the pattern
    max_r = max(r for r, _ in cells)
    max_c = max(c for _, c in cells)
    pattern_height = max_r + 1
    pattern_width = max_c + 1

    top = (height - pattern_height) // 2
    left = (width - pattern_width) // 2

    stamp_pattern(state, cells, top, left)
    return state

def pattern_names():
    return list(PATTERNS.keys())
