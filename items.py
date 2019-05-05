# FCC Text-Based Game
# Author: Robert K Hitch
# Items Module 

# No good adventure game is complete without items, let's define them all here

# First we need a base class for what an item is! Items have names, descriptions and values 
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# A certain subclass of items are weapons. In addition to other attributes, they also have damage
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

# Let's create some weapons
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="Rudimentary and crude, but it packs a punch!",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="Small rusty blade. It'll probably give you an infection if you cut yourself",
                         value=10,
                         damage=10)

class WizardStaff(Weapon):
    def __init__(self):
        super().__init__(name = "Wizard Staff",
                         description = "Tall and wiry, kind of like the developer. Incredibly powerful, but you look awfully goofy carrying it",
                         value = 35,
                         damage = 40)
        
# No good adventure game is complete without some treasure! 
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A coin with ${} engraved on the front.".format(str(self.amt)),
                         value=self.amt)
                
