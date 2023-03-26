import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, directionH):
        super().__init__(name, age, x, directionH)
        self.y = 0
        self.width = 7
        self.height = 4

    def get_animal(self):
        array = [[" ", "*", " ", " ", " ", "*", " "],
                 [" ", " ", "*", "*", "*", " ", " "],
                 ["*", "*", "*", "*", "*", "*", "*"],
                 ["*", " ", " ", " ", " ", " ", "*"]]
        return array
