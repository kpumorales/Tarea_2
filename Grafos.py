#!/usr/bin/env python3
import os

#Se crea la clace vertice que solo tiene como argumento su nombre.

class Vertice(object):

 def __init__(self, n):

  self.nombre = n



#Se crea la clase grafo con vertices e indices de aristas como diccionarios y aristas como una lista.

class Grafo(object):

 vertices = {}
 aristas = []
 indices_aristas = {}
 color = '\033[0;37;46m'
 ENDC = '\033[0m'



 def agregarVertice(self,vertice):

  #Si vertice es una instancia de su clase y su nombre no esta en el diccionario de vertices se agrega.

  if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:

   self.vertices[vertice.nombre] = vertice

   #Se recorre las aristas y se agregan.

   for fila in self.aristas:

    fila.append(0)

   self.aristas.append([0] * (len(self.aristas)+1))

   self.indices_aristas[vertice.nombre] = len(self.indices_aristas)

   return True

  else:

   return False



 def agregarArista(self,u,v, peso=1):

  #Se agrega el arista.

  if u in self.vertices and v in self.vertices:

   self.aristas[self.indices_aristas[u]][self.indices_aristas[v]] = peso

   self.aristas[self.indices_aristas[v]][self.indices_aristas[u]] = peso

   return True

  else:

   return False

'''
 def printGrafo(self):
  os.system('clear')
  #Se muestra el grafo
  print('Representado como matriz')
  print ('  ',end= "")
  for v, i in sorted(self.indices_aristas.items()):
    print(v, end =" ")
  print(' ')
  for v, i in sorted(self.indices_aristas.items()):
   print(v, end='')
   for j in range(len(self.aristas)):
    print('',{True: self.color+'1'+self.ENDC, False: '0'}[self.aristas[i][j] == 1], end='')
   print(' ')    
'''
def printGrafo(self):

  #Se muestra el grafo

  for v, i in sorted(self.indices_aristas.items()):

   print(v + ' ', end='')

   for j in range(len(self.aristas)):

    print(self.aristas[i][j], end='')

   print(' ')


if __name__ == '__main__':
  aristas=[]
  vertices2=[]
  g = Grafo()
  NA =  int(input('Cuantas aristas hay?: '))
  for i in range(NA):
    arista = input('Escribe los indices de los vertices ( ejemplo: "12") ')
    aristas.append(arista)

  for i in range(len(aristas)):
    x= aristas[i]
    for item in list(x):
      if not item in vertices2:
        vertices2.append(item)

  for item in vertices2:
    g.agregarVertice(Vertice(str(item)))  

  for arista in aristas:
    g.agregarArista(arista[:1],arista[1:])

  g.printGrafo()