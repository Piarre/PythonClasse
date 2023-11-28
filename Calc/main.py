# + - * /
# reset, quit

from utils import clear, title
import re
import colorama

def lint_history(expr):
    reg = re.findall(r"\d+ \* \d+|\d+ \/ \d+", expr)
    
    for operation in reg:
        expr = expr.replace(operation, f"({operation})")
    
    return expr

def main():
    result = 0
    history = ""
    
    clear()
    colorama.init()

    print(colorama.Fore.RED + "Welcome to the calculator!")
    print(colorama.Fore.RED + "Type 'quit' or 'ctrl+Q' to exit\n")
    
    title()

    while True:
        try:
            print(colorama.Fore.YELLOW + f"History :{lint_history(history[2::])}")
            print(colorama.Fore.BLUE + f"Actual result : {str(round(result, 2))}\n")
            currentInput = input(colorama.Fore.BLUE + "Command : ")

            if currentInput == "+":
                clear()
                print(colorama.Fore.BLUE + "Current operation : + \n")

                while True:
                    try:
                        val = int(input("Value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                history += f" + {str(val)}"
                result += val
            elif currentInput == "-":
                clear()
                print(colorama.Fore.BLUE + "Current operation : - \n")

                while True:
                    try:
                        val = int(input("Value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                history += f" - {str(val)}"
                result -= val
            elif currentInput == "*":
                clear()
                print(colorama.Fore.BLUE + "Current operation : * \n")

                while True:
                    try:
                        val = int(input("Value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                history += f" * {str(val)}"
                result *= val
            elif currentInput == "/":
                clear()
                print(colorama.Fore.BLUE + "Current operation : / \n")

                while True:
                    try:
                        val = int(input("Value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                history += f" / {str(val)}"
                result /= val
            elif currentInput == "quit":
                clear()
                break
            elif currentInput == "reset":
                result = 0
                clear()
                print(colorama.Fore.BLUE + "Result reset to 0")
            else:
                clear()
                print(colorama.Fore.RED + "Unknown command")

            title()

        except ValueError:
            clear()
            title()                        

        colorama.Fore.RESET


main()