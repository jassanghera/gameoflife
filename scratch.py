# ROUGH WORK

def render(state):

    for i in range(len(state)):
        print(*state[i])
    print("\n")

def dead_state(width, height):

    dead_board = []

    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        dead_board.append(row)

    return dead_board



def random_state(width, height):

    state = dead_state(width, height)

    for i in range(height):
        for j in range(width):

            random_number = random.random()

            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            
            state[i][j] = cell_state
    
    return state



def next_board_state(state):

    height = len(state)
    width = len(state[0])

    new_state = dead_state(width, height)

    for i in range(height):
        for j in range(width):

            msg = " "
            neighbour_count = 0


            if i == 0 and j == 0:
                for x in range(j,j+2):
                    for y in range(i,i+2):
                        if state[y][x] == 1:
                            neighbour_count += 1
            
            if neighbour_count > 0:
                neighbour_count -= 1
                            

            print("Cell " + "(", i, ",", j, ")" + ": ", neighbour_count)





test = [[1,0],
        [0,1]]

print("STATE: ")
render(test)
print("NEIGHBOUR COUNT: ")
next_board_state(test)


