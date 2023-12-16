'''
This script prints the lyrics of the song "Hey Jude" by The Beatles.
It uses a while loop to iterate through the verses and conditionals to determine the lyrics for each verse.
The script also includes an additional section that prints a repeated chorus after the third verse.
'''

# Control variable for the while loop
verse = 0

# Iterates through the verses
while verse < 3:
    verse += 1
    print("Hey Jude, don't ")

    if verse == 1:
        print("make it bad")
        print("take a sad song and make it better")
    elif verse == 2:
        print("be afraid")
        print("you were made to go on and get her")
    elif verse == 3:
        print("let me down")
        print("you have found her, now go and get her")

    print("remember to let her ")

    # Tests if verse is odd or even
    if verse % 2 == 1:
        print("into your heart")
    else:
        print("under your skin")

    print("then you ")

    if verse % 2 == 1:
        print("can start")
    else:
        print("begin")

    print("to make it better")

# Prints final chorus after the third verse
if verse == 3:
    print("better better better better BETTER WAAAAAAAAAAAA")
    infinity = 0
    while infinity < 100:
        print("NA NA NA NANANA NAAAAAAA")
        print("NANANA NAAAAAAA")
        print("Hey Jude")
        infinity += 1
