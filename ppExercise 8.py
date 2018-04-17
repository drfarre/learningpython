while True:

        jugada_p1 = input("Jugada jugador 1: ")

        jugada_p2 = input("Jugada jugador 2: ")


        if jugada_p1 == "piedra" and jugada_p2 != "piedra" :
            if jugada_p1 == "piedra" and jugada_p2 != "papel" :
                print("Gana player 1, felicitaciones!!")
            else:
                print("Gana player 2, felicitaciones!!")

        elif jugada_p1 == "papel" and jugada_p2 != "papel" :
            if jugada_p1 == "papel" and jugada_p2 != "tijera":
                print ("Gana player 1, felicitaciones!!")
            else:
                print("Gana player 2 , felicitaciones!")
        elif jugada_p1 == "tijera" and jugada_p2 != "tijera":
            if jugada_p1 == "tijera" and jugada_p2 != "piedra" :
                print("Gana player 1, felicitaciones!")
            else:
                print("Gana player 2, felicitaciones!!")



        usr_command = input("Desea seguir jugando? tipee NO para salir ")
        if usr_command == "NO":
            break
        else:
            print("Seguimos jugando")
