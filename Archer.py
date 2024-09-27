import os
import sys
import subprocess
from time import sleep
from colorama import Fore, Style, init
from rich import print as rich_print
from rich.panel import Panel
from rich.console import Console
from rich.progress import track
import random

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# Class for terminal colors
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

# Tips to display randomly
TIPS = [
    "Tip: Always run scripts with proper permissions.",
    "Tip: Check for module dependencies before running.",
    "Tip: Regularly update your modules for security fixes.",
    "Tip: You can modify the script to add more functionalities."
]

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the title with ASCII art
def display_title():
    title = """ 
   █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
  ███████║██████╔╝██║     ███████║█████╗  ██████╔╝
  ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
  ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                   """
    console.print(title, style="bold orange")

# Display the menu options
def display_menu():
    clear_screen()
    display_title()
    console.print("─" * 65, style="bold white")
    
    options = [
        "1]  WP Plugin Scanner",
        "2]  Path Enumeration",
        "3]  WP Enumeration",
        "4]  Emails Scanner",
        "5]  Ports Scanner",
        "6]  Subdomain Scanner",
        "7]  Wayback URLs",
        "8]  Help",
        "9]  Exit"
    ]
    
    for option in options:
        console.print(f"[bold cyan]│[/] {option}", style="bold white")
    
    console.print("─" * 65, style="bold white")
    console.print("Select an option by entering the corresponding number:", style="bold yellow")
    console.print("─" * 65, style="bold white")

# Display exit message with panel
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
    console.print("\n\nSession Off ...", style="bold red")
    exit()

# Display a random tip
def display_tip():
    tip = random.choice(TIPS)
    console.print(f"\n💡 {tip}", style="bold yellow")

# Execute the selected module
def execute_module(module_name):
    try:
        # Check if the module exists
        if not os.path.exists(f"module/{module_name}.py"):
            console.print(f"[!] Module '{module_name}.py' not found!", style="bold red")
            return

        # Adjust python command depending on system (python3 for Linux/Mac, python for Windows)
        python_cmd = "python3" if os.name != 'nt' else "python"
        console.print(f"Running {module_name} module...", style="bold green")

        # Progress bar during execution
        for _ in track(range(5), description=f"[cyan]Processing {module_name}..."):
            sleep(0.5)

        subprocess.run(f"{python_cmd} module/{module_name}.py", shell=True, check=True)

    except subprocess.CalledProcessError as e:
        console.print(f"[!] Error occurred while running {module_name}: {e}", style="bold red")
        console.print(f"Error details: {str(e)}", style="bold yellow")

# Handle the menu selection
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
        if selection == '9':
            print_exit_menu()
        elif selection == '8':
            console.print("\n[bold cyan]Help Menu: [/bold cyan]")
            console.print("1. WP Plugin Scanner: Scans WordPress plugins.", style="bold white")
            console.print("2. Path Enumeration: Enumerates paths.", style="bold white")
            console.print("3. WP Enumeration: General WordPress enumeration.", style="bold white")
            console.print("4. Emails Scanner: Scans emails.", style="bold white")
            console.print("5. Ports Scanner: Scans open ports.", style="bold white")
            console.print("6. Subdomain Scanner: Scans for subdomains.", style="bold white")
            console.print("7. Wayback URLs: Fetches URLs from Wayback Machine.", style="bold white")
            console.print("8. Help: Display this help menu.", style="bold white")
            console.print("9. Exit: Exits the program.", style="bold white")
        else:
            console.print(f"[+] Launching {module_map[selection].replace('_', ' ').title()}...", style="bold green")
            execute_module(module_map[selection])
            display_tip()  # Show random tip after execution
    else:
        console.print("[!] Invalid selection, please try again...", style="bold red")

# Main function for the program loop
def main():
    clear_screen()
    sleep(1)
    clear_screen()

    while True:
        display_menu()
        choice = input(f"\n{Fore.CYAN}[?] Please select an option (1-9): {Style.RESET_ALL}").strip()
        handle_selection(choice)

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_exit_menu()
        sys.exit(0)
