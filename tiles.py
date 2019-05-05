# FCC Text-Based Game
# Author: Robert K Hitch
# Tiles Module 

# Here's really the meat and bones of the game, everything is laid out here
# We're going to define everything in our little cave, first we import 
import items, enemies, actions, world

# Let's create our base class for a tile. A coordinate approach works well for this! 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Let's create a method for displaying text when a player enters a room 
    def intro_text(self):
        raise NotImplementedError()
    # And for any actions in that room that change the state of the player    
    def modify_player(self, the_player):
        raise NotImplementedError()
# You might be asking the question why did I define these messages to just raise errors. 
# Essentially, "MapTile" is an abstract base class. We don't want any of them in our game. 
# After all, an empty tile would be kind of boring wouldn't it? 
# These functions will warn us if we accidentally put nothing for a tile 
    # Let's create a function to determine where the player can go 
    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
    # Let's create a function to determine what the player can do 
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

# Now we can start creating rooms 
class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You awake knee deep in a dirty pond, deep inside a cave. The only light source is a small torch on the wall.
        In the faint light, you can make out four paths, all of which appear quite frightening to you!
        """

    def modify_player(self, the_player):
        #Nothing happens in the starting room 
        pass

# How about a room where the player just has to keep moving 
class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        The cave here conintues on. Fairly unremarkable, not much to see.
        """

    def modify_player(self, the_player):
        #Nothing happens here also 
        pass

# Now we can create some special rooms where stuff happens, here's the class for when the player gets loot
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item) # Define how the player gets loot 

    def modify_player(self, the_player): # Now we run that function in the loot room 
        self.add_loot(the_player)


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Out of the corner of your eye you see a glimmer. 
        Looking closer, you find a dagger! 
        """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        A loose bag of gold coins is tucked away. You grab it, can't have too much money!
        """
class FindStaffRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.WizardStaff())
        
    def intro_text(self):
        return """
        You find a weird stick in the ground. 
        Grabbing it, you are filled with immense power. You're a wizard Al!
        """
# Now we must define the room where enemies are encountered! 
        
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player): # Here we say how the enemy does damage to the player 
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self): # The player gets some new actions here. They can either attack or flee 
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

# Now we can define our enemy rooms 
class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A stinky zombie is trying to eat your brains!
            """
        else:
            return """
            The zombie is dead. Dead, undead, then dead again. Kinda funny if you think about it.
            """


class OrcRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Orc())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A hideous orc appears in the shadows, he's coming for you!
            """
        else:
            return """
            The corpse of the orc rots on the ground here.
            """

class VampireRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Vampire())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Pale and oddly... stunning, it's vampire coming to suck your blood!
            """
        else: 
            return """
            A vampire lies beneath your feet. He bears a strange resemblance to Robert Pattinson...
            """ 

class WerewolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Werewolf())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
                   Looks like it's a full moon, even if you can't see outside. A werewolf pounces on you!
                   """
        else: 
            return """
                   No silver bullet needed. The werewolf rots into the soil. 
                   """              
# I just thought it'd be funny if there's one instant death tile 
class SnakePitRoom(MapTile):
    def intro_text(self):
        return """
        You have fallen into a pit of pythons! It's so complex, you die!
        """

    def modify_player(self, player):
        player.hp = 0

# Finally a room that allows the player to finish the game 
class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance. Could it be? Yes! Sunlight! Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
