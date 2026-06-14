print("DO YOU WANNA LEARN A NEW PROGRAMMING LANGUAGE?")

answer = input("YES OR NO: ").lower()

if answer == "yes":
    print("JAVASCRIPT OR PYTHON?")
    choice = input("JS OR PY: ").lower()

    if choice == "js":
        print("CONGRATULATIONS! YOU ARE LEARNING JS!")
        print("JSBUDDY GO AND LEARN!!!")

        decision = input(
            "What do you want to learn? basics, novice, or advanced: "
        ).lower()

        if decision == "basics":
            print("CodeWithHarry Basics Playlist")

        elif decision == "novice":
            print("CodeWithHarry Novice Playlist")

        elif decision == "advanced":
            print("CodeWithHarry Advanced Playlist")

        else:
            print("Invalid choice!")

    elif choice == "py":
        print("CONGRATULATIONS! YOU ARE LEARNING PYTHON!")
        print("PYBUDDY GO AND LEARN!!!!")

    else:
        print("Please choose JS or PY.")

elif answer == "no":
    print("THANKS FOR DESTROYING YOUR FUTURE!")

else:
    print("Please answer YES or NO.")