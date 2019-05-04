# FCC Text-Based Game
# Author: Robert K Hitch
# Enemies Module 

# Start defining out class for enemies, they can have names, health, and damage

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        
    # Also probably a good idea to define if our enemies are alive. Otherwise it might be hard to kill theme 
    def alive_status(self):
        return self.health > 0 # If the health is over 0, the enemy is by definition alive

# Proceeding to create the enemies for the game    
class Orc(Enemy):
    def __init__(self):
        super().__init__(name="Orc", health=30, damage=15)
    
class Zombie(Enemy):
    def __init__(self):
        super().__init__(name = "Zombie", health=10, damage=2)
        
class Vampire(Enemy):
    def __init__(self):
        super().__init__(name="Vampire", health=100, damage=4)
        
class Werewolf(Enemy): 
    def __init__(self):
        super().__init__(name="Werewolf", health=80, damage=15)
        

        
    