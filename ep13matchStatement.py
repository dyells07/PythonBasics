from enum import Enum
from colorama import Fore, Back, Style

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    WHITE = 'white'
    GRAY = 'gray'
    SILVER = 'silver'
    GOLD = 'gold'
    MAROON = 'maroon'
    NAVY = 'navy'
    TEAL = 'teal'
    OLIVE = 'olive'
    LIME = 'lime'
    AQUA = 'aqua'
    FUCHSIA = 'fuchsia'
    BEIGE = 'beige'
    CORAL = 'coral'
    INDIGO = 'indigo'
    BLACK = 'black'

def print_color(color):
    match color:
        case Color.RED:
            print(Fore.RED + "Red is the ultimate cure for sadness." + Style.RESET_ALL)
        case Color.GREEN:
            print(Fore.GREEN + "Your favorite color is green" + Style.RESET_ALL)
        case Color.BLUE:
            print(Fore.BLUE + "Your favorite color is blue" + Style.RESET_ALL)
        case Color.WHITE:
            print(Fore.WHITE + "Your favorite color is white" + Style.RESET_ALL)
        case Color.GRAY:
            print(Fore.LIGHTBLACK_EX + "Your favorite color is gray" + Style.RESET_ALL)
        case Color.SILVER:
            print(Fore.LIGHTBLACK_EX + "Your favorite color is silver" + Style.RESET_ALL)
        case Color.GOLD:
            print(Fore.YELLOW + "Your favorite color is gold" + Style.RESET_ALL)
        case Color.MAROON:
            print(Fore.MAGENTA + "Your favorite color is maroon" + Style.RESET_ALL)
        case Color.NAVY:
            print(Fore.BLUE + "Your favorite color is navy" + Style.RESET_ALL)
        case Color.TEAL:
            print(Fore.CYAN + "Your favorite color is teal" + Style.RESET_ALL)
        case Color.OLIVE:
            print(Fore.YELLOW + "Your favorite color is olive" + Style.RESET_ALL)
        case Color.LIME:
            print(Fore.GREEN + "Your favorite color is lime" + Style.RESET_ALL)
        case Color.AQUA:
            print(Fore.CYAN + "Your favorite color is aqua" + Style.RESET_ALL)
        case Color.FUCHSIA:
            print(Fore.MAGENTA + "Your favorite color is fuchsia" + Style.RESET_ALL)
        case Color.BEIGE:
            print(Fore.LIGHTYELLOW_EX + "Your favorite color is beige" + Style.RESET_ALL)
        case Color.CORAL:
            print(Fore.RED + "Your favorite color is coral" + Style.RESET_ALL)
        case Color.INDIGO:
            print(Fore.MAGENTA + "Your favorite color is indigo" + Style.RESET_ALL)
        case Color.BLACK:
            print(Fore.BLACK + "Your favorite color is black" + Style.RESET_ALL)
        case _:
            print("Sorry, I don't know that color")

color_input = input("What is your favorite color? ")
try:
    color = Color[color_input.upper()]
    print_color(color)
except KeyError:
    print("Sorry, I don't know that color")
