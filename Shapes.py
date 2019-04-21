count = True
print("\nMade By Muhammad Waleed Usman")
while count:
    shape = input("\nEnter your choice:"
                  "\n<kite> for kite."
                  "\n<right facing> for right facing triangle."
                  "\n<right angle> for right angled triangle."
                  "\n<rectangle> for right angled triangle."
                  "\n<name> for the first letter of name."
                  "\n<q> for the Quit."
                  "\nYour choice? ")
    if shape == "q":
        count = False
        print("\nGood bye!")
    else:
        height = int(input("\nEnter the height of the " + shape + " in grid points: "))
        print("\n")
        if shape == 'kite':
            height = int(height / 2)
            for j in range(1, 3):
                for i in range(0, height + 1):
                    if j == 1:
                        print(" " * (height - i) + "*" * ((2 * i) + 1))
                    elif j == 2:
                        print(" " * (i + 1) + "*" * (2 * (height - i) - 1))

        elif shape == 'right facing':
            for j in range(1, 3):
                for i in range(0, height):
                    if j == 1:
                        print("*" * (i + 1))
                    elif j == 2:
                        print("*" * ((height - i) - 1))

        elif shape == 'right angle':
            for i in range(0, height):
                print("*" * (i + 1))

        elif shape == 'rectangle':
            width = int(input("Enter the width of the rectangle in grid points: "))
            print("\n")
            for j in range(0, height):
                print("*" * width)

        elif shape == 'name':
            print("\nName: Muhammad Waleed Usman\n")
            height = height + 2
            for i in range(height - 1, 1, -1):
                print("*" + " " * (height - 1 - i) + "*" + " " * ((2 * i) - 4) + "*" + " " * (height - 1 - i) + "*")
            print("\n")
            height = height - 1
            for i in range(1, height):
                print("*" + " " * (height - 1 - i) + "*" + " " * ((2 * i) - 2) + "*" + " " * (height - 1 - i) + "*")
            print("\n")
            for i in range(1, height):
                if i < height - 1:
                    print("*" + " " * (2 * height - 2) + "*")
                if i == height - 1:
                    print("*" * (2 * height))
        another = input("\nEnter <y> if you want to draw another shape and <n> if you want to exit? ")
        if another == 'y':
            print("\n"*50)
        elif another == 'n':
            count=False
            print("\nGood bye!")
