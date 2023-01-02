import random


class Mano:
    lista = []
    # eleccion = str.lower(input('ingrese piedra, papel o tijera: '))
    
    def __init__(self, forma):
        self.forma = forma
    
    def enlistar():
        Mano.lista.append(piedra.forma)
        Mano.lista.append(papel.forma)
        Mano.lista.append(tijeras.forma)
    
    def juego_ppt():
        print('jugando a piedra, papel o tijeras')
        
        print(f'{com.nombre} elige {com.elec}')
        print(f'{humano.nombre} elige {humano.elec}')
        if humano.elec == 'piedra' and com.elec == 'tijera':
            print('gana el usuario')
        elif com.elec == 'piedra' and humano.elec == 'tijera':
            print('gana la computadora')
        elif humano.elec == 'papel' and com.elec == 'piedra':
            print('gana el usuario')
        elif com.elec == 'papel' and humano.elec == 'piedra':
            print('gana la computadora')
        elif humano.elec == 'tijera' and com.elec == 'papel':
            print('gana el usuario')
        elif com.elec == 'tijera' and humano.elec == 'papel':
            print('gana el usuario')
        else:
            print('tenemos un empate!!')
        

class Jugadores:
    
    def __init__(self,tipo,nombre,elec):
        self.tipo = tipo
        self.nombre = nombre
        self.elec = elec
        



piedra = Mano('piedra')
papel = Mano('papel')
tijeras = Mano('tijera')
Mano.enlistar()


humano = Jugadores('humano', 'usuario',random.choice(Mano.lista))
com = Jugadores('maquina', 'computadora',random.choice(Mano.lista))




