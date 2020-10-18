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

import config as cf
from App import model
import datetime
from time import process_time
from DISClib.ADT import list as lt
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    t_i = process_time()
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    t_f = process_time()
    print (t_f - t_i)
    return analyzer


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def req1(analyzer, fecha):
    t_i = process_time()
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    result = model.req1(analyzer,fecha.date())
    if result != None:
        total = 0
        for i in result:
            total += result[i]
            print ('De severidad '+i+' hubo '+str(result[i])+' accidentes')
            print ('Hubo '+str(total)+' accidentes en esa fecha.')
    else:
        print ('No se encontró nada en esa fecha')
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')


def req4(analyzer, fechamin, fechamax):
    t_i = process_time()
    fechamin = datetime.datetime.strptime(fechamin, '%Y-%m-%d')
    fechamax = datetime.datetime.strptime(fechamax, '%Y-%m-%d')
    # try:
    result = model.req4(analyzer, fechamin.date(), fechamax.date())
    print('El estado con más accidentes entre', fechamin, 'y', fechamax,
            'es:\n\t', result[0], 'con', result[1], 'accidentes.')
# except:
    print('Hubo un error con el rango de fechas')
# finally:
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')


def req5(analyzer, h1, h2):
    t_i = process_time()
    h1 = datetime.time(h1)
    h2 = datetime.time(h2)
    # try:
    result = model.req5(analyzer, h1, h2)
    print('El estado con más accidentes entre', h1, 'y', h2,
            'es:\n\t', result[0], 'con', result[1], 'accidentes.')
# except:
    print('Hubo un error con el rango de fechas')
# finally:
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')



def crimesSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.accidentesSize(analyzer)


def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)
