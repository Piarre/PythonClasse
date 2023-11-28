# + - * /
# reset, quit

from utils import clear, title
import colorama
import time


def main():
    clear()
    colorama.init()

    print(colorama.Fore.RED + "Welcome to the calculator!")
    print(colorama.Fore.RED + "Type 'quit' or 'ctrl+Q' to exit\n")

    result = 0
    title()

    while True:
        try:
            currentInput = input("\nCommand : ")

            if currentInput == "+":
                clear()
                print(colorama.Fore.BLUE + "Current operation : + \n")

                while True:
                    try:
                        first = int(input("First value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                while True:
                    try:
                        seconde = int(input("Second value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                result +=( first + seconde)
            elif currentInput == "-":
                clear()
                print(colorama.Fore.BLUE + "Current operation : - \n")

                while True:
                    try:
                        first = int(input("First value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                while True:
                    try:
                        seconde = int(input("Second value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                result += (first - seconde)
            elif currentInput == "*":
                clear()
                print(colorama.Fore.BLUE + "Current operation : * \n")

                while True:
                    try:
                        first = int(input("First value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                while True:
                    try:
                        seconde = int(input("Second value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                result += (first * seconde)
            elif currentInput == "/":
                clear()
                print(colorama.Fore.BLUE + "Current operation : / \n")

                while True:
                    try:
                        first = int(input("First value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                while True:
                    try:
                        seconde = int(input("Second value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                result += (first / seconde)
            elif currentInput == "quit":
                break
            elif currentInput == "reset":
                result = 0
                clear()
                print(colorama.Fore.BLUE + "Result reset to 0")
            else:
                clear()

            title()
            print(f"Actual result: {result}")

        except ValueError:
            clear()
            title()                        

        colorama.Fore.RESET


main()
