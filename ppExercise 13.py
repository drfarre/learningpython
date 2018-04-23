numbers = input("How many numbers to generate? :")

contador = int(0)
s_primer_num = int(0)
s_segundo_num = int(1)

def suma_num ():
    global contador,s_segundo_num,s_primer_num
    while contador < int(numbers):
        numero = int(s_primer_num + s_segundo_num)
        print(numero)
        s_primer_num = s_segundo_num
        s_segundo_num = numero
        contador = int(contador + 1)
    return

suma_num()
