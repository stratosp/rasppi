import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
right_button = 14
left_button = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)

print ("Let's play a game!")
time.sleep(1)

input("Click any button to begin...")

left_name = input("Left player name is ")
right_name = input("Right player name is ")
names = [left_name, right_name]
left_points = 0
right_points = 0
points = [left_points, right_points]

rounds = input("How many rounds would you like to play?")
num_rounds = int(rounds) 
for i in range(1, num_rounds + 1):
    print ("Round " + str(i) + ".")
    time.sleep(3)

    GPIO.output(led,1)

    time.sleep(random.uniform(5,10))

    GPIO.output(led,0)

    while True:
        if GPIO.input(left_button) == False:
            print (names[0] + " won")
            points[0] += 1
            break
        if GPIO.input(right_button) == False:
            print (names[1] + " won")
            points[1] += 1
            break
print("Game over!")
print(names[0]+ ": " + str(points[0]) + ", " + names[1] + ": " + str(points[1]) + ".")

GPIO.cleanup()
