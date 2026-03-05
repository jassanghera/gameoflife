
# -----------------------------------------------------------------------------
# UNIT TESTS
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    # TEST 1: dead cells with no live neighbours should stay dead
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        print("FAILED 1")
        print("Expected: ")
        print(expected_next_state1)
        print("Actual:")
        print(actual_next_state1)

    
    # TEST 2: dead cells with exactly 3 neighbours should come alive
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print("Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)
    
    # TEST 3: dead cells with less than 3 neighbours stay dead, 
    # live cells with less than 2 neighbours die
    init_state3 = [
        [1,0,0],
        [0,1,0],
        [0,0,0]
    ]
    expected_next_state3 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state3 = next_board_state(init_state3)

    if expected_next_state3 == actual_next_state3:
        print("PASSED 3")
    else:
        print("FAILED 3!")
        print("Expected:")
        print(expected_next_state3)
        print("Actual:")
        print(actual_next_state3)

    # TEST 4: live cells with 2 or 3 neighbours continue to live 
    init_state4 = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    expected_next_state4 = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    actual_next_state4 = next_board_state(init_state4)

    if expected_next_state4 == actual_next_state4:
        print("PASSED 4")
    else:
        print("FAILED 4!")
        print("Expected:")
        print(expected_next_state4)
        print("Actual:")
        print(actual_next_state4)

    # TEST 5: live cells with 24 or more neighbours die 
    init_state5 = [
        [1,1,0],
        [1,1,0],
        [1,0,0]
    ]
    expected_next_state5 = [
        [1,1,0],
        [0,0,0],
        [1,1,0]
    ]
    actual_next_state5 = next_board_state(init_state5)

    if expected_next_state5 == actual_next_state5:
        print("PASSED 5")
    else:
        print("FAILED 5!")
        print("Expected:")
        print(expected_next_state5)
        print("Actual:")
        print(actual_next_state5)