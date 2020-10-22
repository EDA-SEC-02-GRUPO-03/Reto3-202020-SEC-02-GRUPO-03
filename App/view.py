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

sys.setrecursionlimit(3000000)

#accfile = "Data\\us_accidents_small.csv"
accfile = "Data\\Acc2017.csv"

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
    print("5- Requerimento 3")
    print("6- Requerimento 4")
    print("7- Requerimento 5")
    print("8- Requerimento 6")
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
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes ....")
        controller.loadData(cont, accfile)
        print('Accidentes cargados: ' + str(controller.crimesSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))


    elif int(inputs[0]) == 3:
        print("\nRequerimiento No 1 del reto 3: ")
        fecha = input('Ingrese la fecha YYYY-MM-DD: \n')
        controller.req1(cont, fecha)


    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 2 del reto 3: ")
        fecha = input('Ingrese la fecha límite YYYY-MM-DD: \n')
        controller.ejecutarreq2(cont, controller.minKey(cont), fecha)
    
    elif int(inputs[0]) == 5:
        print("\nRequerimiento No 3 del reto 3: ")

    elif int(inputs[0]) == 6:
        print("\nRequerimiento No 4 del reto 3: ")
        fechamin = input('Ingrese la fecha menor YYYY-MM-DD: \n')
        fechamax = input('Ingrese la fecha mayor YYYY-MM-DD: \n')
        controller.req4(cont, fechamin, fechamax)

    elif int(inputs[0]) == 7:
        print("\nRequerimiento No 5 del reto 3: ")
        h1 = input('Ingrese la hora menor en formato 24h (HH:MM): \n')
        h2 = input('Ingrese la hora mayor en formato 24h (HH:MM): \n')
        controller.req5(cont, h1, h2)

    elif int(inputs[0]) == 8:
        print("\nRequerimiento No 6 del reto 3 (bono): ")
        radio = float(input('Ingrese el radio en kilómetros: \n'))
        lat = float(input('Ingrese la latitud: \n'))
        lon = float(input('Ingrese la longitud: \n'))
        controller.ejecutarreq6(cont, lat, lon, radio)

    else:
        sys.exit(0)
sys.exit(0)
