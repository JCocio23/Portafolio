import numpy as np 
import matplotlib.pyplot as plt

###### #PRIMER EJERCICIO DE LA PARTE 2

def ejercicio_1():
    n = np.random.randint(1, 100) #Toma un valor n random
    print(np.random.randint(1,n,n)) #Imprime el array

#ejercicio_1()

####### #SEGUNDO EJERCICIO DE LA PARTE 2

def ejercicio_2():
    matriz = np.ones((3,5), dtype=complex) #Genera una matriz 3x5 de 1s
    for i in range(0,3):
        for a in range(0,5):
            matriz[i,a] = complex(np.random.random(1),np.random.random(1))
    print("La matriz entera es:\n",matriz) #Imprime la matriz entera
    print("La primera fila de la matriz es: \n",matriz[0]) #Imprime la primera fila 
    print("La última fila de la matriz es: \n",matriz[1]) #Imprime la última fila 
    print("El término central de la matriz es:\n",matriz[1,0]) #Imprime el elemento central de la matriz

#ejercicio_2()

###### #TERCER EJERCICIO DE LA PARTE 2

def ejercicio_3(n):
    
    serie = np.random.randint(1,100,n) #Crea un array de N números aleatorios enteros del 1 al 100
    print("La serie es:", serie) #Imprime la serie generada

    diferencia = np.zeros(n-1)
    for i in range(0,len(serie) - 1):
        diferencia[i] = serie[i+1] - serie[i]
    
    print(diferencia, "Es la serie usando un ciclo for.")
    print(serie[1:] - serie[:-1],"Es la serie hecha con la propiedad vectorizada de arrays.") #Imprime la nueva serie usando propiedades vectorizadas

ejercicio_3(10)

######## #CUARTO EJERCICIO DE LA PARTE 2

def ejercicio_4():
    x=[]
    for i in range(200):
        x.append(np.random.uniform(-2*np.pi, 2*np.pi))
    for i in range(len(x)):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    print(x)
    x = np.array(x)
    plt.plot(x, np.cos(x))
    #plt.plot(np.arange(-2*np.pi,2*np.pi,0.1),np.cos(np.arange(-2*np.pi,2*np.pi,0.1)))
    # Comparar con el coseno para ver si es parecido
    plt.show()

#ejercicio_4()
