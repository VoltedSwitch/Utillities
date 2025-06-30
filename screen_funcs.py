import os


def clear_screen():
    """
    Clears the terminal screen.

    This function uses the `os.system` command to clear the terminal screen.
    It works on Unix-based systems by executing the "clear" command.
    """
    os.system("clear" if os.name == "posix" else "cls")


def hide_cursor():
    """
    Hides the terminal cursor using ANSI escape codes.
    """
    print("\033[?25l", end="", flush=True)


def show_cursor():
    """
    Shows the terminal cursor using ANSI escape codes.
    """
    print("\033[?25h", end="", flush=True)
