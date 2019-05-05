# FCC Text-Based Game
# Author: Robert K Hitch
# Enemies Module 

# Similar to the items module, we need to list all the enemies we might encounter in our game 

# Enemies have names, health, and the damage that they can do 
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

# Let's create some of my favorite monsters! 
        
class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", hp=10, damage=2)


class Orc(Enemy):
    def __init__(self):
        super().__init__(name="Orc", hp=30, damage=15)


class Vampire(Enemy):
    def __init__(self):
        super().__init__(name="Vampire", hp=100, damage=4)
        
