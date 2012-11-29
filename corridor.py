def corridor():
    print "You hear a loud moan from the rooms down the corridor"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.")
    if answer == "LEFT" or answer == "Left" or answer == "left":
        print "You enter, and to your horror you see a Zombie"
    elif answer == "RIGHT" or answer == "Right" or answer == "right":
        print "Bingo, you find a polish girl, all alone"
    else:
        print "You didn't pick left or right! Try again."
        corridor()

corridor()
