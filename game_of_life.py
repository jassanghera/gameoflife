import time
import os
import next_state as ns
from board import random_state, render
from next_state import next_board_state
from patterns import board_with_pattern, pattern_names

# -----------------------------------------------------------------------------
# Game of Life
# -----------------------------------------------------------------------------

# runs infinite loop of states, printing each iteration
def life(current_state):

    generation = 0

    try: 
        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"Generation: {generation}\n")
            render(current_state)

            current_state = ns.next_board_state(current_state)
            generation += 1

            time.sleep(0.05)

    except KeyboardInterrupt:
        print(f"Game stopped at iteration {generation}.")
        print("Thanks for playing Conway's Game of Life!\n")
        

# -----------------------------------------------------------------------------
# Pattern Loader from user input
# -----------------------------------------------------------------------------


def choose_pattern():
    options = ["random"] + pattern_names()
    print("Choose a starting configuration:")
    for i, name in enumerate(options, start=1):
        print(f'{i}. {name}')
    
    choice = input("Enter the number of your choice (or press Enter for random board): ").strip()

    if choice == "":
        return "random"  # default pattern
    
    if choice.isdigit():
        index = int(choice)
        if 1 <= index <= len(options):
            return options[index - 1]
        
    print("Invalid choice, defaulting to random.")
    return "random"

def make_initial_state(width, height, selection):
    if selection == "random":
        return random_state(width, height)
    return board_with_pattern(width, height, selection)

# -----------------------------------------------------------------------------
# main function
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    width, height = 25, 25

    selection = choose_pattern()
    state = make_initial_state(width, height, selection)

    life(state)