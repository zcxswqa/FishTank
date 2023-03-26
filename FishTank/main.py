import time
import Aqua

def input_check(input):
    try:
        if float(input) == int(float(input)):
            input = int(float(input))
        else:
            input = -1
    except ValueError:
        input = -1
    return input

def demo(myaqua):
    myaqua.add_animal("scalarfish1", 4  , 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh')
    myaqua.add_animal("ocypodecrab2", 13, 41, myaqua.aqua_height, 0, 0, 'oc')
    myaqua.print_board()

    for i in range(120):
        for animal in myaqua.anim:
            if animal.get_food() <= 1:
                myaqua.feed_all()
        myaqua.next_turn()
        myaqua.print_board()

def add_animal(myaqua):
    choice = 0
    while not 1 <= choice <= 4:
        print("Please select:")
        print("1. Scalare")
        print("2. Moly")
        print("3. Ocypode")
        print("4. Shrimp")
        choice = input("What animal do you want to put in the aquarium?")
        choice = input_check(choice)

    name = input("Please enter a name:")
    age = 0
    while not 1 <= age <= 100:
        age = input("Please enter age:")
        age = input_check(age)

    success = False
    while not success:
        x, y = 0, 0
        while not 1 <= x <= (myaqua.aqua_width - 1):
            x = input("Please enter an X axis location (1 - %d):" % (myaqua.aqua_width - 1))
            x = input_check(x)

        if choice == 1 or choice == 2:
            while not Aqua.WATERLINE <= y <= (myaqua.aqua_height - 1):
                y = input("Please enter an Y axis location (%d - %d):" % (Aqua.WATERLINE - 1, myaqua.aqua_height - 1))
                y = input_check(y)

        directionH, directionV = -1, -1
        while not (directionH == 0 or directionH == 1):
            directionH = input("Please enter horizontal direction (0 for Left, 1 for Right):")
            directionH = input_check(directionH)

        if choice == 1 or choice == 2:
            while not (directionV == 0 or directionV == 1):
                directionV = input("Please enter vertical direction  (0 for Down, 1 for Up):")
                directionV = input_check(directionV)

        if choice == 1:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'sc')
        elif choice == 2:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'mo')
        elif choice == 3:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'oc')
        else:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'sh')
    return None


if __name__ == '__main__':
    width = 0
    height = 0

    print('Welcome to "The OOP Aquarium"')
    while width < 40:
        width = input("The width of the aquarium (Minimum 40): ")
        width = input_check(width)

    while height < 25:
        height = input("The height of the aquarium (Minimum 25): ")
        height = input_check(height)

    myaqua = Aqua.Aqua(width, height)

    while True:
        choice = 0
        while not 1 <= choice <= 7:
            print("Main menu")
            print("-" * 30)
            print("1. Add an animal")
            print("2. Drop food into the aquarium")
            print("3. Take a step forward")
            print("4. Take several steps")
            print("5. Demo")
            print("6. Print all")
            print("7. Exit")
            choice = input("What do you want to do?")
            choice = input_check(choice)

        if choice == 1:
            add_animal(myaqua)
        elif choice == 2:
            myaqua.feed_all()
        elif choice == 3:
            myaqua.next_turn()
        elif choice == 4:
            myaqua.several_steps()
        elif choice == 5:
            demo(myaqua)
        elif choice == 6:
            myaqua.print_all()
        else:
            print("Bye bye")
            exit()

        myaqua.print_board()
