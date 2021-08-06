print("Welcome to the quiz!!")

playing=input("Do u want to play quiz?  ")

if playing.lower() != "yes" :
    quit()

print("Lets play the quiz : ) ")

score=0

answer= input(" 1) what does CPU stands for?  ")
if answer.lower() == "central processing unit" :                    #1
    print("correct!")
    score += 1
else:
    print("Incorrect!")


answer= input(" 2) what does GPU stands for?  ")
if answer.lower() == "graphic processing unit" :                    #2
    print("correct!")
    score += 1
else:
    print("Incorrect!")


answer= input(" 3) what does RAM stands for?  ")
if answer.lower() == "random access memory" :                       #3
    print("correct!")
    score += 1
else:
    print("Incorrect!")


answer= input(" 4) what does SQL stands for?  ")
if answer.lower() == "structured query language" :                  #4
    print("correct!")
    score += 1
else:
    print("Incorrect!")


answer= input(" 5) what does rom stands for?  ")
if answer.lower() == "read only memory" :                           #5
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("you got  " + str(score) + "  Answers correct!")
print("you got  " + str((score/5)* 100) + "%")