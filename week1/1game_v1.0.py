class character(object):
    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

class Hero(character):
    def__init__(self):
        self.health = 10
        self.power = 5

        def attack(self, enemy):
            enemy.health -= self.power
            print "YOu do $d damage to the goblin." % self.power
            if enemy.health <= 0:
                print "The goblin is dead."

        def print_status(self):
            print "You have %d health and %d power." %(self.health, self.power)

class goblin(character):
    def__init__(self):
        self.health = 6






    print "The goblin does %d damage to you." % self.power
    if enemy.health <= 0: 