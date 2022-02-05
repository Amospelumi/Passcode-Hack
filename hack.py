from random import randint

passcode = 7824

i = 0
count = 0

while i < 1:
    guess = randint(100, 9999)
    print("Hacking")
    count += 1
    if guess == passcode:
        print (f"Hacking complete, the password is: {guess}  it took {count} triald" )
        break

