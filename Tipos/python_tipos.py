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

class TipoDatosClave(Enum):
  '''Tipos de Datos Soportados x la clave'''
  NUMERO=1
  CADENA=2
  OTROS=3

class TipoElemento():
  '''Datos a Guardar dentro de las estructuras'''
  def __init__(self, clave=None, Valor1=None, Valor2=None):
    self.clave = clave
    self.Valor1 = Valor1
    self.Valor2 = Valor2