import math



def isitprime(n):

    if n == 2 or n == 3 : return True, print("Es primo")
    if n < 2 : return False, print("NO Es primo 1 ")
    
    if n %2 == 0 : return False , print("NO Es primo 2")

    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False, print("No es primo 3")


    return True, print("Es primo 2")



n = int(input("Ingresar numero a evaluar: "))


isitprime(n)
