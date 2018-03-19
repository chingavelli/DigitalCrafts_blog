class Hero(object):
    def __init__(self):
        self.barry_the_hero.health = 10
        self.barry_the_hero.power = 5
class Goblin(object):
    def __init__(self):
        self.steve_the_goblin.health = 6
        self.steve_the_goblin.power = 2


def main():
    barry_the_hero = Hero()
    steve_the_goblin = Goblin()

    while steve_the_goblin.health > 0 and barry_the_hero.health > 0:
        print "You have %d health and %d power." % (barry_the_hero.health, barry_the_hero.power)
        print "The goblin has %d health and %d power." % (steve_the_goblin.health, steve_the_goblin.power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            steve_the_goblin.health -= barry_the_hero.power
            print "You do %d damage to the goblin." % barry_the_hero.power
            if steve_the_goblin.health <= 0:
                print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.health > 0:
            # Goblin attacks hero
            barry_the_hero.health -= steve_the_goblin.power
            print "The goblin does %d damage to you." % steve_the_goblin.power
            if barry_the_hero.health <= 0:
                print "You are dead."


main()
        