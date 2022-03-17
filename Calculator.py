command = ""
command1 = ""

while command1 != "quit":
    command1 = input("> ")
    if command1 != "calculator":
        print("Sorry! I didn't understand what u are saying!")
    if command1 == "calculator":
        while command.lower() != "quit":
            num1 = float(input("> Enter First Number: "))
            num2 = float(input("> Enter Second Number: "))
            command = input("> Do u want to add or subtract or multiply or divide: ").lower()

            if command == "add":
                def add(num1, num2):
                    return num1 + num2
                a = add(num1, num2)
                print(a)
            elif command == "multiply":
                def multiply(num1, num2):
                    return num1 * num2
                b = multiply(num1, num2)
                print(b)
            elif command == "divide":
                def divide(num1, num2):
                    return num1 / num2
                c = divide(num1, num2)
                print(c)
            elif command == "sub" or "subtract":
                def subtract(num1, num2):
                    return num1 - num2
                d = subtract(num1, num2)
                print(d)