import random
import time

#varibles
yesno = ['yes','no']
yesNoGiven = False

colorPicked = False
colors = ['red','blue','green','purple']

numberPicked = False
numberRange = range(1,7,1)

#add red length (red 3, blue 4, green 5, purple 6)
#add depending on length of color character this number option are given
#add number (1:7) where if red or blue are pick select from 1,3,5. if green or purple are picked select numbers from 2,4,6

fortunes = ['You are going to South Padre Island', 'You are going to Big Bend National Park!', 'You are going to Barton Springs Pool', 'You are going to Guadalupe Mountains National Park',
           'You won a free vacation from TDL \U0001f604']
print(fortunes)

def travelGame():
#while loop#

    while not yesNoGiven:
      loopQ = input("Would you like me to tell you where your next trip will be?")
      if loopQ.lower() in ['yes','y']:
        yesNoGiven = True
        print("Great! Next please pick a color.")

      elif loopQ.lower() in ['no', 'n']:
        print("You deserve a trip!")
      else:
        print("try again")

    while not colorPicked:
        colors = ['red','blue','green','purple']
        colorpick = input("Pick from red, blue, green, or purple:")

        if colorpick.lower() in colors:
          colorPicked = True
          print("Awesome, now pick a number!")
        else:
          print("Pick a color from the list.")

    while not numberPicked:
      numberPick = int(input("Pick from 1 to 6."))
      if numberPick in numberRange:
        numberPicked = True
        print('Awesome, here is your travel fortune!')
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(.5)
        print("...")
        print(random.choice(fortunes))
      else:
        print("Come on!")
