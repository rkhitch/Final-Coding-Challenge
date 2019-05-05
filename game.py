# FCC Text-Based Game
# Author: Robert K Hitch
# Game Module 

# Importing neccessary modules
import world
from player import Player

# Defining a function to play the game 
def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions() # Printing out the actions that the player can do 
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions: # Letting the player type in what they would like to do 
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

# Here we can run the program!
if __name__ == "__main__":
    play()
    
    


