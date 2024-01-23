import time
import os
from py_digital_clock import digital_clock

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(digital_clock())
        print(digital_clock("de_DE"))
        print(digital_clock("fr_FR"))
        time.sleep(1)

if __name__ == "__main__":
    main()
