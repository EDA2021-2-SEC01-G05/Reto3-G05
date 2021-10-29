"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#=================================================================================
# Funciones Iniciales
#=================================================================================

def printMenu():
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de Avistamientos")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("0- Salir")
    print("*******************************************")

UFOfile = 'UFOS/UFOS-utf8-small.csv'
catalog = None

#=================================================================================
# Especificaciones de la impresion de datos
#=================================================================================

def printData(avistamientos):
    size = lt.size(avistamientos)
    if size>0:
        for avistamiento in lt.iterator(avistamientos):
            if avistamiento is not None:
                print ("Fecha-hora: " + avistamiento["datetime"] + ", Ciudad: " + avistamiento["city"] + ", Estado: " + avistamiento['state']
                    + ", Pais:  " + avistamiento["country"] + ", Forma: " + avistamiento["shape"] + ", Duracion(seg): " + avistamiento["duration (seconds)"]
                    + ", Duracion(horas/min): " + avistamiento["duration (hours/min)"] + ", Comentarios: " + avistamiento["comments"] + ", Fecha de publicacion: " 
                    + avistamiento["date posted"] + ", Latitud: " + avistamiento["latitude"] + ", Longitud: " + avistamiento["longitude"])
    else:
        print ("No se encontraron avistamientos")

def printDataReq2(avistamientos):
    size = lt.size(avistamientos)
    if size>0:
        for avistamiento in lt.iterator(avistamientos):
            if avistamiento is not None:
                print ("Fecha-hora: " + avistamiento["datetime"] + ", Ciudad: " + avistamiento["city"]
                    + ", Pais:  " + avistamiento["country"] + ", Duracion(seg): " + avistamiento["duration (seconds)"]
                    + ", Forma: " + avistamiento["shape"])
    else:
        print ("No se encontraron avistamientos")

#=================================================================================
# Requerimientos
#=================================================================================

def cargaDatos():
    controller.loadData(catalog, UFOfile)
    lst = catalog['avistamientos']
    first = controller.firstnD(lst,5)
    last = controller.lastnD(lst,5)
    print("-" * 50)
    print('Avistamientos cargados: ' + str(lt.size(catalog['avistamientos'])))
    print('Altura del arbol: ' + str(om.height(catalog["dateIndex"])))
    print('Elementos en el arbol: ' + str(om.size(catalog['dateIndex'])))
    print('Menor Llave: ' + str(om.minKey(catalog['dateIndex'])))
    print('Mayor Llave: ' + str(om.maxKey(catalog['dateIndex'])))
    print("-" * 50)
    print('Los 5 primeros avistamientos: ')
    print("-" * 50)
    printData(first)
    print("-" * 50)
    print('Los 5 ultimos avistamientos: ') 
    print("-" * 50)
    printData(last)

def req2(catalog,minimo,maximo):
    max_d  = controller.maxDurationD(catalog)
    lmaxd = lt.removeFirst(max_d)
    nmaxd = lt.removeFirst(max_d)
    datos = controller.req2(catalog,minimo,maximo)
    n_rango = lt.removeFirst(datos)
    primeros = lt.removeFirst(datos)
    ultimos = lt.removeFirst(datos)
    print("-" * 50)
    print("El numero de avistamientos con la duracion (seg) mas larga registrada " + str(lmaxd) + " es: " + str(nmaxd))
    print("-" * 50)
    print("El numero de avistamientos en el rango " + str(minimo) + ", " + str(maximo) + " es: " + str(n_rango))
    print("-" * 50)
    print("Los primeros 3 avistamientos en el rango son: ")
    print("-" * 50)
    printDataReq2(primeros)
    print("-" * 50)
    print("Los ultimos 3 avistamientos en el rango son: ")
    print("-" * 50)
    printDataReq2(ultimos)

def req4(catalog,minimo,maximo):
    fa = controller.fechaAntiguaD(catalog)
    f = lt.removeFirst(fa)
    n = lt.removeFirst(fa)
    datos = controller.req4(catalog,minimo,maximo)
    n_rango = lt.removeFirst(datos)
    primeros = lt.removeFirst(datos)
    ultimos = lt.removeFirst(datos)
    print("-" * 50)
    print("El numero de avistamientos con la fecha mas antigua registrada " + str(f) + " es: " + str(n))
    print("-" * 50)
    print("El numero de avistamientos en el rango de fechas " + str(minimo) + ", " + str(maximo) + " es: " + str(n_rango))
    print("-" * 50)
    print("Los primeros 3 avistamientos en el rango son: ")
    print("-" * 50)
    printDataReq2(primeros)
    print("-" * 50)
    print("Los ultimos 3 avistamientos en el rango son: ")
    print("-" * 50)
    printDataReq2(ultimos)

#================================================================================
# Menu principal
#================================================================================

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        catalog = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos ....")
        cargaDatos()

    elif int(inputs[0]) == 4:
        minimo = input("Minima duracion: ")
        maximo = input("Maxima duracion: ")
        req2(catalog,minimo,maximo)

    elif int(inputs[0]) == 6:
        minimo = input("Minima fecha: ")
        maximo = input("Maxima fecha: ")
        req4(catalog,minimo,maximo)

    else:
        sys.exit(0)
sys.exit(0)