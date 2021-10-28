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
import time
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

#=================================================================================
# Requerimientos
#=================================================================================

def cargaDatos():
    controller.loadData(catalog, UFOfile)
    lst = catalog['avistamientos']
    first = controller.firstFiveD(lst)
    last = controller.lastFiveD(lst)
    print("-" * 50)
    print('Avistamientos cargados: ' + str(controller.viewsSize(catalog)))
    print('Altura del arbol: ' + str(controller.indexHeight(catalog, "dateIndex")))
    print('Elementos en el arbol: ' + str(controller.indexSize(catalog, "dateIndex")))
    print('Menor Llave: ' + str(controller.minKey(catalog, "dateIndex")))
    print('Mayor Llave: ' + str(controller.maxKey(catalog, "dateIndex")))
    print("-" * 50)
    print('Los 5 primeros avistamientos: ')
    print("-" * 50)
    printData(first)
    print("-" * 50)
    print('Los 5 ultimos avistamientos: ') 
    print("-" * 50)
    printData(last)
        
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
        print("\nCargando información de crimenes ....")
        cargaDatos()

    elif int(inputs[0]) == 3:
        print('Altura del arbol de ciudades: ' + str(controller.indexHeight(catalog, "cityIndex")))
        print('Elementos en el arbol de ciudades: ' + str(controller.indexSize(catalog, "cityIndex")))

    else:
        sys.exit(0)
sys.exit(0)
