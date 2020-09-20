import datetime

print("Hello there this is being passed into the print() function!")

text = "Hi, this is stored in a string variable."
print(text)

def greet(name):
    #Get the current time
    dt = datetime.datetime.now()

    if dt.hour <= 11:
        greeting = "morning"
    elif dt.hour <= 17:
        greeting = "afternoon"
    else:
        greeting = "night"

    print("Hello " + name + ", good" + greeting + ".")

username = input("What is your name? ")
greet(username)