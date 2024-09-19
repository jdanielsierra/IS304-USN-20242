def main():
    # Inicializa el inventario como un diccionario
    inventario = {}
    
    # Ejemplo de entradas: agregar nombre_producto cantidad
    # Tu código aquí
    
if __name__ == '__main__':
    main()
    
    UMBRAL_BAJO = 5

def mostrar_inventario(inventario):
    print("\nMostrar Inventario")
    if not inventario:
        print("El Inventario esta Vacio")
        return
    for producto, cantidad in inventario:
        estado = "Bajo" if cantidad < UMBRAL_BAJO else "Cantidad Suficiente"
        print(f"{producto}: {cantidad} unidades - Estado: {estado}")
        
        
    def agregar_producto(inventario, producto, cantidad)
