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
    a = model.newAnalyzer()
    return a


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
def ejecutarreq1 (analyzer,fecha):
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

def ejecutarreq2 (analyzer,fecha_min, fecha):
    t_i = process_time()
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    result = model.req2(analyzer,fecha_min.date(), fecha.date())
    print (lt.size(result))
    t_f = process_time()
    print ('Procesado en: '+ str(t_f - t_i) + 's')