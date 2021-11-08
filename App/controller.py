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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

#==================================================================================
# Inicialización del Catálogo de avistamientos
#==================================================================================

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

#==================================================================================
# Funciones para la carga de datos
#==================================================================================

def loadData(catalog, UFOfile):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    file = cf.data_dir + UFOfile
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addAvistamiento(catalog, avistamiento)
    return catalog

#==================================================================================
# Consulta de información Arboles
#==================================================================================

def firstFiveD(lista):
    """
    Retorna una lista con los tres primeros elementos de una lista.
    """
    return model.firstFiveD(lista)
    
def lastFiveD(lista):
    """
    Retorna una lista con los 3 ultimos elementos de una lista.
    """
    return model.lastFiveD(lista)

def viewsSize(catalog):
    """
    Numero de crimenes leidos
    """
    return model.viewsSize(catalog)


def indexHeight(catalog, tipo):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(catalog, tipo)


def indexSize(catalog, tipo):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(catalog, tipo)


def minKey(catalog, tipo):
    """
    La menor llave del arbol
    """
    return model.minKey(catalog, tipo)


def maxKey(catalog, tipo):
    """
    La mayor llave del arbol
    """
    return model.maxKey(catalog, tipo)

def KesySet(analizer, tipo):
    """
    Lista con las llaves de un indice.
    """
    return model.KesySet(analizer, tipo)

#==================================================================================
# Requerimientos
#==================================================================================

#Req 1

def getAvistamientoporCiudad(catalog, ciudad_entry):
    """
    Este función se encarga de encontrar los avistamientos de una ciudad dada por el usuario.
    """
    return model.getAvistamientoporCiudad(catalog, ciudad_entry)

def firstThreeN(lista):
    """
    Retorna una lista con los 5 primeros elementos de una lista.
    """
    return model.firstThreeN(lista)

def lastThreeN(lista):
    """
    Retorna una lista con los 5 ultimos elementos de una lista.
    """
    return model.lastThreeN(lista)

#Req 3

def getAvistamientoPorHora(catalog, hora_entry):
    """
    Esta función se encarga de encontrar los avistamientos de una hora dada por el usuario.
    """
    return model.getAvistamientoPorHora(catalog, hora_entry)

def organizarAvistamientoPorRangoHora(catalog, hora_inicial, hora_final):
    """
    Organiza y retorna los avistamientos que esten en un rango de 
    una hora inicial y una hora final.
    """
    return model.organizarAvistamientoPorRangoHora(catalog, hora_inicial, hora_final)

def avistamientosPorGeografia(catalog, long0, long1, lat0, lat1):
    """
    Esta función devuelve una lista con los avistamientos que
    se encuentran en un rango de latitudes y longitudes. 
    """
    return model.avistamientosPorGeografia(catalog, long0, long1, lat0, lat1)