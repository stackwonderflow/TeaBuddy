import sys
import os
import time

from art import teaCup

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def main():

    running = True

    while running:

        cls()
        print(teaCup)
        print(
            "Welcome to TeaBuddy, your friendly tea assistant!\nWhat kind of tea are you in the mood for?\n\n1. Black\n2. Green\n3. White\n4. Oolong\n5. Pu'er\n6. Herbal\n7. Rooibos\n8. Tisane\n9. Other\n10. Exit\n"
            )
        
        teaChoice = input("Enter desired tea number:")

        try:
            teaChoice = int(teaChoice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        time.sleep(1)

        if teaChoice == 1:
            cls()
            print(
                "You chose black tea!\nDepending on varietal, black tea is brewed at 93 to 100 degrees Celsius for 3 to 5 minutes.\nBlack teas generally have a higher caffeine content than other teas, so drink responsibly."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 2:
            cls()
            print(
                "You chose green tea!\nDepending on varietal, green tea is brewed at 60 to 85 degrees Celsius for 2 to 3 minutes.\nGreen teas generally have a lower caffeine content than black teas."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 3:
            cls()
            print(
                "You chose white tea!\nDepending on varietal, white tea is brewed at 70 to 85 degrees Celsius for 2 to 3 minutes.\nWhite teas generally have a lower caffeine content than green or black teas."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 4:
            cls()
            print(
                "You chose oolong tea!\nDepending on varietal, oolong tea is brewed at 85 to 95 degrees Celsius for 3 to 5 minutes.\nOolong teas generally have a moderate caffeine content."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 5:
            cls()
            print(
                "You chose pu'er tea!\nDepending on varietal, pu'er tea is brewed at 85 to 100 degrees Celsius for 2 to 5 minutes.\nPu'er teas generally have a moderate caffeine content."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 6:
            cls()
            print(
                "You chose herbal tea!\nDepending on varietal, herbal tea is brewed at 85 to 100 degrees Celsius for 3 to 5 minutes.\nHerbal teas generally have little to no caffeine."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 7:
            cls()
            print(
                "You chose rooibos tea!\nRooibos is brewed at 95 to 100 degrees Celsius for 5 to 7 minutes.\nRooibos generally has little to no caffeine."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 8:
            cls()
            print(
                "You chose tisane!\nTisanes are brewed at 85 to 100 degrees Celsius for 3 to 5 minutes.\nTisanes generally have little to no caffeine."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 9:
            cls()
            print(
                "You chose other tea!\nSince you chose other, I'll let you choose the temperature and steeping time."
                )
            time.sleep(1)
            timeChoice = input("Enter desired steeping time in minutes: ")

            try:
                timeChoice = int(timeChoice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            cls()
            teaTimer(timeChoice)

        elif teaChoice == 10:
            cls()
            print("Goodbye!")
            running = False

def teaTimer(timeChoice):
    for i in range(timeChoice):
        print(f"Steeping time remaining: {timeChoice - i} minutes")
        time.sleep(1)
    print(teaCup)
    print("Tea is ready!")

    time.sleep(1.5)
    cls()
    print(
        "Would you like to brew another cup?"
    )
    brewAgain = input("1. Yes\n2. No\n")

    try:
        brewAgain = int(brewAgain)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if brewAgain == 1:
        main()
    elif brewAgain == 2:
        print("Goodbye!")
        exit()

if __name__ == "__main__":
    main()
