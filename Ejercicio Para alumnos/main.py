from Grafico import *
from os import *
import sys
sys.path.append("Ejercicios")
from Package_Input.Input import *

def inicio_programa():
    system("cls")
    while True:
        opcion = int(input("1. Seleccionar figura y cargar valores\n2. Visualizar resultados\n3. Salir\nElija una opción: "))
        match opcion:
            case 1:
                system("cls")
                print("¿Qué tipo de figura desea representar?")
                que_figura = input("a. Círculo\nb. Rectángulo\nc. Triángulo\nd. Volver al menu anterior\nElija una opción: ")
                match que_figura:
                    case "a":
                        system("cls")
                        radio = get_int("Ingrese el radio del círculo:\n", "Debe ser un número válido", 0, inf, inf)
                        figura = {"tipo_figura": "Circulo",
                                "dimensiones": (radio,),
                                "posicion": (1000/2 - radio/2, 850/2 - radio/2 - 100),
                                "color": seleccionar_color("Ingrese el color del círculo: ")}
                    case "b":
                        system("cls")
                        base = get_int("Ingrese la base del rectángulo:\n", "Debe ser un número válido", 0, inf, inf)
                        altura = get_int("Ingrese la altura del rectángulo:\n", "Debe ser un número válido", 0, inf, inf)
                        figura = {"tipo_figura": "Rectangulo",
                                "dimensiones": (base, altura),
                                "posicion": (1000/2 - base/2, 850/2 - altura/2 - 100),
                                "color": seleccionar_color("Ingrese el color del rectángulo: ")}
                    case "c":
                        system("cls")
                        base = get_int("Ingrese la base del triángulo:\n", "Debe ser un número válido", 0, inf, inf)
                        altura = get_int("Ingrese la altura del triángulo:\n", "Debe ser un número válido", 0, inf, inf)
                        figura = {"tipo_figura": "Triangulo",
                                "dimensiones": (base, altura),
                                "posicion": (1000/2 - base/2, 850/2 - altura/2 - 100),
                                "color": seleccionar_color("Ingrese el color del triángulo: ")}
            case 2:
                graficar(figura)
            case 3:
                print("Gracias por usar nuestro programa")
                break 
            
        system("cls")   

inicio_programa()