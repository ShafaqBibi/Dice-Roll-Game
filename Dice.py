#For generate random numbers
import random

#This function will generate random numbers from 1 to 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

print("\nWELCOME TO THE DICE ROLL GAME")
print("\nRULE:\n  *Dice number must be greater then 1.\n  *Turn will be ended if got 1.\n\n")

#This loop will take the info of players that how many players will play
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Members must be between 2 - 4")

    else:
        print("Invalid, try again.")

# Set the maximum score limit for players
max_score = 50
# Initialize player scores to zero using a list comprehension
players_scores = [0 for _ in range(players)]

#This block of code responsible to manage individual player's score, compare individual player's score, 
#and declare the winner.
while max(players_scores) < max_score:

    #This inner loop check the player number and initial score
    for player_num in range(players):
        print("\nPlayer Number",player_num + 1, "turn has just started!")
        print("Your current score is: ",players_scores[player_num],"\n")
        current_score = 0

        #This loop ask from user to want to roll dice or not.
        while True:
            roll_mode = input("Would you like roll the Dice (Y)?: ")
            if roll_mode.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("\nYou rolled a 1! Turn done!")
                current_score += value
                break
            else:
                current_score += value
                print("\nYou rolled a:", value)

            print("Your current score is: ",current_score,"\n")

        #Keep record of individual player's total score
        players_scores[player_num] += current_score
        print("\nYour total score is: ",players_scores[player_num]) 

    #Compare the score of individual player and declare the winner
    max_score = max(players_scores)
    winner_player = players_scores.index(max_score)
    print("Player number ", winner_player + 1, "is the winner with the score of: ",max_score,"\n")