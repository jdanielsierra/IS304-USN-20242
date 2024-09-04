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
    print("\nMenu Principal")
    print("\n1. Apertura de Cuenta")
    print("2. Consignaciones")
    print("3. Retiros")
    print("4. Transferencias")
    print("5. Activaciones de Token")
    print("6. Certificados")
    print("7. Bloqueo de Tarjetas")
    print("8. Cuenta Bolsillo")
    print("9. Consultas de Saldos")
    print("10. CDT")
    print("0. Volver")

def seleccion_mostrar():
    MostrarMenu()
    opción = 



def apertura_de_Cuenta():
    print("Haz seleccionado Apertura de cuenta")

def consignar():
    print("Haz seleccionado Consignaciones")

def retiros():
    print("Haz seleccionado Retiros")

def transferencias():
    print("Haz seleccionado Transferencias")

def activaciones_token():
    print("Haz seleccionado Activaciones de Token")

def certificados():
    print("Haz seleccionado Certificados")

def bloqueo_tarjetas():
    print("Haz seleccionado Bloqueos de Tarjetas")

def cuenta_bolsillo():
    print("Haz seleccionado Cuenta Bolsillo")

def consultas_saldos():
    print("Haz seleccionado Consultas de Saldos")

def cdt():
    print("Haz seleccionado CDT")


  








  
