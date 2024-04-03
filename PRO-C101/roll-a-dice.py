import random

class DiceSimulator:
    def roll_dice(self):
        return random.randint(1, 6)

    def display_dice(self, value):
        if value == 1:
            print("---------")
            print("|       |")
            print("|   •   |")
            print("|       |")
            print("---------")
        elif value == 2:
            print("---------")
            print("| •     |")
            print("|       |")
            print("|     • |")
            print("---------")
        elif value == 3:
            print("---------")
            print("| •     |")
            print("|   •   |")
            print("|     • |")
            print("---------")
        elif value == 4:
            print("---------")
            print("| •   • |")
            print("|       |")
            print("| •   • |")
            print("---------")
        elif value == 5:
            print("---------")
            print("| •   • |")
            print("|   •   |")
            print("| •   • |")
            print("---------")
        elif value == 6:
            print("---------")
            print("| •   • |")
            print("| •   • |")
            print("| •   • |")
            print("---------")

    def run(self):
        response = 'y'

        while response.lower() == 'y':
            value = self.roll_dice()
            self.display_dice(value)

            response = input("Y to roll again N to exit (y/n): ")

        print("Thanks for rolling!")

if __name__ == "__main__":
    dice_simulator = DiceSimulator()
    dice_simulator.run()
