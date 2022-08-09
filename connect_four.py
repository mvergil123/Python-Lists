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

def main():
    board_positions = [
    ["R", " "," "," "," ","B", " "],
    [" ", "R"," "," "," "," ", " "],
    [" ", " "," ","B"," "," ", " "],
    ["B", "R"," "," "," "," ", " "],
    [" ", " "," "," "," ","R", "B"],
    [" ", " ","R"," "," "," ", " "],
     
    ]
    board(board_positions)

def add_piece(board_positions):
    user_input = int(input("Which column would you like to play? "))

def find_bottom_column(column,board_positions):
    for row in range(6):
        for column in range(7):
            if board_positions[row+1][column] != " ":
                return row
main()