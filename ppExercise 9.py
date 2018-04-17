import random


for x in range(1):
  secreto= (random.randint(1,9))

usertries = 0

while True:



    userguess = input("Que número crees que es? : ")


    if int(userguess) == secreto :
        print ("Adivinaste! lo hiciste en " , usertries , "intentos")
        break
    elif int(userguess) > secreto:
        print("Demasiado alto!")
        usertries += 1
    else:
        print("Demasiado bajo!")
        usertries += 1
