
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack (self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        
    def battleCry(self):
        return f"Odin Owns You All!"
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"



# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"

# War

import random
class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    
    def vikingAttack(self):
        Viking = random.choice(self.vikingArmy)
        Saxon = random.choice(self.saxonArmy)
        saxon_damage = Saxon.receiveDamage(Viking.strength)
        if Saxon.health <= 0:
             self.saxonArmy.remove(Saxon)
        return saxon_damage


    
    def saxonAttack(self):
        Viking = random.choice(self.vikingArmy)
        Saxon = random.choice(self.saxonArmy)
        viking_damage = Viking.receiveDamage(Saxon.strength)
        if Viking.health <= 0:
             self.vikingArmy.remove(Viking)
        return viking_damage
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return f"Vikings and Saxons are still in the thick of battle."
        
