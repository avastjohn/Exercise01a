from random import randint

print "Hi. What's your name?"
name = raw_input("> ")
print "Well, %s, I have a number between 1 and 100. Care to guess?" % name

guess = int(raw_input())
number = randint(1, 101)
guess_count = 0

while number != guess:
    if guess < number:
        print "Nope. Guess higher."
    else:
        print "Nope. Guess lower."
    guess = int(raw_input())
    guess_count += 1


print "That's correct! My number was %d" % number
print "It only took you %d guesses!" % guess_count