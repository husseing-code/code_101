fruits = ["apple", "banana", "strawberry", "orange", "peach"]

fruits[4] = "nectarine"

print(fruits[4])

#a type object, just like a list but 'immutable'
fruits_tuple = ("apple", "banana", "strawberry", "orange", "peach")

#This line will throw an exception
#fruits_tuple[4] = "Nectarine"


fruit_locations = {
    "Bin 1" : "apple",
    "Bin 2" : "banana",
    "Bin 3" : "strawberry",
    "Bin 1" : "orange",
    "Bin 1" : "peach",
}

print(fruit_locations.get("Bin 3"))