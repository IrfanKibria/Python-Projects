def operation():
    while True:
        action = input("Enter what operation you want to do: add/sub/div/mul/exit: ")
        if action.lower() in ['add', 'sub','mul','div','exit']:
            return action
        else:
            print(f"{action} this is invalid, Please Input valid action")

def numbers():
    while True:
        