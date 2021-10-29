﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.ADT import orderedmap as om
import datetime
from datetime import date, timedelta
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

#==================================================================================
# Construccion de Modelos
#==================================================================================

def newCatalog():
    """ 
    """
    catalog = {'avistamientos': None,
                'durationIndex': None,
                'dateIndex': None}

    """
    """
    catalog["avistamientos"] = lt.newList()
    # Ordered Map Req 2
    catalog["durationIndex"] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDurationD)
    # Ordered Map Req 4
    catalog['dateIndex'] = om.newMap(omaptype='RBT',
                                    comparefunction=compareDateD)
    return catalog

#==================================================================================
# Funciones para agregar info al catalogo
#==================================================================================

def addAvistamiento(catalog,avistamiento):
    """
    """
    lt.addLast(catalog['avistamientos'], avistamiento)
    updateDurationIndexD(catalog['durationIndex'], avistamiento)
    updateDateIndexD(catalog['dateIndex'],avistamiento)

    return catalog

def updateDurationIndexD(arbol, avistamiento):
    """
    Se toma la duracion(seg) del avistamiento y se busca si ya existe en el arbol dicha duracion.
    Si es asi, se adiciona a su lista de avistamientos.
    Si no se encuentra creado un nodo para esa duracion en el arbol se crea.
    """
    duracion = float(avistamiento['duration (seconds)']) 
    entry = om.get(arbol, duracion)
    if entry is None:
        datentry = newDurationD(duracion)
        om.put(arbol, duracion, datentry)
    else:
        datentry = me.getValue(entry)
    addDurationIndexD(datentry,avistamiento)
    return arbol

def addDurationIndexD(datentry,avistamiento):
    lst = datentry['lst']
    lt.addLast(lst, avistamiento)
    index = datentry['index']
    countryentry = mp.get(index, avistamiento['country'])
    if (countryentry is None):
        entry = newCountryD(avistamiento['country'])
        lt.addLast(entry['lstpais'], avistamiento)
        mp.put(index, avistamiento['country'], entry)
    else:
        entry = me.getValue(countryentry)
        lt.addLast(entry['lstpais'], avistamiento)
    return datentry

def newDurationD(duracion):
    """
    Crea una entrada en el indice por duracion, es decir en el arbol
    binario.
    """
    entry = {'index': None, 'lst': None}
    entry['index'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareCountryD)
    entry['lst'] = lt.newList('SINGLE_LINKED')
    return entry

def newCountryD(country):
    """
    Crea una entrada en el indice por pais, es decir 
    en la tabla de hash que se encuentra en cada nodo del arbol.
    """
    countryentry = {'country': None, 'lstpais': None}
    countryentry['country'] = country
    countryentry['lstpais'] = lt.newList('SINGLE_LINKED')
    return countryentry


def updateDateIndexD(arbol, avistamiento):
    """
    Se toma la fecha(AAAA-MM-DD) del avistamiento y se busca si ya existe en el arbol dicha fecha.
    Si es asi, se adiciona a su lista de avistamientos.
    Si no se encuentra creado un nodo para esa fecha en el arbol se crea.
    """
    dato = avistamiento['datetime']
    fecha = datetime.datetime.strptime(dato, '%Y-%m-%d %H:%M:%S')
    entry = om.get(arbol, fecha.date())
    if entry is None:
        datentry = lt.newList()
        om.put(arbol, fecha.date(), datentry)
    else:
        datentry = me.getValue(entry)
    lt.addLast(datentry,avistamiento)

#==================================================================================
# Funciones de comparacion
#==================================================================================

def compareDurationD(d1, d2):
    """
    Compara dos duraciones.
    """
    if (d1 == d2):
        return 0
    elif d1 > d2:
        return 1
    return -1
    
def compareDateD(f1, f2):
    """
    Compara dos fechas.
    """
    if (f1 == f2):
        return 0
    elif f1 > f2:
        return 1
    return -1

def compareCountryD(pais1,p2):
    """
    Compara dos paises. 
    """
    pais2 = me.getKey(p2)
    if (pais1 == pais2):
        return 0
    elif (pais1 > pais2):
        return 1
    else:
        return -1

#==================================================================================
# Funciones Auxiliares
#==================================================================================

def firstnD(lista,n):
    """
    Retorna una lista con los n primeros elementos de una lista.
    """
    first = lt.subList(lista,1,n)
    return first
    
def lastnD(lista,n):
    """
    Retorna una lista con los n ultimos elementos de una lista.
    """
    last = lt.subList(lista,lt.size(lista)-(n-1),n)
    return last

def copiarListaD(lista, cmpf):
    """
    Copia una lista con nueva cmpfunction cmpf
    """
    copia = lt.newList("LINKED_LIST",cmpf)
    for elemento in lt.iterator(lista):
        lt.addLast(copia,elemento)
    return copia

