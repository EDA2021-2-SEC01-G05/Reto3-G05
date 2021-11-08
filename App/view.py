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
                    + avistamiento["date posted"] + ", Latitud: " + avistamiento["latitude"] + ", Longitud: " + avistamiento["longitude"] + "\n")
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
    first = controller.firstFiveD(lst)
    last = controller.lastFiveD(lst)
    print("-" * 50)
    print('Avistamientos cargados: ' + str(controller.viewsSize(catalog)))
    print("-" * 50)
    print('Los 5 primeros avistamientos: ')
    print("-" * 50)
    printData(first)
    print("-" * 50)
    print('Los 5 ultimos avistamientos: ') 
    print("-" * 50)
    printData(last)

def Requerimiento1(catalog, ciudad):
    avist_city = controller.getAvistamientoporCiudad(catalog, ciudad.lower())
    first = controller.firstThreeN(avist_city)
    last = controller.lastThreeN(avist_city)
    total = controller.indexSize(catalog, "cityIndex")
    print("-" * 50)
    print("-" * 50 + "Requerimeinto 1 Answers" + ("-" * 50))
    print("There are " + str(total) + " differrent cities with UFO sightings..." + "\n")
    print("There are " + str(lt.size(avist_city)) + " at the: " + ciudad + " city.")    
    print("-" * 50)
    print('Los 3 primeros avistamientos: ')
    print("-" * 50)
    printData(first)
    print("-" * 50)
    print('Los 3 ultimos avistamientos: ') 
    print("-" * 50)
    printData(last)
    print("-" * 50 + "\n")

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

def Requerimiento3(catalog, hora_inicial, hora_final):
    late = controller.maxKey(catalog, "hourIndex")
    size_late = lt.size(controller.getAvistamientoPorHora(catalog, late))
    org = controller.organizarAvistamientoPorRangoHora(catalog, hora_inicial, hora_final)
    first = controller.firstThreeN(org)
    last = controller.lastThreeN(org)
    print("There are " + str(controller.indexSize(catalog, "hourIndex")) + " UFO sightings with different times [hh:mm:ss]...")
    print("The latest UFO sightings time is: ")
    print(str(late) + ": " + str(size_late) + "\n")
    print("There are " + str(lt.size(org)) + " sightings " + hora_inicial + " and " + hora_final) 
    print('Los 3 primeros avistamientos: ')
    print("-" * 50)
    printData(first)
    print("-" * 50)
    print('Los 3 ultimos avistamientos: ') 
    print("-" * 50)
    printData(last)
    print("-" * 50 + "\n")

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

def Requerimiento5(catalog, long0, long1, lat0, lat1):
    lst = controller.avistamientosPorGeografia(catalog, long0, long1, lat0, lat1)
    tamaño = lt.size(lst)
    last = controller.lastFiveD(lst)
    firts = controller.firstFiveD(lst)
    print("=" * 50 + " Req No. 5 Answers " + "=" * 50)
    print("There are " + str(tamaño) + " different UFO sightings in the current area")
    print("-" * 50)
    print('Los 5 primeros avistamientos: ')
    print("-" * 50)
    printData(firts)
    print('Los 5 primeros avistamientos: ')
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
        print("\nCargando información de avistamientos ....")
        cargaDatos()

    elif int(inputs[0]) == 3:
        print("-" * 50 + "Requerimeinto 1 Inputs" + ("-" * 50))
        ciudad = input("UFO Sightings in the city of: ")
        Requerimiento1(catalog, ciudad)
    
    elif int(inputs[0]) == 4:
        minimo = input("Minima duracion: ")
        maximo = input("Maxima duracion: ")
        req2(catalog,minimo,maximo)
    
    elif int(inputs[0]) == 5:
        hora_inicial = input("Límite inferior en formato HH: MM.: ")
        hora_final = input("Límite superior en formato HH: MM.: ")
        Requerimiento3(catalog, hora_inicial, hora_final)
    
    elif int(inputs[0]) == 6:
        minimo = input("Minima fecha: ")
        maximo = input("Maxima fecha: ")
        req4(catalog,minimo,maximo)

    elif int(inputs[0]) == 7:
        long0 = input("Ingrese la longitud inicial: ")
        long1 = input("Ingrese la longitud final: ")
        lat0 = input("Ingrese la latitud inicial: ")
        lat1 = input("Ingrese la latitud final: ")
        Requerimiento5(catalog, long0, long1, lat0, lat1)
    else:
        sys.exit(0)
sys.exit(0)
