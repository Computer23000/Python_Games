import numpy as np
import pygame
import sys
import math

# colors used for board and pieces
blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
orange=(255,165,0)

# define function to check if row count and column count is valid
def string_to_int(user_input, prompt):
    while True:
        if user_input.isdigit():
            user_input = int(user_input)
            return user_input
        else:
            user_input = input(prompt)

#creating the board
# its a 2D array, or lists inside of lists
def create_board():
    '''Creates lists inside of lists to create the board.'''
    board = np.zeros((row_count,column_count))
    return board

# where to drop piece
def drop_piece(board, row, col, piece):
    '''Puts the piece somewhere.'''
    board[row][col] = piece

# if piece to dropped at valid place
def is_valid_location(board, col):
    '''Returns true or false depending on if that particular column is available.'''
    return board[row_count-1][col] == 0

# place piece in next row
def get_next_open_row(board, col):
    '''Finds the next open row.'''
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    '''Prints the board with indexes for the lists in reverse.'''
    print(np.flip(board, 0))

def winning_move(board, piece):
    '''Checks if a player wins.'''
    # check horizontal locations
    for c in range(column_count-3):
        for r in range (row_count):
            if board[r][c] == piece and board [r][c+1] == piece and board[r][c+2] == piece and board [r][c+3] == piece:
                return True

    # check vertical locations
    for c in range(column_count):
        for r in range (row_count-3):
            if board[r][c] == piece and board [r+1][c] == piece and board[r+2][c] == piece and board [r+3][c] == piece:
                return True

    # check positively sloped diagonals
    for c in range(column_count-3):
        for r in range (row_count-3):
            if board[r][c] == piece and board [r+1][c+1] == piece and board[r+2][c+2] == piece and board [r+3][c+3] == piece:
                return True

    # check negatively sloped diagonals
    for c in range(column_count-3):
        for r in range (3, row_count):
            if board[r][c] == piece and board [r-1][c+1] == piece and board[r-2][c+2] == piece and board [r-3][c+3] == piece:
                return True

def tie(board, game_over):
    '''Sees if there is a tie.'''
    for c in range(column_count):
        if board[row_count-1][c] == 0:
            return game_over
    game_over = True
    return game_over

#drawing the board pygame
def draw_board(board):
    '''Draws the board with pieces.'''
    # draws blue squares and black circles
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c*squaresize, r*squaresize+squaresize, squaresize, squaresize))
            pygame.draw.circle(screen, black, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)),radius)

    # fills in the pieces
    for c in range(column_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*squaresize+squaresize/2), height-int(r*squaresize+squaresize/2)),radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(c*squaresize+squaresize/2), height-int(r*squaresize+squaresize/2)),radius)

    pygame.display.update()

### Main Program ###

# number of rows
row_count = input("How many rows do you want to play with?")
# check if user input is valid
prompt = "How many rows do you want to play with?"
row_count = string_to_int(row_count, prompt)
# check if the board is the right size
while True:
    if row_count <= 4:
        print('You need more than four rows.')
        row_count = input(prompt)
        row_count = string_to_int(row_count, prompt)
    elif row_count > 18:
        print('You put too many rows.')
        row_count = input(prompt)
        row_count = string_to_int(row_count, prompt)
    else: break

# number of columns
column_count= input("How many columns do you want to play with?")
# check if user input is valid
prompt = "How many columns do you want to play with?"
column_count = string_to_int(column_count, prompt)
#check is the board is the right size
while True:
    if column_count <= 4:
        print('You need more than four columns.')
        column_count = input(prompt)
        column_count = string_to_int(column_count, prompt)
    elif column_count > 25:
        print('You put too many columns.')
        column_count = input(prompt)
        column_count = string_to_int(column_count, prompt)
    else: break

board = create_board()
game_over = False
turn=0

#running pygame
pygame.init()
squaresize=50
width = column_count * squaresize
height = (row_count + 1) * squaresize
size = (width, height)
radius=int(squaresize/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("comicsans", squaresize)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0,0,width,squaresize))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(squaresize/2)), radius)
            else:
                pygame.draw.circle(screen, yellow, (posx, int(squaresize/2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0,0,width,squaresize))
            # print(event.pos)
            # asking player 1 input
            if turn == 0:
                posx=event.pos[0]
                col = int(math.floor(posx/squaresize))

                # check if piece is in valid location
                if is_valid_location (board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    # check if player 1 wins
                    if winning_move(board, 1):
                        print_board(board)
                        label = myfont.render("Player 1 wins!", 1, red)
                        screen.blit(label, (40, 10))
                        game_over = True
                # if its not valid location, try again
                else:
                    game_over = tie(board, game_over)
                    if game_over == True:
                        label = myfont.render("It's a tie!", 1, orange)
                        screen.blit(label, (40,10))


            # asking player 2 input
            else:
                posx=event.pos[0]
                col = int(math.floor(posx/squaresize))

                if is_valid_location (board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        print_board(board)
                        label = myfont.render("Player 2 wins!", 1, yellow)
                        screen.blit(label, (40, 10))
                        game_over = True
                else:
                    game_over = tie(board, game_over)
                    if game_over == True:
                        label = myfont.render("It's a tie!", 1, orange)
                        screen.blit(label, (40,10))

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
