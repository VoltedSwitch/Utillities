import sys
import termios
import tty
import select

ARROW_KEYS = {
    "\x1b[A": "up",
    "\x1b[B": "down",
    "\x1b[C": "right",
    "\x1b[D": "left",
    " ": "space"
}

def instant_input(prompt, timeout=None):
    print(prompt, end="", flush=True)

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)

        if timeout:
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)
            if not rlist:
                return "no key pressed"

        key_pressed = sys.stdin.read(1)  # Read one character

        # Handle escape sequences for arrow keys
        if key_pressed == "\x1b":
            key_pressed += sys.stdin.read(2)  # Read the next two bytes

        # Always check the key against the ARROW_KEYS mapping
        return ARROW_KEYS.get(key_pressed, key_pressed)  # For normal or special keys

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
