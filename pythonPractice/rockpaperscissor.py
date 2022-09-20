import random

hand = {
"rock":'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
"paper":'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
"scissor":'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

#looping games so that you can continue playing
while True:
    #user input
    userChoice = input('rock,paper, or scissor?').lower()

    #trying to catch wrong input
    try:
        userChoice == hand[userChoice]
    except KeyError:
        print ("Wrong Input!")
        continue

    #Computer choice we gonna put the keys of the dictionaries into a lists
    r = random.choice(list (hand.keys()))

    #print (hand[r]) #the computer choice

    if userChoice ==r:
        print("Draw!")
    elif userChoice == 'paper' and r == 'scissors':
        print("You have lost!")
    elif userChoice == 'scissor' and r == 'rock':
            print("You have lost!")
    elif userChoice == 'rock' and r == 'paper':
        print("You have Lost!")
    else:
        print ("You have won!")

    print ("Computer: " + hand[r]) #the computer choice
    print ("You: " + hand[userChoice])

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break 
        
