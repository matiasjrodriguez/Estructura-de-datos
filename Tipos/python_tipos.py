from enum import Enum

class Resultado(Enum):
    '''Retorno de las funciones de manejo de estructuras'''
    OK=1
    CError=2
    Llena=3
    Vacia=4
    PosicionInvalida=5
    Otro=6
    ClaveIncompatible=7
    ClaveDuplicada=8