from random import randint 
""" 
  1.     Generar una lista de números enteros aleatorios: Desarrollar una función que genere de manera aleatoria una lista de 50 números enteros positivos entre 1 y 100.
"""

def enteros_aleatoreos ():
  numeros_aleatoreos = []
  for i in range(50): 
    numeros_aleatoreos.append(randint(1, 100))
  return numeros_aleatoreos

""" 
  2.   Generar una matriz de caracteres alfanuméricos: Desarrollar una función que genere de manera aleatoria una matriz de 6 filas por 15 columnas (6 listas de 15 elementos cada una), compuesta de caracteres alfanuméricos (letras y dígitos).
"""

def caracteres_alfanumericos ():
  matriz = []
  alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',' V', 'W', 'X', 'Y', 'Z']
  for i in range(6):
    fila = []
    for j in range (15):
      print(i, 'i')
      print(j, 'j')
      alfa_o_numero = randint(1,10)
      if alfa_o_numero % 2 == 0: 
        letra = randint(0, 26)
        fila.append(alpha[letra])
      else :
        fila.append(randint(1, 100))
        
        
      fila.append(j)
    matriz.append(fila)
  return matriz

""" 
  3.  Ordenar una lista de números enteros: Desarrollar una función que ordene una lista de números enteros, recibiendo como parámetro el criterio de ordenamiento "ASC" o "DESC" (ascendente o descendente).
"""
def ordenar_enteros(lista: list, param: str): 
  if param == 'ASC': 
    # Ordenar de manera ascendente
    print('asc')
    for i in range(len(lista)):
      print(i, 'i')
      for j in range(len(lista)):
        print(int(j) + 1, 'j')
        if int(j) + 1 < len(lista):
          if lista[i] > lista[int(j) + 1]:
            valor_j = lista[int(j) + 1]
            lista[int(j) + 1] = lista[i]
            lista[i] = valor_j
          """ print(lista[int(j) + 1], 'index')
          

          j + 1
          i + 1 """
  else :
    print('DESC')
    # Ordenar de manera descendente

  return lista

""" ordenar_enteros('ASC') """

"""  
  4. Validar el ingreso de una cadena alfanumérica: Desarrollar una función que valide el ingreso de una cadena de caracteres alfanuméricos (letras y números), y que será utilizada en el menú de opciones.
"""

# Valida rango
def numeros_dentro_rango (min, max, lista) :
  lista_rango = []
  for i in range(len(lista)):
    if lista[i] <= max and lista[i] >= min :
      lista_rango.append(lista[i])
  
  return lista_rango