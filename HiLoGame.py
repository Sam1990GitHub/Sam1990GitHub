low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please ENTER to start")

guesses = 1
while low != high:
    #print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i "
                     "guess higher"
                     " or lower? "
                     "Enter H or L or C if guess is correct ".
                     format(guess)).casefold()
    if high_low == "h":
        #guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        #guess lower. the high end f the range becomes one less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got in it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    #guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
