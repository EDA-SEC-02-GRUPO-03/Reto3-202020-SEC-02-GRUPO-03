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
from DISClib.DataStructures import linkedlistiterator as it
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


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'accidentes': None,
                'fechas': None}

    analyzer['accidentes'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['fechas'] = om.newMap(omaptype='RBT',
                                   comparefunction=compareDates)
    return analyzer


# Funciones para agregar informacion al catalogo


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
    dicc = me.getValue(entry)
    return dicc


def req2 (analyzer, fecha):
    pass


def req3 (analyzer, fecha):
    pass


def req4(analyzer, fechamin, fechamax):
    """
    Conocer el estado con más accidentes en un rango de fechas.

    William Mendez
    """
    lst = om.values(analyzer['fechas'], fechamin, fechamax)
    estados = {'ninguno': {'cont': 0}}

    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)

        if type(element) == type(fechamax):

            valor = om.get(analyzer['fechas'], element)
            ids = valor['value']['id']
            for j in range(1, lt.size(ids) + 1):
                ID = lt.getElement(ids, j)
                value = lt.getElement(analyzer['accidentes'], ID)
                estado = value['State']

                if estado not in estados.keys():
                    estados[estado] = {}
                    estados[estado]['cont'] = 1
                else:
                    estados[estado]['cont'] += 1

                if element not in estados[estado].keys():
                    estados[estado][element] = 1
                else:
                    estados[estado][element] += 1

    mayor = ('ninguno', 0)
    for i in estados.keys():
        # print(estados[i])
        if estados[i]['cont'] >= estados[mayor[0]]['cont']:
            fechamay = ('none', 0)
            for j in estados[i].keys():
                if estados[i][j] >= fechamay[1] and j != 'cont':
                    fechamay = (j, estados[i][j])
            fechamay = str(fechamay[0]) + ' con ' + str(fechamay[1])
            mayor = (i, estados[i]['cont'], fechamay)
    return mayor


def req5 (analyzer, h1, h2):
    n_acc = {'total': 0,
             '1': 0,
             '2': 0,
             '3': 0,
             '4': 0}
    for i in range(1, lt.size(analyzer['accidentes']) + 1):
        info = lt.getElement(analyzer['accidentes'], i)
        if datetime.datetime.__ge__(datetime.datetime.strptime( \
           info['Start_Time'][-8:-3], '%H:%M'), h1) and \
           datetime.datetime.__le__(datetime.datetime.strptime( \
           info['End_Time'][-8:-3], '%H:%M'), h2):
            n_acc['total'] += 1
            n_acc[info['Severity']] += 1
    porc = round(n_acc['total'] * 100 / accidentesSize(analyzer), 2)
    n_acc['porc'] = porc
    return n_acc


def req6 (analyzer, fecha):
    pass


def accidentesSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer['accidentes'])


def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['fechas'])


def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['fechas'])


def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['fechas'])


def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['fechas'])



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


def compareOffenses(offense1, offense2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1
