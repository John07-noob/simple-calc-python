def inputNumber(number):
    while True:
        try:
            userInput = int(input(number))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break
