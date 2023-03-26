import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5

    def get_animal(self):
        array1 = [["*", "*", "*", "*", "*", "*", " ", " "],
                  [" ", " ", " ", " ", "*", "*", "*", " "],
                  [" ", " ", "*", "*", "*", "*", "*", "*"],
                  [" ", " ", " ", " ", "*", "*", "*", " "],
                  ["*", "*", "*", "*", "*", "*", " ", " "]]
        array0 = [line[::-1] for line in array1]
        if self.directionH == 1:
            return array1

        elif self.directionH == 0:
            return array0
