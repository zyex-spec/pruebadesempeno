##Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
##1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
##2. Digitar 2 para mostrar todos los productos registrados (+0.4)
##3. Digitar 3 para permitir buscar por código un producto y editar el preciode este (+0.4)
##4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4)
##5. Digitar 0 para SALIR

from math import prod

i = 1
sw = 0
listaProductos=[]

while(i != 0):

    print(".:Menu:.")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto y editar precio")
    print("4. Buscar producto y eliminarlo")
    print("0. Salir")
    i= int(input("Digite la opcion: "))

    if(i == 1):
        codigoProducto = input(f'Digite el codigo de el producto: ')
        nombreProducto = input(f'Digite el nombre del producto: ')
        precioProducto = float(input(f'Digite el precio del producto: '))

        listaProductos.append({'Codigo: ':codigoProducto, 'Nombre: ':nombreProducto, 'Precio Producto: ':precioProducto})
        print("")
       
    elif(i == 2):
        for producto in listaProductos:
            print(producto)
        print("")
    elif(i == 3):
        cod = input(f'Digite el codigo del producto a buscar: ')
        for producto in listaProductos:
            if(producto["Codigo: "]== cod):
                nombre = producto["Nombre: "]
                nuevoPrecio = float(input(f'Se encontro el producto {nombre}, digite su nuevo precio: '))
                producto["Precio Producto: "] = nuevoPrecio
                print("Se actualizo el precio correctamente")
                print("")
            else:
                print(f'No se encontro el producto con codigo {cod}')
                print("")
        
    elif(i == 4):
        cod = input(f'Digite el codigo del producto a buscar: ')
        for producto in listaProductos:
            if(producto["Codigo: "]== cod):
                nombre = producto["Nombre: "]
                listaProductos.remove(producto)
                print("Se elimino el producto correctamente")
            else:
                print(f'No se encontro el producto con codigo {cod}')
                print("")         
    else:
        print('Digite una opcion valida')
