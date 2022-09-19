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

#user input

userChoice = input('rock,paper, or scissors?').lower()


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
