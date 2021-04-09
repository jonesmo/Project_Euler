# -*- coding: utf-8 -*-
"""connect_four.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19kn27qF_2VUoxyCga6I3xAMPK3v26VeO
"""

import random

"""##Connect Four

1. Write an application that holds board state. It should render the board state visually in a 6 x 7 grid. It should represent tokens for a "red" player and a "black" player. Your application should represent empty spaces as visually distinct from player tokens, but it's your choice how these tokens look.
"""

def draw_board(board):

  print('____________________________________')
  print('| {}  | {}  | {}  | {}  | {}  | {}  | {}  |'.format(board[35], board[36], board[37], board[38], board[39], board[40], board[41]))
  print('____________________________________')
  print('| {}  | {}  | {}  | {}  | {}  | {}  | {}  |'.format(board[28], board[29], board[30], board[31], board[32], board[33], board[34]))
  print('____________________________________')
  print('| {}  | {}  | {}  | {}  | {}  | {}  | {}  |'.format(board[21], board[22], board[23], board[24], board[25], board[26], board[27]))
  print('____________________________________')
  print('| {}  | {}  | {}  | {}  | {}  | {}  | {}  |'.format(board[14], board[15], board[16], board[17], board[18], board[19], board[20]))
  print('____________________________________')
  print('| {}  | {}  | {}  | {}  | {}  | {}  | {}  |'.format(board[7], board[8], board[9], board[10], board[11], board[12], board[13]))
  print('____________________________________')
  print('| {}  | {}  | {}  | {}  | {}  | {}  | {}  |'.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6]))
  print('____________________________________')
  print('| 1  | 2  | 3  | 4  | 5  | 6  | 7  |')

board = ['#'] * 42

draw_board(board)

"""2. Add functionality that accepts user input to drop a token into a specified column. The token should take the last available cell within a particular column."""

#check if column is full
def full_column_check(column):
  empty = '#'

  if empty in column:
    return False
  else:
    return True

#function to identify lowest available space in a column
col1_list = [0, 7, 14, 21, 28, 35]
col2_list = [1, 8, 15, 22, 29, 36]
col3_list = [2, 9, 16, 23, 30, 37]
col4_list = [3, 10, 17, 24, 31, 38]
col5_list = [4, 11, 18, 25, 32, 39]
col6_list = [5, 12, 19, 26, 33, 40]
col7_list = [6, 13, 20, 27, 34, 41]

all_cols = [col1_list, col2_list, col3_list, col4_list, col5_list, col6_list, col7_list]


def find_lowest(column_number):

  column_index = int(column_number) - 1
  current_column = all_cols[column_index]
  subset_of_board = []

  for j in current_column:
    current_term = board[j]
    subset_of_board.append(current_term)

  is_full = full_column_check(subset_of_board)
  
  if is_full is True:
    print('Column is full.  Please select a different column: ')
    return -1

  else:
    for i in current_column:
      if board[i] == '#':
        return i

#user input for column
def user_input(board):
  while True:
    user_selection = input('Please select a column, 1 through 7: ')

  #while True:
    space = find_lowest(user_selection)

    if space >= 0:
      board[space] = 'R'
      return True
      break
    else:
      # return False
      # break
      continue

user_input(board)

draw_board(board)

"""3. Write a function to check if the board is full."""

def full_board_check(board):
  empty = '#'

  if empty in board:
    return False
  else:
    return True

"""4. Add a rudimentary AI that will make the simplest, valid move possible. Your AI should not do anything if the board is full."""

def AI_move(board):
  is_full = full_board_check(board)

  if is_full:
    print('No more moves!')

  while True:
    AI_column_selection = random.randint(1,7)

    AI_space = find_lowest(AI_column_selection)

    if AI_space >= 0:
      board[AI_space] = 'B'
      break
    else:
      continue

AI_move(board)

draw_board(board)

"""##Assembling it into a game, no win check"""

print('Let\'s Play Connect Four!')

i = 1

board = ['#'] * 42

draw_board(board)

while True:
  board_full = full_board_check(board)

  if board_full:
    print('The board is full!  No more moves.')
    break
  
  while not board_full:
    if i % 2 == 0:
      AI_move(board)
      draw_board(board)
    else:
      user_input(board)

    i += 1

"""##Add win check"""

def four_identical(array):
  for item in array:
    if item < len(array) - 3:
      if (array[item] == array[item + 1] == array[item + 2] == array[item + 3]) and (array[item] == 'R') or (array[item] == 'B'):
        return array[item]
        print(array[item] + ' wins!!')

def win_check(board):
  #four horizontally
  row1 = list(range(0,7))
  row2 = list(range(7, 14))
  row3 = list(range(14, 21))
  row4 = list(range(21, 28))
  row5 = list(range(28, 35))
  row6 = list(range(35, 42))

  all_rows = [row1, row2, row3, row4, row5, row6]

  for row in all_rows:
    four_identical(row)

  #four vertically
  for column in all_cols:
    four_identical(column)

  #four diagonally
  diag1 = [14, 8, 2, 4]
  diag2 = [21, 15, 9, 3, 5]
  diag3 = [28, 22, 16, 10, 4, 6]
  diag4 = [35, 29, 23, 17, 11, 5]
  diag5 = [36, 30, 24, 18, 12]
  diag6 = [37, 31, 25, 19, 13]
  diag7 = [38, 32, 26, 20]
  diag8 = [38, 30, 22, 14]
  diag9 = [39, 31, 23, 15, 7]
  diag10 = [40, 32, 24, 16, 8, 0]
  diag11 = [41, 33, 25, 17, 9, 1]
  diag12 = [34, 26, 18, 10, 2]
  diag13 = [27, 19, 11, 3]

  all_diags = [diag1, diag2, diag3, diag4, diag5, diag6, diag7, diag8, diag9, diag10, diag11, diag12, diag13]

  for diagonal in all_diags:
    four_identical(diagonal)



print('Let\'s Play Connect Four!')

i = 1

board = ['#'] * 42

draw_board(board)

while True:
  board_full = full_board_check(board)

  if board_full:
    print('The board is full!  No more moves.')
    break
  
  while not board_full:
    if i % 2 == 0:
      AI_move(board)
      win_check(board)
      draw_board(board)
    else:
      user_input(board)
      win_check(board)

    i += 1