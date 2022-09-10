listaFrutas=[]

for i in range(0,10,1):
    nombreFruta = input(f'Digite el nombre de la fruta {i}: ')
    colorFruta = input(f'Digite el color de la fruta {i}: ')
    precioFruta = float(input(f'Digite el precio de la fruta {i}: '))
    print("")

    listaFrutas.append({'Nombre: ':nombreFruta, 'Color Fruta: ':colorFruta, 'Precio Fruta: ':precioFruta})

#for i in range(9,-1,-1):
#   print(listaFrutas[i])

for item in reversed(listaFrutas):
    print(item)