#==================================================================================
# Requerimientos
#==================================================================================

#-----------------------------------------------------------
# Requerimiento 2 
#-----------------------------------------------------------
def maxDurationD(catalog):
    """
    Retorna una lista con la duración en segundos más larga que se tenga(n) registrado(s)
    y el número de avistamientos correspondientes a esa duracion.
    """
    mapa = catalog['durationIndex']
    llave = om.maxKey(mapa)
    pareja = om.get(mapa,llave)
    valor = me.getValue(pareja)
    lista = valor['lst']
    num = lt.size(lista)
    resultado = lt.newList("LINKED_LIST")
    lt.addLast(resultado,llave)
    lt.addLast(resultado,num)
    return resultado

def req2(catalog,minimo,maximo):
    """
    Retorna lista con 3 cosas: 
    El numero de avistamientos en un rango por duracion minimo, maximo.
    Una lista con los primeros 3 avistamientos dentro del rango.
    Una lista con los ultimos 3 avistamientos dentro del rango.
    """
    datos = catalog['durationIndex']
    llaves = om.keys(datos,float(minimo),float(maximo))
    # sacar el numero de avistamientos en el rango
    n = 0 
    for llave in lt.iterator(llaves):
        pareja = om.get(datos,llave)
        valor = me.getValue(pareja)
        lista = valor['lst']
        n += lt.size(lista)
    # sacar los primeros
    primeros = lt.newList()
    i = 0
    while i < 3:
        llav = lt.removeFirst(llaves)
        par = om.get(datos,llav)
        val = me.getValue(par)
        mapa = val['index']
        paises = mp.keySet(mapa)
        for pais in lt.iterator(paises):
            pais_lista = mp.get(mapa,pais)
            lista = me.getValue(pais_lista)['lstpais']
            for e in lt.iterator(lista):
                lt.addLast(primeros,e)
        i += 1
    # sacar los ultimos
    ultimos = lt.newList("LINKED_LIST")
    j = 0
    while j < 3:
        lla = lt.removeLast(llaves)
        parej = om.get(datos,lla)
        va = me.getValue(parej)
        mapa2 = va['index']
        paiss = mp.keySet(mapa2)
        for p in lt.iterator(paiss):
            pais_list = mp.get(mapa2,p)
            l = me.getValue(pais_list)['lstpais']
            for el in lt.iterator(l):
                lt.addLast(ultimos,el)
        j += 1      
    # estipular el return
    resultado = lt.newList("LINKED_LIST")
    lt.addLast(resultado,n)
    lt.addLast(resultado,firstnD(primeros,3))
    lt.addLast(resultado,firstnD(ultimos,3))
    return resultado

#-----------------------------------------------------------
# Requerimiento 4 
#-----------------------------------------------------------
def fechaAntiguaD(catalog):
    """
    Retorna una lista con la fecha (AAAA-MM-DD) más antigua que se tenga(n) registrado(s)
    y el número de avistamientos correspondientes a esa fecha.
    """
    mapa = catalog['dateIndex']
    llave = om.minKey(mapa)
    pareja = om.get(mapa,llave)
    valor = me.getValue(pareja)
    num = lt.size(valor)
    resultado = lt.newList("LINKED_LIST")
    lt.addLast(resultado,llave)
    lt.addLast(resultado,num)
    return resultado

def req4(catalog,minimo,maximo):
    """
    Retorna lista con 3 cosas: 
    El numero de avistamientos en un rango dado por dos fechas: minimo, maximo.
    Una lista con los primeros 3 avistamientos del rango.
    Una lista con los ultimos 3 avistamientos del rango.
    """
    datos = catalog['dateIndex']
    llaves = om.keys(datos,date.fromisoformat(minimo),date.fromisoformat(maximo))
    # sacar el numero de avistamientos en el rango
    n = 0 
    for llave in lt.iterator(llaves):
        pareja = om.get(datos,llave)
        lista = me.getValue(pareja)
        n += lt.size(lista)
    # sacar los primeros
    primeros = lt.newList()
    i = 0
    while i < 3:
        llav = lt.removeFirst(llaves)
        par = om.get(datos,llav)
        lst = me.getValue(par)
        for e in lt.iterator(lst):
            lt.addLast(primeros,e)
        i += 1
    # sacar los ultimos
    ultimos = lt.newList("LINKED_LIST")
    j = 0
    while j < 3:
        lla = lt.removeLast(llaves)
        parej = om.get(datos,lla)
        lsta = me.getValue(parej)
        for el in lt.iterator(lsta):
            lt.addLast(ultimos,el)
        j += 1      
    # estipular el return
    resultado = lt.newList("LINKED_LIST")
    lt.addLast(resultado,n)
    lt.addLast(resultado,firstnD(primeros,3))
    lt.addLast(resultado,firstnD(ultimos,3))
    return resultado