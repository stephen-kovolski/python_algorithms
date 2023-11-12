def main():
    x = int(input("Enter a number: "))
    y = input("Enter +, -, *, /: ")
    z = int(input("Enter another number: "))

    if y in ["+", "-", "*", "/"]:
        if y == "+":
            print(x + z)
        elif y == "-":
            print(x - z)
        elif y == "*":
            print(x * z)
        elif y == "/":
            print(x / z)

main()