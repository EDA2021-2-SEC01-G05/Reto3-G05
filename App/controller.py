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

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    file = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for avistamiento in input_file:
        model.addAvistamiento(catalog, avistamiento) 

#==================================================================================
# Requerimientos
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
