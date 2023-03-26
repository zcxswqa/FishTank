import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, directionH):
        super().__init__(name, age, x, directionH)
        self.width = MAX_CRAB_WIDTH
        self.height = MAX_CRAB_HEIGHT

    def __str__(self):
        st = "The crab " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st

    def starvation(self):
        if self.food <= 0:
            print("the crab " + str(self.name) + " died at the age of " + str(self.age) + " years\nBecause he ran out of food")
            self.alive = False

    def die(self):
        if self.age >= 120:
            print(str(self.name) + " died in good health")
            self.alive = False

