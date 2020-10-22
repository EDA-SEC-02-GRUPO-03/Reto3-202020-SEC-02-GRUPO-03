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
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8-sig"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')
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
        for i in result['severidades']:
            total += result['severidades'][i]
            print ('De severidad '+i+' hubo '+str(result['severidades'][i])+' accidentes')
        print ('Hubo '+str(lt.size(result['id']))+' accidentes en esa fecha.')
    else:
        print ('No se encontró nada en esa fecha')
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')

def ejecutarreq2 (analyzer,fecha_min, fecha):
    t_i = process_time()
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    result = model.req2(analyzer,fecha_min.date(), fecha.date())
    print ('Entre esas fechas hubo', result[0], 'accidentes')
    print ('La fecha de más accidentes fue ', result[1], ', ', result[2], 'accidentes')
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')

def req3 ():
    pass

def req4(analyzer, fechami, fechama):
    t_i = process_time()
    fechamin = datetime.datetime.strptime(fechami, '%Y-%m-%d')
    fechamax = datetime.datetime.strptime(fechama, '%Y-%m-%d')
# try:
    result = model.req4(analyzer, fechamin.date(), fechamax.date())
    print('El estado con más accidentes entre', fechami, 'y', fechama, \
            'es:\n -', result[0], 'con', result[1], 'accidentes.')
    print(' - La fecha con más accidentes para este estado es:', result[2])
# except:
    # print('Hubo un error con el rango de fechas')
# finally:
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')


def req5(analyzer, h1, h2):
    t_i = process_time()
    if int(h1[3:]) < 15:
        h1 = h1[:2] + ':00'
    elif int(h2[3:]) < 15:
        h2 = h2[:2] + ':00'
    elif int(h1[3:]) >= 15 and int(h1[3:]) < 45:
        h1 = h1[:2] + ':30'
    elif int(h2[3:]) >= 15 and int(h2[3:]) < 45:
        h2 = h2[:2] + ':30'
    elif int(h1[3:]) >= 45:
        h1 = str(int(h1[:2]) + 1) + ':00'
    elif int(h2[3:]) >= 45:
        h2 = str(int(h2[:2]) + 1) + ':00'

    if int(h1[3:]) >= 60 or int(h2[3:]) >= 60 or \
        int(h1[:2]) >= 24 or int(h2[:2]) >= 24 or len(h1 + h2) < 10:
        print('Hora no válida\n')

    else:
        h1 = datetime.time(int(h1[:2]), int(h1[3:]))
        h2 = datetime.time(int(h2[:2]), int(h2[3:]))
        try:
            result = model.req5(analyzer, h1, h2)
            print('Los resultados entre las', h1, 'y', h2,
                    'son:\n -', result['porc'], '% (', result['total'], ') del', \
                    'total de accidentes. Se agrupan de la suiguente manera:')
            for i in range(1, 5):
                print('severidad', i, ':\t', result[str(i)])
        except:
            print('Hubo un error con el rango de fechas')
        finally:
            t_f = process_time()
            print ('Procesado en: '+ str(t_f - t_i) + 's')

def ejecutarreq6 (analyzer, lat, lon, radio):
    t_i = process_time()
    result = model.req6(analyzer, lat, lon, radio)
    print ('En un radio de ', radio, ' kms. hubo en total ', result[0], ' accidentes.')
    print (result[1])
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
