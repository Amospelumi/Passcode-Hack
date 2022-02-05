from random import randint

# prompting to input the correct passcode.
passcode = int(input("Input the Correct passcode: "))

# declare the variable for the while loop and also the count variable to get the number of trial before hacking the code.
i = 0
count = 0

# Passcode hacking while loop start.
while i < 1:
    guess = randint(100, 9999)
    print("Hacking")
    count += 1
    if guess == passcode:
        print(f"""
        Passcode Successfully Hacked!
        The password is: {guess}.
        it took {count} trials to get the pascode hacked.""")
        break

