import random

board = [i for i in range(0, 9)]  # Itertaions to print 9 boxes of the board
player, computer = '', ''

moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))  # Corners, Center and Others, respectively

winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
           (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # Winner combinations on the board

tab = range(1, 10)  # Table range that can be entered


def print_board():  # Function to print the game board
    x = 1  # Variable
    for i in board:  # Iterations to display the move after selecting
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1: end += '---------\n';
        char = ' '
        if i in ('X', 'O'): char = i;
        x += 1
        print(char, end=end)


def select_char():  # Function to select character among two
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, move):  # Function to check the place for move is empty or not
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


def can_win(brd, player):  # To check if the player Wins
    places = []
    x = 0
    for i in brd:
        if i == player: places.append(x);
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


def make_move(brd, player, move, undo=False):  # Function to make a move by player
    if can_move(brd, move):
        brd[move - 1] = player
        win = can_win(brd, player)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


def computer_move():    # Function for Computer move
    move = -1   # If I can win, others don't matter.
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            move = i
            break
    if move == -1:      # If player can win, block him.
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                move = i
                break
    if move == -1:      # Otherwise, try to take move on one of desired places
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, mv):
                    move = mv
                    break
    return make_move(board, computer, move)


def space_exist():      # To check the availability of space in board
    return board.count('X') + board.count('O') != 9


player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result = '%%% Deuce ! %%%'

while space_exist():        # Condition holds good till the space exists in the board
    print_board()
    print('# Make your move ! [1-9] : ', end='')        # Read User Input
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid number. Please, Try again !")    # Check if entered input is wrong
        continue
    if won:     # Check if player won
        result = '----- Congratulations, You won ! -----'       # Print result
        break
    elif computer_move()[1]:        # Check if computer won
        result = '==== You lost the GAME! ==='        # Print result
        break

print_board()  # Function calling to print the board
print(result)       # To print final result
print("-----Thank You------")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~End of program~~~~~~~~~~~~~~~~~~~~~~~~~~~")








####------GAME FOR TWO PERSONS---------####

# theBoard = {'7': ' ', '8': ' ', '9': ' ',
#             '4': ' ', '5': ' ', '6': ' ',
#             '1': ' ', '2': ' ', '3': ' '}       # Structure of the board
#
# board_keys = []     # Method to add the particular key after user input
# for key in theBoard:
#     board_keys.append(key)
#
#
# def printBoard(board):      # Function to print on the plane with keys
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])
#
#
# def game():     # Defining function to perform all gameplay actions
#     turn = 'X'      # Variables
#     count = 0
#
#     for i in range(10):     # Iterating
#         printBoard(theBoard)        # Function calling to print the bord on console
#         print("It's your turn,", turn, ". Select the place to move(1-9): \n")     # Reading User Input
#         move = input()
#         if theBoard[move] == ' ':       # To check if the place is already occupied or not
#             theBoard[move] = turn       # To print the place selected by the user
#             count += 1      # Incrementing counter
#         else:
#             print("That place is already filled.\n Select the place to move(1-9): \n")        # Reading User Input
#             continue
#
#         if count >= 5:      # Iterations to check if player X or O has won for each move 5th move
#             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # To check pattern across the top
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # To check pattern across the middle
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # To check pattern across the bottom
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # To check pattern down the left side
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # To check pattern down the middle
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # To check pattern down the right side
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # To check pattern across diagonal
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # To check pattern across another diagonal
#                 printBoard(theBoard)        # Function calling to print the current filled board
#                 print("\n-----Game Over!!-----\n")
#                 print(" **** ", turn, " won. ****")     # printing the result
#                 break
#
#         if count == 9:      # If Both X and O doesn't win, and the board is full
#             print("\n-----Game Over!!-----\n")
#             print("It's a Tie!!")       # printing the result
#
#         if turn == 'X':     # To change the player name after the game
#             turn = 'O'
#         else:
#             turn = 'X'
#
#     restart = input("Do you want to play the game Again?(y/n)")  # Asking the player to restart the game again
#     if restart == "y" or restart == "Y":  # checking for the condition for yes or no
#         for key in board_keys:
#             theBoard[key] = " "  # if yes, then start the game again
#         game()  # Calling the game function again
#     else:
#         print("-----Thank you-----")
#
#
# if __name__ == "__main__":      # Main method to start the game
#     game()      # Calling the game function to start the game
#
# print("----End of Program-----")
