import os

def clear_screen():
    """
    Clears the terminal screen.

    This function uses the `os.system` command to clear the terminal screen.
    It works on Unix-based systems by executing the "clear" command.
    """
    os.system("clear" if os.name == "posix" else "cls")