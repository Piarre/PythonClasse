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
    history = "0"
    
    clear()
    colorama.init()

    print(colorama.Fore.RED + "Welcome to the calculator!")
    print(colorama.Fore.RED + "Type 'quit' or 'ctrl+Q' to exit\n")
    
    title()

    while True:
        try:
            currentInput = input(colorama.Fore.BLUE + "Command : ")

            if currentInput in ["+", "-", "*", "/"]:
                clear()
                print(colorama.Fore.BLUE + f"Current operation : {currentInput} \n")

                while True:
                    try:
                        val = int(input("Value : "))
                        break
                    except ValueError:
                        print(colorama.Fore.RED + "Error number only")

                clear()
                history += f" {currentInput} {str(val)}"
            elif currentInput == "quit":
                clear()
                break
            elif currentInput == "reset":
                history = "0"
                clear()
                print(colorama.Fore.BLUE + "Result reset to 0")
            else:
                clear()
                print(colorama.Fore.RED + "Unknown command")

            result = eval(history)
            
            title()

            print(colorama.Fore.YELLOW + f"History :{lint_history(history[2::])}")
            print(colorama.Fore.BLUE + f"Actual result : {str(round(result, 2))}\n")


        except ValueError:
            clear()
            title()                        

        colorama.Fore.RESET


main()
