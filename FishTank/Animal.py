MAX_ANIMAL_HEIGHT = 5
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        st = "the " + self.__class__ + str(self.name) + " is " + str(self.age) + " with " + str(self.food) + " food"
        return st

    def get_food(self):
        return self.food

    def get_age(self):
        return self.age

    def dec_food(self):
        self.food -= 1

    def inc_age(self):
        self.age += 1

    def right(self):
        self.x += 1
        return self.x

    def left(self):
        self.x -= 1
        return self.x

    def get_position(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def starvation(self):
        pass

    def die(self):
        pass

    def get_directionH(self):
        return self.directionH

    def set_directionH(self, directionH):
        self.directionH = directionH

    def get_alive(self):
        return self.alive

    def get_size(self):
        return self.width, self.height

    def get_food_amount(self):
        return self.food

    def add_food(self, amount):
        self.food += amount

    def get_animal(self):
        pass
