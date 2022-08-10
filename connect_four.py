def board(board_positions):
    column = 0
    row = 0
    print(f"""
    |  {board_positions[row][column]}   |  {board_positions[row][column+1]}    | {board_positions[row][column+2]}     | {board_positions[row][column+3]}     | {board_positions[row][column+4]}     | {board_positions[row][column+5]}     | {board_positions[row][column+6]}     |
    |      |       |       |       |       |       |       |
    {"="*57}

    |  {board_positions[row+1][column]}   |  {board_positions[row+1][column+1]}    | {board_positions[row+1][column+2]}     | {board_positions[row+1][column+3]}     | {board_positions[row+1][column+4]}     | {board_positions[row+1][column+5]}     | {board_positions[row+1][column+6]}     |
    |      |       |       |       |       |       |       |
    {"="*57}

    |  {board_positions[row+2][column]}   |  {board_positions[row+2][column+1]}    | {board_positions[row+2][column+2]}     | {board_positions[row+2][column+3]}     | {board_positions[row+2][column+4]}     | {board_positions[row+2][column+5]}     | {board_positions[row+2][column+6]}     |
    |      |       |       |       |       |       |       |
    {"="*57}

    |  {board_positions[row+3][column]}   |  {board_positions[row+3][column+1]}    | {board_positions[row+3][column+2]}     | {board_positions[row+3][column+3]}     | {board_positions[row+3][column+4]}     | {board_positions[row+3][column+5]}     | {board_positions[row+3][column+6]}     |
    |      |       |       |       |       |       |       |
    {"="*57}


    |  {board_positions[row+4][column]}   |  {board_positions[row+4][column+1]}    | {board_positions[row+4][column+2]}     | {board_positions[row+4][column+3]}     | {board_positions[row+4][column+4]}     | {board_positions[row+4][column+5]}     | {board_positions[row+4][column+6]}     |
    |      |       |       |       |       |       |       |
    {"="*57}

    |  {board_positions[row+5][column]}   |  {board_positions[row+5][column+1]}    | {board_positions[row+5][column+2]}     | {board_positions[row+5][column+3]}     | {board_positions[row+5][column+4]}     | {board_positions[row+5][column+5]}     | {board_positions[row+5][column+6]}     |
    |      |       |       |       |       |       |       |
    {"="*57}
    """)


#
# Start of Program
#
def main():
    board_positions = [
    [" ", " "," "," "," "," ", " "],
    [" ", " "," "," "," "," ", " "],
    [" ", " "," "," "," "," ", " "],
    [" ", " "," "," "," "," ", " "],
    [" ", " "," "," "," "," ", " "],
    [" ", " "," "," "," "," ", " "],
     
    ]

    # what players turn? Red or Blue
    players_turn = "R"

    # Play loop
    while True:
        # Swap player's turn
        if players_turn == "R":
            players_turn = "B"
        else:
            players_turn = "R"
        
        # add piece
        # pass the players turn into add_piece
        # ask for a specific color's piece 
        board_positions = add_piece(board_positions, players_turn)

        # check if anyone won
        winner = check_win(board_positions)

        # if winner = R, red player won. Congratulate player and end game
        if winner == "R":
            print("Red player has won!")
            print("Thanks for playing!")
            break
        # if winner = B, blue player won. Congratulate player and end game
        elif winner == "B":
            print("Blue player has won!")
            print("Thanks for playing!")
            break
        # if winner = N, no player won. Continue game
       
       
        # presents the board to the user
        board(board_positions)
    
   

# 
# Summary: This function will add a symbol to where the user wants to play.
#
# Parameters:
# - board_positions
# - players turn
#
# Return:
#   board_positions
#
def add_piece(board_positions, players_turn):
    # scope
    # if we create the variable outside the if block here
    # then we can use the variable anywhere in the function
    column_integer = ''

    # get input from the user
    # Let players know who's turn it is (R or B).
    if players_turn == "R":
        column_integer = int(input("Red player which column would you like to play? "))
        # only use the variable inside this if block
    elif players_turn == "B":
        column_integer = int(input("Blue player which column would you like to play? "))

    # next steps

    # call find_row function to get row
    # ...
    row_integer = find_row(column_integer - 1, board_positions)
    
    # place the correct symbol down to mark its placement.
    # update board_positons
    # ..
    board_positions[row_integer][column_integer - 1] = players_turn
    

    # return board positions
    return board_positions

#
# Summary: 
# This function will find out the bottom most empty spot in a certain column.
# Returns:
# row integer
#
def find_row(column_input,board_positions):
    # subtract column by 1
    #column_input -= 1

    # if bottom column is empty then just return bottom number
    if board_positions[5][column_input] == " ":
        # return bottom row
        return 5
    

    # find bottom most empty spot
    for row in range(6):
        if board_positions[row+1][column_input] != " ":
            print(f"returning row {row} because row{row+1} and column {column_input} was not equal to ' '")
            return row


#
# Summary:
# This function will check if any player has gotten four symbols together either horizontally, vertically, or diagonally. 
#
# Parameters:
# - board_positions
#
# Returns:
#   string (R, B, or N)
#
def check_win(board_positions):
    # Horizontal win?
    win_horizontal = check_win_horizontal(board_positions)
    win_vertical = check_win_vertical(board_positions)
    win_diagonal = check_win_diagonal(board_positions)
    if win_horizontal == "R" or win_horizontal == "B":
        return win_horizontal


    # Vertical win?
    elif win_vertical == "R" or win_vertical == "B":
        return win_vertical


    # Diagonal win?
    elif win_diagonal == "R" or win_diagonal == "B":
        return win_diagonal

    else:
        return "N"



# Summary:
# This function will check if any player has won horizontally
# Returns:
#   string (R, B, or N)
def check_win_horizontal(board_positions):
    return "N"


# Summary:
# This function will check if any player has won vertically
# Returns:
#   string (R, B, or N)
def check_win_vertical(board_positions):
    return "N"


# Summary:
# This function will check if any player has won diagonally
# Returns:
#   string (R, B, or N)
def check_win_diagonal(board_positions):
    return "N"

main()


