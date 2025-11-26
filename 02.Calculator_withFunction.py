def operation():
    while True:
        action = input("Enter what operation you want to do: add/sub/div/mul/exit: ")
        if action.lower() in ['add', 'sub','mul','div','exit']:
            return action
        else:
            print(f"{action} this is invalid, Please Input valid action")

def numbers():
    while True:
        try:
            x = int("Enter a First Number: ")
            y = int("Enter a second Number: ")
            return x,y
        except ValueError as v:
            print("Enter valid integer Number")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x*y

def div(x, y):
    if y ==0:
        return None
    else:
        return x/y
    
def calculation():
    while True:
        