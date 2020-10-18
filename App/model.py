"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
from time import process_time
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------


# Funciones para agregar informacion al catalogo
def newAnalyzer ():
    analyzer = {'accidentes': None,
                'fechas': None}

    analyzer['accidentes'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['fechas'] = om.newMap(omaptype='BST',
                                   comparefunction=compareDates)

    return analyzer

def addAccident(analyzer, accident):

    lt.addLast(analyzer['accidentes'], accident)
    updateDateIndex(analyzer, accident)

    return analyzer


def updateDateIndex(analyzer, accident):

    occurreddate = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    severidad = accident['Severity']
    ID = lt.size(analyzer['accidentes'])
    entry = om.get(analyzer['fechas'], accidentdate.date())
    if entry is None:
        severidades = {}
        severidades[severidad] = 1
        lista = lt.newList()
        lt.addLast(lista, ID)
        om.put(analyzer['fechas'], accidentdate.date(), {'id': lista, 'severidades': severidades})
    else:
        dicc = me.getValue(entry)
        lt.addLast(dicc['id'],ID)
        if severidad in dicc['severidades']:
            dicc['severidades'][severidad] += 1
        else:
            dicc['severidades'][severidad] = 1
        om.put(analyzer['fechas'], accidentdate.date(), {'id': dicc['id'], 'severidades': dicc['severidades']})
    return analyzer


# ==============================
# Funciones de consulta
# ==============================

def req1 (analyzer, fecha):

    entry = om.get(analyzer['fechas'], fecha)
    if entry != None:
        dicc = me.getValue(entry)
        return dicc
    else:
        return None

def req2 (analyzer, fecha):
    pass


# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):

    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):

    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1