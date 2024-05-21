from math import *

#region Calculos

def calcular_area_rectangulo(base, altura):
    area = base * altura
    
    return area

def calcular_perimetro_rectangulo(base, altura):
    perimetro = (base + altura) * 2
    
    return perimetro

def calcular_area_circulo(radio):
    area = pi * radio**2
    
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    
    return perimetro

def calcular_area_triangulo_rectangulo(base, altura):
    area = (base * altura) / 2
    
    return area

def calcular_perimetro_triangulo_rectangulo(base, altura):
    perimetro = sqrt(base**2 + altura**2)
    
    return perimetro


#endregion

    
