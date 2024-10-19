from biblioteca import *

def menu ():
  opcion = input('¿Que acción desea realizar?: A - Generar lista de números | B - Ordenar lista anterior | C - Buscar cantidad de números dentro del rango | D - Máximo y mínimo del rango | E - Generar una matriz: ')
  lista = []
  ordenar = []
  rango = 0
  min = 5
  max = 10
  rango_max = 0
  rango_min = 0

  while opcion != 0 and opcion != '0': 
    if opcion == 'A':
      lista = enteros_aleatoreos()
      opcion = input('¿Que acción desea realizar?: A - Generar lista de números | B - Ordenar lista anterior | C - Buscar cantidad de números dentro del rango | D - Máximo y mínimo del rango | E - Generar una matriz: ')
    
    elif opcion == 'B':
      if len(lista) > 0: 
        print('Se seleccionó previamente A')
        ordenar = ordenar_enteros(lista, 'ASC')
        opcion = input('¿Que acción desea realizar?: A - Generar lista de números | B - Ordenar lista anterior | C - Buscar cantidad de números dentro del rango | D - Máximo y mínimo del rango | E - Generar una matriz: ')
      else :
        print('Debe seleccionar la opción A para poder hacer uso de esta opción')
        """ menu() """
    elif opcion == 'C':
      if len(lista) > 0:
        rango = numeros_dentro_rango(min, max, lista)
      opcion = input('¿Que acción desea realizar?: A - Generar lista de números | B - Ordenar lista anterior | C - Buscar cantidad de números dentro del rango | D - Máximo y mínimo del rango | E - Generar una matriz: ')
    elif opcion == 'D':
      if len(lista) > 0 and len(rango) > 0:
        for i in range (len(rango)):
          if i == 0:
            rango_max = rango[i]
            rango_min = rango[i]
          else :
            if rango_max < rango[i]:
              rango_max = rango[i]
            
            if rango_min > rango[i]:
              rango_min = rango[i]
      opcion = input('¿Que acción desea realizar?: A - Generar lista de números | B - Ordenar lista anterior | C - Buscar cantidad de números dentro del rango | D - Máximo y mínimo del rango | E - Generar una matriz: ')

    elif opcion == 'E':
      caracteres_alfanumericos()
      opcion = input('¿Que acción desea realizar?: A - Generar lista de números | B - Ordenar lista anterior | C - Buscar cantidad de números dentro del rango | D - Máximo y mínimo del rango | E - Generar una matriz: ')

  print(lista, 'lista')
  print(ordenar, 'ordenar')
  print(f'CANTIDAD DE NÚMEROS EN EL RANGO [{min} - {max}]: {len(rango) + 1}')
  print(f'rango máximo: {rango_max}, rango mínimo: {rango_min}')

menu()