import Animal

MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8


class Fish(Animal.Animal):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, directionH)
        self.y = y
        self.width = MAX_FISH_WIDTH
        self.height = MAX_FISH_HEIGHT
        self.directionV = directionV  # random 0 - down / 1 - up

    def __str__(self):
        st = "The fish " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st

    def up(self):
        self.y -= 1
        return self.y

    def down(self):
        self.y += 1
        return self.y

    def starvation(self):
        if self.food <= 0:
            print("the fish " + str(self.name) + " died at the age of " + str(self.age) + " years\nBecause he ran out of food")
            self.alive = False

    def die(self):
        if self.age >= 120:
            print(str(self.name) + " died in good health")
            self.alive = False

    def get_directionV(self):
        return self.directionV

    def set_directionV(self, directionV):
        self.directionV = directionV