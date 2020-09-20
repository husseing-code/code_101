#states = ["New York", "Michigan", "California", "Texas", "Oregon"]

#for state in states:
 #   print(state)


#abbrevs = {
#   "New York" : "NY" ,
#  "Michigan" : "MI" ,
#    "California" : "CA" ,
 #   "Texas" : "TX" , 
 #   "Oregon" : "OR"
#}

#for key in abbrevs:
 #   print(key + ":" + abbrevs[key])


#for i in range(20):
 #   print(i)

direction = ""

while direction != "q":
    direction = input("Do you want to go (N)orth, (S)outh, (E)ast, (W)est")

    if direction == "n":
        print("You head north, into the forest.")
    elif direction == 's':
        print("The cost blocks your path south.")
    elif direction == "w":
        print("The western fields are comforting to walk through.")
    elif direction == "q":
        print("Quitting the game.")
    else:
        print("I didn't recognize your choice")