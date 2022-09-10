multDos = 0
multTres = 0

numeros = int(input("Digite cuantos numeros desea ingresar: "))

for i in range(0,numeros,1):
    num = float(input("Digite el numero: "))
    if(num%2==0 and num%3==0):
        multDos = multDos + 1
        multTres = multTres + 1
    if(num%2==0):
        multDos = multDos+1
    if(num%3==0):
        multTres = multTres+1

print(f'La cantidad de numeros que ingreso son {numeros}, la cantidad de multiplos de dos son: {multDos} y la cantidad de numeros de tres son: {multTres}')


