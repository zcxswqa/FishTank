import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []

    def build_tank(self):
        board_a = [[" " for x in range(self.aqua_width)] for x in range(WATERLINE - 1)]
        board_a.append(["~" for x in range(self.aqua_width)])
        board_b = [[" " for x in range(self.aqua_width)] for x in range(self.aqua_height - WATERLINE -1)]
        for x in range(len(board_b)):
            board_a.append(board_b[x])
        board_a.append(["_" for x in range(self.aqua_width)])
        for i in range(len(board_a) - 1):
            board_a[i][0] = "|"
            board_a[i][self.aqua_width - 1] = "|"
        board_a[self.aqua_height - 1][0] = "\\"
        board_a[self.aqua_height - 1][self.aqua_width - 1] = "/"
        self.board = board_a

    def print_board(self):
        for i in range(self.aqua_height):
            for j in range(self.aqua_width):
                print(self.board[i][j], end=" ")
            print()

    def get_board(self):
        return self.board

    def get_all_animal(self):
        return self.anim

    def is_collision(self, animal):
        for anim in self.anim:
            if isinstance(animal, Crab.Crab) and isinstance(anim, Crab.Crab) and not anim == animal:
                if abs(anim.x - animal.x) <= 8:
                    return True

    def print_animal_on_board(self, animal: Animal):
        y = animal.y
        x = animal.x
        for i in range(animal.height):
            self.board[y-1][x:x+animal.width] = animal.get_animal()[i]
            y += 1

    def delete_animal_from_board(self, animal: Animal):
        y = animal.y
        x = animal.x
        for i in range(animal.height):
            self.board[y-1][x:x+animal.width] = [" " for x in range(animal.width)]
            y += 1

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):

        if fishtype == "sc":
            fish = Scalar.Scalar(name, age, x, y, directionH, directionV)
        elif fishtype == "mo":
            fish = Moly.Moly(name, age, x, y, directionH, directionV)
        if x < 1:
            fish.set_x(1)
        elif x > self.aqua_width - (fish.width + 1):
            fish.set_x(self.aqua_width - (fish.width + 1))
        if y < WATERLINE + 1:
            fish.set_y(WATERLINE + 1)
        elif y > self.aqua_height - MAX_CRAB_HEIGHT - fish.height:
            fish.set_y(self.aqua_height - MAX_CRAB_HEIGHT - fish.height)
        if self.check_if_free(fish.x, fish.y):
            self.anim.append(fish)
            self.print_animal_on_board(fish)
            return True
        else:
            return False

    def add_crab(self, name, age, x, directionH, crabtype):
        if crabtype == 'oc':
            crab = Ocypode.Ocypode(name, age, x, directionH)
            crab.set_y(self.aqua_height - 4)
        elif crabtype == 'sh':
            crab = Shrimp.Shrimp(name, age, x, directionH)
            crab.set_y(self.aqua_height -3)
        if x < 1:
            crab.set_x(1)
        elif x > self.aqua_width - (crab.width + 1):
            crab.set_x(self.aqua_width - (crab.width + 1))
        if self.check_if_free(crab.x, crab.y):
            self.anim.append(crab)
            self.print_animal_on_board(crab)
            return True
        else:
            return False

    def check_if_free(self, x, y) -> bool:
        free = True
        for anim in self.anim:
            if abs(x - anim.x) < Animal.MAX_ANIMAL_WIDTH and abs(y - anim.y) < Animal.MAX_ANIMAL_HEIGHT:
                free =  False
        if not free:
            print("The place is not available! Please try again later.")
        return free

    def left(self, animal):
        if animal.x <= 1:
            animal.set_directionH(1)
        else:
            self.delete_animal_from_board(animal)
            animal.left()

    def right(self, animal):
        if animal.x >= self.aqua_width - (animal.width+1):
            animal.set_directionH(0)
        else:
            self.delete_animal_from_board(animal)
            animal.right()

    def up(self, animal):
        if animal.y <= WATERLINE + 1:
            animal.set_directionV(0)
        else:
            self.delete_animal_from_board(animal)
            animal.up()

    def down(self, animal):
        if animal.y >= self.aqua_height - MAX_CRAB_HEIGHT - animal.height:
            animal.set_directionV(1)
        else:
            self.delete_animal_from_board(animal)
            animal.down()

    def next_turn(self):
        for animal in self.anim:
            if self.turn % 10 == 0:
                animal.dec_food()
            if self.turn % 100 == 0:
                animal.inc_age()
            animal.die()
            animal.starvation()

        dead_animal = []
        for animal in self.anim:
            if not animal.alive:
                self.delete_animal_from_board(animal)
                dead_animal.append(animal)
        for i in range(len(dead_animal)):
            self.anim.remove(dead_animal[i])

        for animal in self.anim:
            if self.is_collision(animal):
                if animal.get_directionH() == 1:
                    animal.set_directionH(0)
                else:
                    animal.set_directionH(1)

        for animal in self.anim:
            if animal.get_directionH() == 1:
                self.right(animal)
            else:
                self.left(animal)
            if isinstance(animal, Fish.Fish):
                if animal.get_directionV() == 1:
                    self.up(animal)
                else:
                    self.down(animal)
            self.print_animal_on_board(animal)
        self.turn += 1

    def print_all(self):
        for animal in self.anim:
            print(str(animal))

    def feed_all(self):
        for animal in self.anim:
            animal.add_food(10)

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        number_of_steps = input("How many steps do you want to take?")
        for i in range(int(number_of_steps)):
            self.next_turn()