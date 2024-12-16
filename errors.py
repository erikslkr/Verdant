from termcolor import colored

def driver_warning(message):
    warning = colored("Warning: ", "yellow", attrs=["bold"])
    message = colored(message, "yellow")
    print(f"{warning}{message}")

def driver_error(message):
    error = colored("Error: ", "red", attrs=["bold"])
    message = colored(message, "red")
    print(f"{error}{message}")
