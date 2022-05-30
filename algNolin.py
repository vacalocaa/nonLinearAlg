import math         #Se requiere math para aplicar raiz cuadrada de un número, aplicada en el módulo de Pk + 1 - Pk
import numpy as np  #Se requiere numpy para aplicar operaciones de matrices como suma, producto, inversa, etc
                    #Este modulo numpy no funciona con matrices de python propias, así que se hace que todas
                    #las matrices y listas de python que tienes se pasen a arrays de numpy con numpy.array


def pasos(x, y, z, w):
    Pk = np.array([[x], [y], [z], [w]]) #Un array que contiene los puntos xyzw

    f1 = (x*y) - y - z + w           #La primera ecuacion del sistema no lineal
    f2 = x - (y*z) + (x*w) - 2       #Segunda
    f3 = (y*w) + (z*w) - 1           #Tercera
    f4 = (x*y) - (z*w) - 1           #Cuarta

    J = np.array([[  y  ,(-1+x), -1 ,   1  ], #Matriz Jacobiana, array de 4 datos dentro de un array de 4 datos
                  [(1+w),   -z , -y ,   x  ], #osea, 16 datos en total.
                  [  0  ,    w ,  w , (y+z)],
                  [  y  ,    x , -w ,   -z]])

    matrizF = np.array([[f1], [f2], [f3],[f4]]) #Matriz de 4x1 del sistema no lineal aplicandole los valores xyzw

    Y =  np.dot(np.linalg.inv(J), -matrizF)     #Producto de matrices entre la inversa de la matriz Jacobiana
                                                #y, la matriz 4x1 del sistema no lineal multiplicada por escalar -1
                                                #Esto para conocer el valor de Y, vector solución del sistema lineal

    Pnew = np.add(Y, Pk)             #Suma entre la solucion Y, y el punto Pk para conocer el punto nuevo Pk + 1
    resta = np.add(Pnew, -Pk)        #Resta entre el punto nuevo y el punto Pk para luego aplicar el módulo

    # Se aplica el módulo sacando los valores de resta cada uno al cuadrado y sumandose, en una raiz.
    # Asi se saca el módulo de un vector
    mod = math.sqrt((resta[0][0] ** 2) + (resta[1][0] **2) + (resta[2][0] **2) + (resta[3][0] **2))

    #Se retornan los xyzw de Pk + 1, modulo, matriz Jacobiana, solución Y y la matriz de la solución no lineal
    return Pnew[0][0], Pnew[1][0], Pnew[2][0], Pnew[3][0], mod, J, Y, matrizF

it = 1      #Número de iteraciones
x0 = 10     #Valor entregado de xyzw
y0 = 10     #
z0 = 8      #
w0 = 8      #
t = 0.000001 #Valor de la tolerancia

while True:  #Loop eterno hasta que se encuentre que el módulo es mayor a la tolerancia

    print(f'Iteración {it}')                                    #Imprime por consola el numero de iteración actual
    print(f'Puntos (x, y, z, w) = ({x0}, {y0}, {z0}, {w0})')    #Puntos actuales
    tot = pasos(x0, y0, z0, w0) #Aplica la funcion con los valores de xyzw
    print(f'Vector F(P{it}):\n'                                 #Imprime Vector F(Pk)
          f'{tot[7]}\n')
    print(f'Matriz Jacobiana:\n'                                #Imprime Matriz Jacobiana
          f'{tot[5]}\n')
    print(f'Vector Solución Y:\n'                               #Imprime Vector Solución Y
          f' {tot[6]}')

    if tot[4] >= t:  #Si el Modulo (tot[4]) es mayor a la tolerancia, se sacan los valores del punto nuevo y se
                    #Aplica la función nuevamente con esos puntos
        print(f'Modulo Pk+1 - Pk = {tot[4]} , es mayor a la tolerancia\n\n') #Imprime Modulo de Pk + 1 - Pk
        x0 = tot[0] #xk (x0) ahora es xk+1
        y0 = tot[1] #yk (y0) ahora es yk+1
        z0 = tot[2] #zk (z0) ahora es zk+1
        w0 = tot[3] #wk (w0) ahora es wk+1
        it += 1     #Suma 1 a la iteración si se cambió el Punto

    else:          #Si el Modulo  (tot[4] es menos a la tolerancia o pasa cualquier otra cosa que no sea mayor
                   #en el if de arriba, se termina el loop con break
        print(f'Terminó de iterar con modulo: {tot[4]} e iteración {it} contando de iteración 1')
        #Imprime el módulo de termino y la iteración y rompe el loop.
        break

