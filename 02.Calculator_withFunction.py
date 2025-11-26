def operation():
    while True:
        action = input("Enter what operation you want to do: add/sub/div/mul/exit: ").lower()
        if action in ['add', 'sub','mul','div','exit']:
            return action
        else:
            print(f"{action} this is invalid, Please Input valid action")

def numbers():
    while True:
        try:
            x = int(input("Enter a First Number: "))
            y = int(input("Enter a second Number: "))
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
    
def calculator():
    while True:
        ac = operation()
        if ac == 'exit':
            print("Thank You for using Calculator")
            break

        x, y = numbers()

        if ac == 'add':
            print(f'{x} + {y} = {add(x,y)}')

        if ac == 'sub':
            print(f'{x} - {y} = {sub(x,y)}')

        if ac == 'mul':
            print(f'{x} * {y} = {mul(x,y)}')

        if ac == 'div':
            result = div(x,y)
            if result is None:
                print("Any number cant divided by 0")
            else:
                print(f"{x} / {y} = {result}")

calculator()