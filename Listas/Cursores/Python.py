from Tipos.python_tipos import TipoDatosClave

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
  def __init__(self, TipoClave, alSize): # Lista.Crear() 
    '''Crea una lista vacía''' 
    if alSize >= MIN and alSize <= MAX:
      self._cursor = [''] * (alSize + 1) # La posicion 0 no la usamos pero hay que tenerla en cuenta | Reemplaza SetLength
      for Q in range(MIN, alSize - 1):   # Encadenamientos de Libres
        self._cursor[Q].proximo = Q + 1
      self._cursor[alSize].proximo = NULO
      
      self._inicio = NULO
      self._final = NULO
      self._libre = MIN
      self._Q_Items = 0
      self._TDatoDeLaClave = TipoClave
      self._Size = alSize