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
                'cityIndex': None,
                "hourIndex": None}

    """
    """
    catalog["avistamientos"] = lt.newList()
    catalog["cityIndex"] = om.newMap(omaptype="RBT", comparefunction=compareCities)
    catalog["hourIndex"] = om.newMap(omaptype="RBT", comparefunction= compareHour)
    catalog["coordIndex"] = om.newMap(omaptype= "RBT", comparefunction= compareLongitudes)
    return catalog

#==================================================================================
# Funciones para agregar info al catalogo
#==================================================================================

def addAvistamiento(catalog,avistamiento):
    """
    """
    lt.addLast(catalog['avistamientos'], avistamiento)
    addCityIndex(catalog, avistamiento)
    addHourIndex(catalog, avistamiento)
    updateCoordIndex(catalog, avistamiento)
    return catalog

def addCityIndex(catalog, avistamiento):
    """
    """
    index = catalog["cityIndex"]
    ciudad = avistamiento["city"]
    existcity = om.contains(index, ciudad)
    if existcity:
        c_entry = om.get(index, ciudad)["value"]
    else:
        c_entry = lt.newList()
    lt.addLast(c_entry, avistamiento)
    om.put(index, ciudad, c_entry)

def addHourIndex(catalog, avistamiento):
    """
    """
    index = catalog["hourIndex"]
    fecha = datetime.datetime.strptime(avistamiento["datetime"], '%Y-%m-%d %H:%M:%S')
    hora = str(fecha.time())
    existhour = om.contains(index, hora)
    if existhour:
        h_entry = om.get(index, hora)["value"]
    else:
        h_entry = lt.newList("SINGLE_LINKED", cmpfunction= compareTimeFrames)
    lt.addLast(h_entry, avistamiento)
    om.put(index, hora, h_entry)

def updateCoordIndex(catalog, avistamiento):
    """
    """
    index = catalog["coordIndex"]
    longitud = str(round(float(avistamiento["longitude"]), 2)) 
    existlongitude = om.contains(index, longitud)
    if existlongitude:
        l_entry = om.get(index, longitud)["value"]
    else:
        l_entry = lt.newList("SINGLE_LINKED", cmpfunction= compareLatitudes)
    lt.addLast(l_entry, avistamiento)
    om.put(index, longitud, l_entry)


#==================================================================================
# Funciones de comparacion
#==================================================================================

def compareLongitudes(longi1, longi2):
    """
    Compara dos longitudes
    """
    if (float(longi1) == float(longi2)):
        return 0
    elif (float(longi1) > float(longi2)):
        return 1
    else:
        return -1
    
def compareCities(city1, city2):
    if (city1 == city2):
        return 0 
    elif (city1 > city2):
        return 1
    else:
        return -1

def compareDates2(av1, av2):
    date1 = datetime.datetime.strptime(av1["datetime"], '%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(av2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (date1 > date2):
        return 0
    else:
        return -1

def compareHour(h1, h2):
    if (h1 == h2):
        return 0
    elif (h1 > h2):
        return 1
    else:
        return -1

def compareTimeFrames(av1, av2):
    date1 = datetime.datetime.strptime(av1["datetime"], '%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(av2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (date1.time() > date2.time()):
        return 0
    else:
        return -1

def compareLatitudes(av1, av2):
    l1 = round(float(av1["latitude"]), 2)
    l2 = round(float(av2["latitude"]), 2)
    if (l1 < l2):
        return 0
    else:
        return -1

#==================================================================================
# Consultar info, modificar datos
#==================================================================================

def firstFiveD(lista):
    """
    Retorna una lista con los 5 primeros elementos de una lista.
    """
    first = lt.subList(lista,1,5)
    return first
    
def lastFiveD(lista):
    """
    Retorna una lista con los 5 ultimos elementos de una lista.
    """
    last = lt.subList(lista,lt.size(lista)-4,5)
    return last

def viewsSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['avistamientos'])


def indexHeight(analyzer, tipo):
    """
    Altura del arbol
    """
    return om.height(analyzer[tipo])


def indexSize(analyzer, tipo):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer[tipo])


def minKey(analyzer, tipo):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer[tipo])


def maxKey(analyzer, tipo):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer[tipo])

def KesySet(analizer, tipo):
    """
    Lista con las llaves de un indice.
    """
    return om.keySet(analizer[tipo])

#==================================================================================
# Requerimientos
#==================================================================================

#Requerimiento 1 

def getAvistamientoporCiudad(catalog, ciudad_entry):
    """
    Esta función se encarga de encontrar los avistamientos de una ciudad dada por el usuario.
    """
    exist = om.contains(catalog["cityIndex"], ciudad_entry)
    if exist:
        avist = om.get(catalog["cityIndex"], ciudad_entry)["value"]
    ms.sort(avist, cmpfunction= compareDates2)
    return avist

def firstThreeN(lista):
    """
    Retorna una lista con los 5 primeros elementos de una lista.
    """
    first = lt.subList(lista,1,3)
    return first
    
def lastThreeN(lista):
    """
    Retorna una lista con los 5 ultimos elementos de una lista.
    """
    last = lt.subList(lista,lt.size(lista)-2,3)
    return last

#Requerimiento 3

def getAvistamientoPorHora(catalog, hora_entry):
    """
    Esta función se encarga de encontrar los avistamientos de una hora dada por el usuario.
    """
    exist = om.contains(catalog["hourIndex"], hora_entry)
    if exist:
        avist = om.get(catalog["hourIndex"], hora_entry)["value"]
    return avist

def getAvistamientoPorHora2(catalog, hora_entry, org):
    """
    Esta función se encarga de encontrar los avistamientos de una hora dada por el usuario.
    """
    exist = om.contains(catalog["hourIndex"], hora_entry)
    if exist:
        avist = om.get(catalog["hourIndex"], hora_entry)["value"]
        for avit in lt.iterator(avist):
            lt.addLast(org, avit)

def organizarAvistamientoPorRangoHora(catalog, hora_inicial, hora_final):
    """
    Organiza y retorna los avistamientos que esten en un rango de 
    una hora inicial y una hora final.
    """
    org = lt.newList()
    time_1 = datetime.datetime.strptime(hora_inicial,"%H:%M")
    time_2 = datetime.datetime.strptime(hora_final,"%H:%M")
    time_interval = time_2 - time_1
    h = str(time_interval)
    hh, mm, ss = h.split(':')
    delta = int(hh) * 60 + int(mm) + int(ss) * 0
    for minute in range(delta + 1):
        new_day = time_1 + datetime.timedelta(minutes=minute)
        new_hour = new_day.strftime("%H:%M:%S")
        getAvistamientoPorHora2(catalog, str(new_hour), org)
    return org

#Req 5

def avistamientosPorGeografia(catalog, long0, long1, lat0, lat1):
    """
    Esta función devuelve una lista con los avistamientos que
    se encuentran en un rango de latitudes y longitudes. 
    """
    final = lt.newList("ARRAY_LIST")
    lst = om.values(catalog["coordIndex"], long0, long1) #O(n)
    for avist in lt.iterator(lst):
        for a in lt.iterator(avist):
            if float(a["latitude"]) >= float(lat0) and float(a["latitude"]) <= float(lat1):
                lt.addLast(final, a)
    return final


