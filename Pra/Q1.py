import math

h = 0
a = 0
b = 0


while (True):
    chk = 0
    while chk == 0:
        try:
            h = int(input("Enter the length of hypotenuse(unit):"))
            chk += 1
        except:
            print("Sorry please enter it again")
            chk = 0
    while chk == 1:
        try:
            b = int(input("Enter the length of first side(unit):"))
            chk += 1
        except:
            print("Sorry please enter it again")
            chk = 1
    while chk == 2:
        try:
            a = int(input("Enter the length of second side(unit):"))
            chk += 1
        except:
            print("Sorry please enter it again")
            chk = 2

    if math.sqrt(h) == math.sqrt(a)+math.sqrt(b) and h > 0:
        print("Yes, it is a right angle triangle")
    elif math.sqrt(h) != math.sqrt(a)+math.sqrt(b) and a and b and h > 0:
        print("No, it is not a right angle triangle")
    print()
