print("============================================")
print("          Welcome to Holiday Planner        ")
print("============================================")
print()

print("Step 1:Pick your holiday type")
print("    1 - Beach holiday")
print("    2  - Mountain Holiday")
print()

choice = int(input("Enter 1 0r 2: "))
print()

if choice == 1:
    print("Step 2:Pick our beach activity")
    print("  1 - swimming")
    print("  2 - sandcastle building")
    print()

    beach_activity = int(input("Enter 1 or 2: "))
    print()

    if beach_activity == 1:
        print("You picked  : Swimming")
        print("Best time   : Morning")
        print("Remember    : Carry sunscreen and water")
    else:
        print("You picked  : Sandcastle building")
        print("Best time   : Evening")
        print("Remember    : Carry a bucket and spade")

elif choice == 2:
    print("Step 2: Pick your mountain activity")
    print("  1 - hiking")
    print("  2 - camping")
    print()

    mountain_activity = int(input("Enter 1 or 2: "))
    print()

    if mountain_activity == 1:
        print("You picked   : Hiking")
        print("Best for     : Exploring trails")
        print("Remember     : Wear comfortable shoes")
    else:
        print("You picked   : camping")
        print("Best for     : Staying close to nature")
        print("Remember     : Carry a tent and flashlight")

else:
    print("That was not a valid choice")
    print("Please enter 1 for beach holiday or 2 for mountain holiday")

print()
print("===========================================")
print("       Your Holiday plan is ready          ")
print("Enjoy your trip                            ")
print("===========================================")


        



