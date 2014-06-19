#!/usr/bin/python
# -*- coding: utf-8 -*-

#Estructura Estado_Actual;Simbolo_Actual_Del_Cabezal;Estado_Siguiente;
#Simbolo_a_Escribir;Direccion_De_Avance
#D: movimiento derecha - I: Movimiento izquierda

class Turing:

    def __init__(self):
        self.eIni = ""
        self.eFin = ""


    def llenarMatriz(self, matriz, fil, col, ent):
        M = matriz
        F = fil
        C = col
        pos1 = 0
        pos2 = 0
        aux = self.sepTupla(ent)
        for i in aux:
            aux2 = self.sepElem(i)
            cont1 = 0
            cont2 = 0
            for a in F:  # Obteniendo posiciones de cada transicion
                if aux2[0] == a:
                    pos1 = cont1
                cont1 = cont1 + 1
            for b in C:
                if aux2[1] == b:
                    pos2 = cont2
                cont2 = cont2 + 1
            M[pos1][pos2] = aux2[2], aux2[3], aux2[4]  # Agregando a la matriz
        for w in M:
            print w



    def dimMatriz(self, entrada0):
        n = 5
        m = 0
        dim = ""
        aux = self.sepTupla(entrada0)
        for i in aux:
            aux2 = self.sepElem(i)
            if dim < aux2[2]:
                dim = aux2[2]
            m = int(dim[1])
        Matriz = [["**************" for x in xrange(n)] for x in xrange(m+1) ]
        Estados = [0 for x in xrange(m+1) ]
        Simbolos = [0 for x in xrange(n)]
        c1 = 0
        c2 = 0
        for j in aux:
            aux2 = self.sepElem(j)
            if aux2[2] not in Estados:  # llenando la Estados sin repeticiones
                Estados[c1] = aux2[2]
                c1 = c1 + 1
            if aux2[1] not in Simbolos:  # Llenando Simbolos sin repeticiones
                Simbolos[c2] = aux2[1]
                c2 = c2 + 1
        Estados.sort()  # ordenando estados
        return (Matriz, Estados, Simbolos)








    def sepTupla(self, entrada1):
        sepT = entrada1.split(';')
        return (sepT)

    def sepElem(self, entrada2):
        sepEl = entrada2.split(',')
        return (sepEl)

Turing1 = Turing()
x = "q0,0,q1,x,D;q1,0,q1,0,D;q2,0,q2,0,I;q1,1,q2,y,I;q2,x,q0,x,D;q0,y,q3,y,D;q1,y,q1,y,D;q2,y,q2,y,I;q3,y,q3,y,D;q3,b,q4,b,F"
(dim, filas, columnas) = Turing1.dimMatriz(x)
Turing1.llenarMatriz(dim, filas , columnas, x)


#Javier: si haras algo con este archivo respaldalo xD
#Basicamente lo que hace es q segun esa gigantesca cadena determinar las tuplas
#y a que corresponde cada dato
#Una forma facil de comprobar que la matriz de Transiciones funciona, basta con
#cambiar cualquier estado inicial de una tupla (ya que ese indica la fila a la
#que corresponde y al ejecutarlo te mostrara la 3tupla en la fila que indicaste
#Ejemplo que en la 4ta 5tupla cambie el q1 inicial por q4 y lo ejecute :B
#Aviso: si cambias estado y lo que lee tienes que verificar que estas destinando a un espacio disponible de la matriz
#ya que si no la transicion se movera reemplazando la existente...3tupla
#Me voy al sobre xD
#PD: no es mucho el codigo pero PUTA que fue webeo hacerlo funcionar sin sin que crasheara xD
#cosa de cachar la hora a la que vine a terminar jajaa xD

