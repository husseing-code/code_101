direction = input("Do you want to go (N)north, (S)outh, (E)ast, (W)est?")

if direction == "n":
    print("You head north, into the forest.")
elif direction == "s":
    print("The cost blocks your path south.")
elif direction == "w":
    print("The western fields are comforting to walk through.")
elif direction == "e":
    print("You were eaten by a grue.")
else:
    print("I didn't recognize your choice")