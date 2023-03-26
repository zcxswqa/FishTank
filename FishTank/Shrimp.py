import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, directionH):
        super().__init__(name, age, x, directionH)
        self.y = 0
        self.width = 7
        self.height = 3

    def get_animal(self):
        array1 = [[" ", " ", " ", " ", "*", " ", "*"],
                  ["*", "*", "*", "*", "*", "*", " "],
                  [" ", " ", "*", " ", "*", " ", " "]]
        array0 = [line[::-1] for line in array1]
        if self.directionH == 1:
            return array1
        elif self.directionH == 0:
            return array0
