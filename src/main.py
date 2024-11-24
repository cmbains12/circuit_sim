# main.py

import sys
from drawing import Screen

def main():
    print("Electrical Circuit Simulation Program")

    # Create a Screen object with a width of 800 and a height of 600
    screen = Screen(800, 600)

    # Run the Screen object
    screen.run()




if __name__ == "__main__":
    main()
