import p_p_t as ppt
import an 
import dado
import grafmat as gr
import time

def menu():
        return int(input('''
                                Jugar piedra,papel o tijeras = 1
                                Jugar eleccion de numeros = 2
                                Tirar dado = 3
                                Graficar funcion = 4
                                Salir = 5
                                Cual es tu eleccion? 
                                                                '''))
init = menu()   
if init == 1:
        ppt.Mano.juego_ppt()
        time.sleep(2)            
elif init == 2:
        an.Juego.init()
        time.sleep(2)
elif init == 3:
        dado.Dado.enlistar()
        print(f'al tirar el dado cae {dado.Dado.tirar()}')
        time.sleep(2)
elif init == 4:
        gr.Graficos.enlistar()
        gr.Graficos.Graficar()
        time.sleep(2)
elif init == 5:
        print('gracias por jugar')        
else:
        print('ingresaste un numero no valido')
