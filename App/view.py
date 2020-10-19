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

import sys
import config
from DISClib.ADT import list as lt
from App import controller
assert config
import datetime

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


#accfile = "Data\\us_accidents_small.csv"
accfile = "Data\\US_Accidents_Dec19.csv"
mini = '2016-02-08'
fecha_min = datetime.datetime.strptime(mini, '%Y-%m-%d')
maxi  = '2019-08-23'
fecha_max = datetime.datetime.strptime(maxi, '%Y-%m-%d')

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1")
    print("4- Requerimento 2")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        analyzer = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes ....")
        accidentes = controller.loadData(analyzer, accfile)
    

    elif int(inputs[0]) == 3:
        print("\nReq1: ")
        fecha = input('Ingrese la fecha YYYY-MM-DD: \n')
        controller.ejecutarreq1(accidentes, fecha)



    elif int(inputs[0]) == 4:
        print("\nReq2 ")
        fecha = input('Ingrese la fecha límite YYYY-MM-DD: \n')
        controller.ejecutarreq2(accidentes, fecha_min, fecha)
    else:
        sys.exit(0)
sys.exit(0)
