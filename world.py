# FCC Text-Based Game
# Author: Robert K Hitch
# World Module 

# This is the script used to create a world. I laid out the rooms in a text file, and this parses thru the file to
# create the game in the computer. 

_world = {} # Start an empty dictionary 
starting_position = (0, 0)

def tile_exists(x, y): # Returns tile at given coordinates or none if it doesn't exist 
        return _world.get((x, y))


def load_tiles():
    with open('resources/map.txt', 'r') as f: # The file is here that we need to get, change if elsewhere 
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y) # Ensuring we start in the starting room 
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


