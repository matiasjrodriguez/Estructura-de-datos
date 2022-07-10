from Tipos.python_tipos import TipoDatosClave, TipoElemento, Resultado

MIN = 1
MAX = 2000
NULO = 0
PosicionLista = int

class Nodo:
  def __init__(self):
    self.dato = None
    self.anterior = None
    self.proximo = None

class Lista:
  def __init__(self, TipoClave:TipoDatosClave, alSize:int): # Lista.Crear() 
    '''Crea una lista vacía''' 
    if alSize >= MIN and alSize <= MAX:
      self._cursor = []
      for Q in range(alSize + 1): # La posicion 0 no la usamos pero hay que tenerla en cuenta | Reemplaza SetLength
        nodo = Nodo()
        self._cursor.append(nodo)
        if Q > 0:
          self._cursor[Q].proximo = Q + 1 # Encadenamientos de Libres
        
      self._cursor[alSize].proximo = NULO
      
      self._inicio = NULO
      self._final = NULO
      self._libre = MIN
      self._Q_Items = 0
      self._TDatoDeLaClave = TipoClave
      self._Size = alSize

  def EsVacia(self) -> bool: 
    '''Control de lista vacia'''
    return self._inicio == NULO

  def EsLlena(self) -> bool: 
    '''Control de lista llena'''
    return self._libre == NULO

  def Siguiente(self, P:PosicionLista) -> PosicionLista:
    '''Proximo de P o NULO'''
    if self.EsVacia() or P == NULO:
      Q = NULO
    else:
      Q = self._cursor[P].proximo

    return Q