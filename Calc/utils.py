import os
import colorama

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    print(colorama.Fore.BLUE + """
    Available operations:  
          
        + for addition
        - for subtraction
        * for multiplication
        / for division  
                
        reset for reset
            
        """)
