from vikingsClasses import*
import random
def create_teams(num_vikings, num_saxons):
    war = War()
    for i in range(num_vikings):
        name = f"Viking {i+1}"
        health = random.randint(80, 120)
        strength = random.randint(20, 30)
        viking = Viking(name, health, strength)
        war.addViking(viking)
    
    for i in range(num_saxons):
        health = random.randint(50, 90)
        strength = random.randint(10, 25)
        saxon = Saxon(health, strength)
        war.addSaxon(saxon)
    
    return war
