# FCC Text-Based Game
# Author: Robert K Hitch
# Items Module

# Start by defining our base class for items, they can have names, descriptions and values
class Item():
    """This is our base class for items"""
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.desc, self.value)
# Gold is a must for any good fantasy game    
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         desc="A coin with {} engraved on the front.".format(str(self.amt)),
                         value=self.amt)
# Let's make a subclass of items that are our weapons, they have the attribute also of damage! 
class Weapon(Item):
    def __init__(self, name, desc, value, damage):
        self.damage = damage
        super().__init__(name, desc, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.desc, self.value, self.damage)
 
 # Let's create some weapons 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Stone",
                         desc="Rudimentary and crude, but it packs a punch!",
                         value=0,
                         damage=5)
 
 
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         desc="Small rusty blade. It'll probably give you an infection if you cut yourself",
                         value=10,
                         damage=10)
        
class Sword(Weapon):
    def __init__(self):
        super().__init__(name = "Sword",
                         desc = "Long and powerful, but a little heavy. You'll need to hit the gym",
                         value = 25,
                         damage = 30)

class WizardStaff(Weapon):
    def __init__(self):
        super().__init__(name = "Wizard Staff",
                         desc = "Tall and wiry, kind of like the developer. Incredibly powerful, but you look awfully goofy carrying it",
                         value = 35,
                         damage = 40)
        
        