import random
from instant_input_func import instant_input

DEFAULT_ARROW_KEYS = {
    "\x1b[A": "up",
    "\x1b[B": "down",
    "\x1b[C": "right",
    "\x1b[D": "left",
    " ": "space"
}

right_left_mapped = {
    "right": "left",
    "left": "right"
}

while True:
    right_or_left = random.choice(["right", "left"])

    print("You are in a coridoor, do you go left or right?")
    direction = instant_input("> ", timeout=5, special_keys=DEFAULT_ARROW_KEYS)
    print()
    if direction == right_or_left:
        print("You have fallen to your death")
        break
    elif direction == right_left_mapped[right_or_left]:
        print(f"You made a run towards the {right_or_left} coridoor successfully")
        continue
    elif direction == "space":
        print("You jumped over the ferocious monster")
    elif direction == "no key pressed":
        print("The monster devoured you")
        break
    else:
        print("Ahh! You're a genius, you've won")
        exit()
print("The game is over, you've failed!")