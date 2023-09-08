# se crea un diccionario de productos y precios
productos = {
    "cafe": 4.75,
    "arroz": 0.75,
    "pollo": 2.00,
    "repollo": 2.50,
}

# se  solicita al usuario el nombre del producto y la cantidad
nombre_producto = input("Ingrese el nombre del producto: ")

# verificamos si el producto está en el diccionario
if nombre_producto in productos:
    cantidad = int(input("Ingrese la cantidad deseada: "))
    precio_unitario = productos[nombre_producto]
    total_pagar = precio_unitario * cantidad
    print("Total a pagar por {0} unidades de {1}: ${2:.2f}".format(cantidad, nombre_producto, total_pagar))
else:
    print("El producto no se encuentra disponible.")


