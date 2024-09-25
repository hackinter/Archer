import os
import sys
import subprocess
from time import sleep
from colorama import Fore, Style, init
from rich import print as rich_print
from rich.panel import Panel

init(autoreset=True)

class Color:
    BLUE = '\033[94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    title = """ 
   █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
  ███████║██████╔╝██║     ███████║█████╗  ██████╔╝
  ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
  ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                   """
    print(Color.ORANGE + Style.BRIGHT + title)

def display_menu():
    clear_screen()
    display_title()
    print(Fore.WHITE + Style.BRIGHT + "─" * 65)
    border_color = Color.CYAN + Style.BRIGHT
    option_color = Fore.WHITE + Style.BRIGHT  

    print(border_color + "┌" + "─" * 63 + "┐")
    
    options = [
        "1]  WP Plugin Scanner",
        "2]  Path Enumeration",
        "3]  WP Enumeration",
        "4]  Emails Scanner",
        "5]  Ports Scanner",
        "6]  Subdomain Scanner",
        "7]  Wayback URLs",
        "8]  Exit"
    ]
    
    for option in options:
        print(border_color + "│ " + option_color + option.ljust(60) + border_color + "│")
    
    print(border_color + "└" + "─" * 63 + "┘")
    authors = "Created by: Naho, AnonKryptiQuz, CoffinXP, HexSh1dow"
    instructions = "Select an option by entering the corresponding number:"
    
    print(Fore.WHITE + Style.BRIGHT + "─" * 65)
    print(Fore.WHITE + Style.BRIGHT + authors.center(65))
    print(Fore.WHITE + Style.BRIGHT + "─" * 65)
    print(Fore.WHITE + Style.BRIGHT + instructions.center(65))
    print(Fore.WHITE + Style.BRIGHT + "─" * 65)

def print_exit_menu():
    clear_screen()
    panel = Panel(
        """
       \                |                 
      _ \     __|  __|  __ \    _ \   __| 
     ___ \   |    (     | | |   __/  |    
   _/    _\ _|   \___| _| |_| \___| _|    
                                             
                                      
  Credit - Naho x AnonKryptiQuz x CoffinXP x HexSh1dow 
        """,
        style="bold green",
        border_style="blue",
        expand=False
    )
    rich_print(panel)
    print(Color.RED + "\n\nSession Off ...\n")
    exit()

def execute_module(module_name):
    try:
        subprocess.run(f"python3 module/{module_name}.py", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(Color.RED + f"[!] {module_name} চালাতে ত্রুটি ঘটেছে: {e}")

def handle_selection(selection):
    module_map = {
        '1': "plugin",
        '2': "path",
        '3': "WPenum",
        '4': "emails",
        '5': "ports",
        '6': "subdomi",
        '7': "wayback",
        '8': None
    }

    if selection in module_map:
        clear_screen()
        if selection == '8':
            print_exit_menu()
        else:
            print(Color.GREEN + f"[+] {module_map[selection].replace('_', ' ').title()} চালু হচ্ছে...")
            execute_module(module_map[selection])
    else:
        print(Color.RED + "[!] অবৈধ নির্বাচন, আবার চেষ্টা করুন...")

def main():
    clear_screen()
    sleep(1)
    clear_screen()

    while True:
        display_menu()
        choice = input(f"\n{Fore.CYAN}[?] একটি অপশন নির্বাচন করুন (1-8): {Style.RESET_ALL}").strip()
        handle_selection(choice)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_exit_menu()
        sys.exit(0)
