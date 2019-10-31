
# Soldier


class Soldier:
    pass
    def __init__(self,health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health=self.health-damage

# Viking


class Viking:
    pass
class Viking(Soldier):
    def __init___ (self,name,health, strength):
        self.name=name
        self.health=health
        self.strength=strength
    def receiveDamage(self,damage):
        if damage<self.health:
            self.health=self.health-damage
            return "{} has received DAMAGE points ".format(self.name)
        elif damage>self.health:
            return "{} has died in act of combat".format(self.name)   
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon:
    pass

class Saxon(Soldier):
    def __init__(self,health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        if damage<self.health:
            self.health=self.health-damage
            return "A Saxon has received DAMAGE points of damage"
        elif damage>self.health:
            return "A saxon has died in act of combat"  
