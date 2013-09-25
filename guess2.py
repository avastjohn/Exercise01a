from random import randint

print "Hi. What's your name?"
name = raw_input("> ")
print "Well, %s, I have a number between 1 and 100. Care to guess?" % name

def number_game():
    guess = raw_input()
    number = randint(1, 101)
    guess_count = 0

    if guess.isdigit():
        while number != int(guess):
            if int(guess) < number:
                print "Nope. Guess higher."
            else:
                print "Nope. Guess lower."
            guess = raw_input()
            guess_count += 1

        print "That's correct! My number was %d" % number
        print "It only took you %d guesses!" % guess_count
    else:
        guess = raw_input("I asked for a number.  Please type in a number. ")


number_game()
print " "
play_again = raw_input("Play again? y/n")

if play_again == "y":
    print "Ok! I've got a new number. Guess away!"
    number_game()