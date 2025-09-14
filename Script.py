import pandas as pd
import random
import numpy as np


lotto_numbers = list(range(1, 50))
numbers_per_boards = 5  # Example range for lottery numbers

def dataProcessing():
 pass





def analyzePatterns():
 pass




def generatePredictions():
 pass




def results():
 pass

#--------
# Logic for quick pick section
#--------

# Boards and Draws validation
def number_of_boards(boards_per_play = 1):
 #One set of chosen numbers and how many set of number are played
  print('How many boards/lines would you like to play? (1-5): \n')

  if boards_per_play < 1:
   raise ValueError("You play atleast one board")
  else:
   return boards_per_play

def number_of_draws(draws: int = None):

  if draws is None:
    draws = int(input("Enter the number of draws you want to enter, 1 - 5 : \n"))
  if draws < 1:
    raise ValueError("You must play atleast 1 draw")
  return draws

def generate_quick_picks(boards: IndentationError):
    # returns a list of the draws and boards played by user in a list
    generate_boards = []
    boards = validate_boards(boards)

    for _ in range(boards):
        board = random.sample(range(lotto_numbers[0], lotto_numbers[1] + 1), numbers_per_boards)
        board.sort()
        generate_boards.append(board)
    
    return generate_boards
 

# now we compare the users numbers based on the quick pick or winning numbers
def compare_winning_numbers(user_boards, winning_numbers = None):
  if winning_numbers is None:
    winning_numbers = sorted(random.sample(lotto_numbers[0], lotto_numbers[1] + 1), numbers_per_boards)

  results = []
  for board in user_boards:
    matches = [num for num in board if num in winning_numbers]
    results.append({
      "board": board,
      "matches": matches,
      "match_count": len(matches),
      "win": board == winning_numbers
    })

  return {"winning numbers": winning_numbers, "results": results}