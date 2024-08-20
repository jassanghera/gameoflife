print("hello life")

# dead_state should accept integer width and height
    #output: 2D grid as list of lists
def dead_state(width, height):

    dead_board = []

    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        dead_board.append(row)


    return dead_board


print(dead_state(4,5))



