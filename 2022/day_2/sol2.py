import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    input_strategy_guide = f.read().splitlines()
    

# Parse the input strategy guide and create a list of rounds
rounds = []

for line in input_strategy_guide:
    move, response = line.split()
    rounds.append({"opponent_move": move, "recommended_move": response})
  # Define a dictionary mapping opponent moves to player moves
move_mapping = {
    "A": "X",  # Opponent's Rock is mapped to player's Rock
    "B": "Y",  # Opponent's Paper is mapped to player's Paper
    "C": "Z",  # Opponent's Scissors is mapped to player's Scissors
}

# Parse the input strategy guide and store it in a list
strategy_guide = []

for line in input_strategy_guide:
    move, response = line.split()
    strategy_guide.append(response)

# Set up a dictionary mapping move names to scores
scores = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

# Set up a dictionary mapping move names to their winning move
wins = {
    "X": "Z",  # Rock wins against Scissors
    "Y": "X",  # Paper wins against Rock
    "Z": "Y",  # Scissors wins against Paper
}

# Initialize total score
total_score = 0

# For each round in the game
for i, round in enumerate(rounds):
    # Look up the recommended move in the strategy guide
    recommended_move = strategy_guide[i]

    # Convert the opponent's move to the corresponding move for the player
    opponent_move = move_mapping[round["opponent_move"]]

    # Calculate the score for this round
    if recommended_move == opponent_move:
        # It's a draw
        round_score = scores[recommended_move] + 3
    elif wins[recommended_move] == opponent_move:
        # You win
        round_score = scores[recommended_move] + 6
    else:
        # You lose
        round_score = scores[recommended_move] + 0

    # Add the score for this round to the total score
    total_score += round_score

# Print the total score
print(total_score)