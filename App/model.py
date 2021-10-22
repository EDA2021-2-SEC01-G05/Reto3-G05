"""
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
                'arbol': None}

    """
    """
    catalog["avistamientos"] = lt.newList()
    catalog["arbol"] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates) 
    return catalog

#==================================================================================
# Funciones para agregar info al catalogo
#==================================================================================

def addAvistamiento(catalog,avistamiento):
    """
    """
    lt.addLast(catalog['avistamientos'], avistamiento)
    updateDateIndex(catalog['arbol'], avistamiento)
    return catalog

def updateDateIndex(arbol, avistamiento):
    """
    Se toma la fecha del avistamiento y se busca si ya existe en el arbol dicha fecha.
    Si es asi, se adiciona a su lista de avistamientos y se actualiza el indice de ciudades de los avistamientos.
    Si no se encuentra creado un nodo para esa fecha en el arbol se crea y se actualiza el indice de ciudades de los avistamientos
    """
    occurreddate = avistamiento['datetime']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(arbol, crimedate.date())
    if entry is None:
        datentry = newDataEntry(avistamiento)
        om.put(arbol, crimedate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, avistamiento)
    return arbol

def addDateIndex(datentry, avistamiento):
    """
    Actualiza un indice de ciudad del avistamiento. Este indice tiene una lista
    de avistamientos y una tabla de hash cuya llave es la ciudad del avistamiento y
    el valor es una lista con los avistamientos de dicha ciudad en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lst']
    lt.addLast(lst, avistamiento)
    cityIndex = datentry['index']
    cityentry = mp.get(cityIndex, avistamiento['city'])
    if (cityentry is None):
        entry = newCityEntry(avistamiento['city'], avistamiento)
        lt.addLast(entry['lstcity'], avistamiento)
        mp.put(cityIndex, avistamiento['city'], entry)
    else:
        entry = me.getValue(cityentry)
        lt.addLast(entry['citylst'], avistamiento)
    return datentry


def newDataEntry(avistamiento):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'index': None, 'lst': None}
    entry['index'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=None)
    entry['lst'] = lt.newList()
    return entry

def newCityEntry(city, avistamiento):
    """
    Crea una entrada en el indice por ciudad del avistamiento, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    cityentry = {'city': None, 'lstcity': None}
    cityentry['city'] = city
    cityentry['lstcity'] = lt.newList()
    return cityentry

#==================================================================================
# Funciones de comparacion
#==================================================================================

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
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

#==================================================================================
# Requerimientos
#==================================================================================
