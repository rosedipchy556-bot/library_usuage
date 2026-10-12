from colorama import Fore, Style, init

init(autoreset=True)

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

print(Fore.CYAN + f"\nStudent Name: {name}")

if marks >= 40:
    print(Fore.GREEN + "Result: Pass")

else:
    print(Fore.RED + "Result: Fail")

print(Style.RESET_ALL + "Report completed.") 