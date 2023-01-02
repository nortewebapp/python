import random
class Juego:
    def init():
        numeros = [1,2,3,4,5,6,7,8,9,10]
        jugador = int(input('ingrese un numero del 1 a al 10: '))
        com = random.choice(numeros)
        index = random.choice(numeros)
        print(f'''el numero a igualar es {index}
                El usuario ingreso {jugador}
                La pc escogio {com}
        ''')
        if jugador == index:
            print('el ganador es el usuario')
        elif com == index:
            print('Gana la pc')
        else:
            print('ninguno de los dos acerto, es un empate') 


