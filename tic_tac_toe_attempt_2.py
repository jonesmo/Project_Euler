# -*- coding: utf-8 -*-
"""tic_tac_toe_attempt_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qKXTzrGw341dPSGIqC-haXDUxF30O3KF
"""

#display a Tic Tac Toe board
#the """ notation allows all the spacing to be preserved as part of the string

def display_board(board):
  blankBoard = """
  ________________
  |    |    |    |
  |  7 |  8 |  9 |
  ________________
  |    |    |    |
  |  4 |  5 |  6 |
  ________________
  |    |    |    |
  |  1 |  2 |  3 |
  ________________
  """

  print('________________')
  print('|    |    |    |')
  print('|  {} |  {} |  {} |'.format(board[7], board[8], board[9]))
  print('________________')
  print('|    |    |    |')
  print('|  {} |  {} |  {} |'.format(board[4], board[5], board[6]))
  print('________________')
  print('|    |    |    |')
  print('|  {} |  {} |  {} |'.format(board[1], board[2], board[3]))
  print('________________')

  for i in range(1,10):
    if board[i] == 'O' or board[i] == 'X':
      blankBoard = blankBoard.replace(str(i), board[i])
    else:
      blankBoard = blankBoard.replace(str(i), ' ')

#ask player if they want X or O, include lower case

def player_input():
  player1 = input('Please pick a marker, X or O: ')
  while True:
    if player1.upper() == 'X':
      player1 = 'X'
      player2 = 'O'
      print('You\'ve chosen ' + player1 + '. Player 2 will be ' + player2)
      players = [player1, player2]
      return players
    elif player1.upper() == 'O':
      player1 = 'O'
      player2 = 'X'
      print('You\'ve chosen' + player1 + '. Player 2 will be ' + player2)
      return player1, player2
    else:
      player1 = input('Error. Please pick a marker, X or O')

#place marker on board

def place_marker(board, marker, position):
  board[position] = marker
  return board

#check to see if space is empty
def space_check(board, position):
  return type(board[position]) == int

#ask player for choice of position
def player_choice(board):
  choice = input('Please select an empty space between 1 and 9: ')
  
  while not space_check(board, int(choice)):
    choice = input('This space isn\'t free. Please choose an empty space between 1 and 9: ')
  
  return choice

#is the board full?
def full_board_check(board):
  return len([x for x in board if x == '#']) == 1

#check for win
def win_check(board, mark):
  if board[1] == board[2] == board[3] == mark:
      return True
  if board[4] == board[5] == board[6] == mark:
      return True
  if board[7] == board[8] == board[9] == mark:
      return True
  if board[1] == board[4] == board[7] == mark:
      return True
  if board[2] == board[5] == board[8] == mark:
      return True
  if board[3] == board[6] == board[9] == mark:
      return True
  if board[1] == board[5] == board[9] == mark:
      return True
  if board[3] == board[5] == board[7] == mark:
      return True
  return False

#ask if they want to play again
def replay():
  playAgain = input('Do you want to play again (y/n)?')

  if playAgain.lower() == 'y':
    return True
  if playAgain.lower() == 'n':
    return False

"""Now put it all together"""

if __name__ == "__main__":
  print('Welcome to Tic Tac Toe!')

  i=1

  #Choose your player
  players = player_input()

  #initialize empty board
  board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  display_board(board)

  while True:
    game_on = full_board_check(board)

    while not game_on:
      #player chooses position
      position = player_choice(board)

      #select which marker is getting placed
      if i % 2 == 0:
        marker = players[1]
      else:
        marker = players[0]
      
      #place marker!
      place_marker(board, marker, int(position))

      #check the board
      display_board(board)
      
      i += 1

      if win_check(board, marker):
        print('You won!!')
        break
      
      game_on = full_board_check(board)

    if not replay():
      break
    
    else:
      i = 1

      players = player_input()

      board = ['#'] * 10