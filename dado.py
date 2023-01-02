import random
class Dado:
    caras = []
    def __init__(self,car1,car2,car3,car4,car5,car6) :
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5
        self.car6 = car6
    def enlistar():
        Dado.caras.append(dado.car1)
        Dado.caras.append(dado.car2)
        Dado.caras.append(dado.car3)
        Dado.caras.append(dado.car4)
        Dado.caras.append(dado.car5)
        Dado.caras.append(dado.car6)
    def tirar():
        return random.choice(Dado.caras)



dado = Dado(1,2,3,4,5,6)
