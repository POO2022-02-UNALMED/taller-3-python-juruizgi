class Control:
  _tv = None

  def enlazar(self,tv):
    self._tv = tv
    tv.setControl(self)
  
  def getTv(self):
    return self._tv
  
  def setTv(self,tv):
    self._tv = tv
  
  def turnOn(self):
    self._tv.turnOn()
  
  def turnOff(self):
    self._tv.turnOff
  
  def canalUp(self):
    self._tv.canalUp()
  
  def canalDown(self):
    self._tv.canalDown()
  
  def volumenUp(self):
    self._tv.volumenUp()
  
  def volumenDown(self):
    self._tv.volumenDown()
  
  def setCanal(self,canal):
    self._tv.setCanal(canal)





class Marca:

  def __init__(self,nombre):
    self._nombre = nombre

  def getNombre(self):
    return self._nombre

  def setMarca(self,nombre):
    self._nombre = nombre





class TV:
  _numTV = 0
  def __init__(self,marca,estado):
    _canal = 1
    _precio = 500
    _volumen = 1
    _control = None
    self._marca = marca
    self._estado = estado
    TV._numTV+=1
  
  def setMarca(self,marca):
    self._marca = marca
  
  def getMarca(self):
    return self._marca
  
  def setControl(self,control):
    self._control = control
  
  def getControl(self):
    return self._control
  
  def setPrecio(self,precio):
    self._precio = precio
  
  def getPrecio(self):
    return self._precio
  
  def setVolumen(self,volumen):
    if volumen>=0 and volumen<=7:
      self._volumen = volumen

  def getVolumen(self):
    return self._volumen
  
  def setCanal(self,canal):
    if canal<=120 and canal >=1 and self._estado ==True:
      self._canal = canal
    
  def getCanal(self):
    return self._canal
  
  @classmethod
  def setNumTV(cls,numTV):
    cls.numTV = numTV
  
  def turnOn(self):
    self._estado = True
  
  def turnOff(self):
    self._estado = False
  
  def getEstado(self):
    return self._estado
  
  def canalUp(self):
    if self._canal!=120 and self._estado == True:
      self._canal+=1

  def canalDown(self):
    if self._canal!=1 and self._estado == True:
      self._canal-=1
  
  def volumenUp(self):
    if self._volumen!=7 and self._estado == True:
      self._volumen+=1
  
  def volumenDown(self):
    if self._volumen!=0 and self._estado == True:
      self._volumen-=1