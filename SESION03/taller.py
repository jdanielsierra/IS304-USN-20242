'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
class CuentaBancaria:
def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
  self.__numeroCta = numeroCta
  self.__nombreCliente = nombreCliente
  self.__saldoCta = saldoCta
  self.__fechaApertura =fechaApertura
  self.__ultuimoRetiro = ultimoRetiro
  self.__ultimaCosignacion = ultimaConsignacion

def set(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion)
  self.__numeroCta = numeroCta
  self.__nombreCliente = nombreCliente
  self.__saldoCta = saldoCta
  self.__fechaApertura = fechaApertura
  self.__ultuimoRetiro = ultimoRetiro
  self.__ultimaCosignacion = ultimaConsignacion


def set_numeroCta(self, x):
  self.__numeroCta = x

def set_nombreCliente(self, x):
  self.__nombreCliente = x
  
def set_saldoCta(self, x):
  self.__saldoCta = x

def set_fechaApertura(self, x):
  self.__fechaApertura = x

def set_ultimoRetiro(self, x):
  self.__ultimoRetiro = x

def set_ultimaConsignacion(self, x):
  self.__ultimaConsignacion = x


def MostrarMenu():
  print("Menu Principal")
  print("1. Apertura de Cuenta")
  print("2. Consignar")
  print("3. Retirar")
  print("4. Transferencia")
  print("5. Activaciones de Token")
  print("6. Certificados")
  print("7. Bloqueo de Tarjetas")
  print("8. Cuenta Bolsillo")
  print("9. Consultas de Saldos")
  print("10. CDT")






  
