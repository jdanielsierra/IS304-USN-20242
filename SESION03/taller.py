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

    def set(self, numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion):
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

def seleccion_opcion():
    while True:
        MostrarMenu()
        opcion = input("\nSeleccione una Opción: ")

        if opcion == "1":
            apertura_de_Cuenta()
        elif opcion == "2":
            consignar()
        elif opcion == "3":
            retiros()
        elif opcion == "4":
            transferencias()
        elif opcion == "5":
            activaciones_token()
        elif opcion == "6":
            certificados()
        elif opcion == "7":
            bloqueo_tarjetas()
        elif opcion == "8":
            cuenta_bolsillo()
        elif opcion == "9":
            consultas_saldos()
        elif opcion == "10":
            cdt()
        elif opcion == "0":
            print("\nSaliendo del Sistema...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del menú.")



def apertura_de_Cuenta():
    print("Haz seleccionado Apertura de cuenta")
    input("Presiona Enter para volver al menú principal")

def consignar():
    print("Haz seleccionado Consignaciones")
    input("Presiona Enter para volver al menú principal")

def retiros():
    print("Haz seleccionado Retiros")
    input("Presiona Enter para volver al menú principal")

def transferencias():
    print("Haz seleccionado Transferencias")
    input("Presiona Enter para volver al menú principal")

def activaciones_token():
    print("Haz seleccionado Activaciones de Token")
    input("Presiona Enter para volver al menú principal")

def certificados():
    print("Haz seleccionado Certificados")
    input("Presiona Enter para volver al menú principal")

def bloqueo_tarjetas():
    print("Haz seleccionado Bloqueos de Tarjetas")
    input("Presiona Enter para volver al menú principal")

def cuenta_bolsillo():
    print("Haz seleccionado Cuenta Bolsillo")
    input("Presiona Enter para volver al menú principal")

def consultas_saldos():
    print("Haz seleccionado Consultas de Saldos")
    input("Presiona Enter para volver al menú principal")

def cdt():
    print("Haz seleccionado CDT")
    input("Presiona Enter para volver al menú principal")

seleccion_opcion()


  








  
