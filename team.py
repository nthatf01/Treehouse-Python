# Create an empty list to maintain the player names
player_names = []
user_wants_to_add_player = ""

# Ask the user if they'd like to add players to the list.
while user_wants_to_add_player != "no":
    user_wants_to_add_player = input("Would you like to add a player to the list? (Yes/No) ").lower()

    # If the user answers "Yes", let them type in a name and add it to the list.
    if user_wants_to_add_player == "yes":
        player_names.append(input("Enter the name of the player to add to the team: "))
        print("")

# If the user answers "No", print out the team 'roster'

# print the number of players on the team
print("")
print("There are {} players on the team.".format(len(player_names)))

# Print the player number and the player name
# The player number should start at the number one
for player_number in range(len(player_names)):
    print("Player {}: {}".format(player_number+1, player_names[player_number]))

print("")
# Select a goalkeeper from the above roster
if len(player_names) > 0:
    goalkeeper = player_names[int(input("Please select the goal keeper by selecting the player number. (1-{}) ".format(len(player_names))))-1]

    # Print the goal keeper's name
    print("Great!!! The goalkeeper for the game will be {}.".format(goalkeeper))


