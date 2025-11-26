while True:
    operation = input("Enter what operation you want to do: add/sub/div/mul/exit: ")

    if operation.lower() == 'exit':
        print(f'Thank You For Using Calculator')
        break
    

    x = int(input("Enter first number for operation: "))
    y = int(input("Enter second number for operation: "))

    if operation.lower() == 'add':
        print(f'{x} + {y} = {x+y}')

    elif operation.lower() == 'sub':
        print(f'{x} - {y} = {x-y}')

    elif operation.lower() == 'mul':
        print(f'{x} * {y} = {x*y}')

    elif operation.lower() == 'div':
        if y == 0:
            print(f"No number can divided by 0")
        else:
            print(f"{x} / {y} = {x/y}")
