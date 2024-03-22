#Ruchitha008
#March2024
points = 0
print("WELCOME TO THE QUIZ!")
playing = input("Do you want to play?")
if playing.lower()!="yes":
    quit()

print("Okay! Let's play :)")

#question
answer = input("WHAT DOES CPU STAND FOR? ")

if answer == "central processing unit":
    print("Correct")
    points+=1
else:
    print("Incorrect")

#question
answer = input("WHAT DOES GPU STAND FOR? ")

if answer == "graphics processing unit":
    print("Correct")
    points+=1
else:
    print("Incorrect")

#question
answer = input("WHAT DOES RAM STAND FOR? ")

if answer == "random access memory":
    print("Correct")
    points+=1
else:
    print("Incorrect")

#question
answer = input("WHAT DOES PSU STAND FOR? ")

if answer == "power supply":
    print("Correct")
    points+=1
else:
    print("Incorrect")

print("Congratulations!! Your total score is " + str(points))
print("You got " + str((points)/4 * 100) + "%.")
