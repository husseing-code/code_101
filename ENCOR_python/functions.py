import datetime

def greet():
    #Get the current time
    dt = datetime.datetime.now()

    if dt.hour <= 11:
        greeting = "morning"
    elif dt.hour <= 17:
        greeting = "afternoon"
    else:
        greeting = "night"
    
    print("Hello, good " + greeting + ".")

#display the result from the function code
greet()