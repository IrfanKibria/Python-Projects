class Calculator:

    def get_operation(self):
        while True:
            action = input("Enter what operation you want to do: add/sub/div/mul/exit: ").lower()
            if action in ['add', 'sub', 'mul', 'div', 'exit']:
                return action
            else:
                print(f"{action} is invalid, Please input a valid action")

    def get_numbers(self):
        while True:
            try:
                x = float(input("Enter a First Number: "))
                y = float(input("Enter a Second Number: "))
                return x, y
            except ValueError:
                print("Enter a valid integer number")


    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return None
        return x / y


    def calc(self):
        while True:
            action = self.get_operation()

            if action == 'exit':
                print("Thank You for using Calculator")
                break

            x, y = self.get_numbers()

            if action == 'add':
                print(f"{x} + {y} = {self.add(x, y)}")

            elif action == 'sub':
                print(f"{x} - {y} = {self.sub(x, y)}")

            elif action == 'mul':
                print(f"{x} * {y} = {self.mul(x, y)}")

            elif action == 'div':
                result = self.div(x, y)
                if result is None:
                    print("Any number can't be divided by 0")
                else:
                    print(f"{x} / {y} = {result}")

Calculator().calc()