def factorial(N):
    """Retorna una lista de factoriales desde 0! hasta N!. Por ejemplo:
     factorial(5) -> [1,1,2,6,24,120]
    """
    f=1 
    return [1 if n==0 else (f:=f*n) for n in range(N+1)]

import numpy as np

def factorial_numpy(N, dtype=np.int32):
    """Retorna un arreglo de numpy de factoriales desde 0! hasta N!.
    El argumento 'dtype' controla la presición
    f.cumprod(dtype=dtype) retornará el producto de todos los elementos hasta el i-ésimo 
    y guarda el resultado en el i-ésimo lugar con la presición escogida.
    Ejemplos:
    factorial_numpy(5)    ->    array([1,1,2,6,24,120]), dtype=int32
    factorial_numpy(5, dtype=np.int64)   ->   array([1,1,2,3,24,120]), dtype=int64
    """
    f = np.arange(N+1, dtype=dtype)
    f[0] = 1
    return f.cumprod(dtype=dtype)

def catalan(N):
    """Entrega una lista con los primeros N+1-ésimos números de Catalán, usando la 
    función factorial predefinida. Se crea una lista vacía y se van agregando los 
    números de Catalán mediante un ciclo for.
    Ejemplos: 
    catalan(1)   ->   [1.0, 1.0]
    catalan(5)   ->   [1.0, 1.0, 2.0, 5.0, 14.0, 42.0]
    """
    lista = []
    q = factorial(2*(N+1)) 
    for i in range(N+1):
        lista.append(q[2*i] / (q[i+1] * q[i]))
    return lista

def catalan_numpy(N, dtype=np.float128):
    """Entrega un arreglo de numpy con los primeros N+1-ésimos números de Catalán usando
    la función factorial_numpy predefinida.
    Ejemplos:
    catalan_numpy(1) -> array([ 1., 1. ], dtype=np.float128)
    catalan_numpy(4) -> np.array([ 1., 1., 2., 5., 14. ], dtype=np.float128)"""
    q = factorial_numpy(2*N, dtype = dtype)
    return q[::2] / ( q[1:N+2] * q[:N+1] )


def cat_rec(N, dtype=np.int32):
    """ Retorna un arreglo de numpy con los primeros N+1-ésimos números de Catalán
    utilizando la relación de recurrencia C_0=1, C_n = (4n+2)/(n+2) * C_n
    Ejemplos:
    cat_rec(1)  ->  array([1, 1])
    cat_rec(4, dtype=np.int16)  -> array([ 1, 1, 2, 5, 14], dtype=int16)
    """
    C = np.zeros(N+1, dtype=dtype) #arreglo donde se almacenarán los números
    C[0] = 1.0  #definimos el caso base C_0=0 como el primer elemento
    
    for i in range(N):
        C[i+1] = (4*i +2) / (i+2) * C[i] #se calculan los demás elementos con la
    return C                             #relación de recurrencia con un ciclo for
      
print(catalan_numpy(16, dtype=np.int16 ))
