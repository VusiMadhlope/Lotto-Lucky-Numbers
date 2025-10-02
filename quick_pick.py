#--------
# Logic for quick pick section
#--------
lotto_min = 1
lotto_max = 50
numbers_per_boards = 5  # Example range for lottery numbers


# Boards and Draws validation
def number_of_boards(boards_per_play = 1):
 #One set of chosen numbers and how many set of number are played
  if boards_per_play < 1:
   raise ValueError("You must play atleast 1 board")
  else:
   return boards_per_play

def number_of_draws(draws: int = None):
  if draws < 1:
    raise ValueError("You must play atleast 1 draw")
  return draws


def generate_quick_picks(boards: int):
    # returns a list of the draws and boards played by user in a list
    generate_boards = []

    for _ in range(boards):
        board = random.sample(range(lotto_min, lotto_max + 1), numbers_per_boards)
        board.sort()
        generate_boards.append(board)
    
    return generate_boards
 

# now we compare the users numbers based on the quick pick or winning numbers
def compare_winning_numbers(user_boards, winning_numbers = None):
  if winning_numbers is None:
    winning_numbers = random.sample(range(lotto_min, lotto_max + 1), numbers_per_boards)

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