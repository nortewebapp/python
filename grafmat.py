import matplotlib.pyplot as plt
class Graficos:
        X = []
        Y = []
        def funcion(x):
            return (30-20*x)/30
        def enlistar():
            for x in range(20):
                y = Graficos.funcion(x)
                Graficos.X.append(x)
                Graficos.Y.append(y)
        def Graficar():
            plt.plot(Graficos.X, Graficos.Y)
            plt.show()




