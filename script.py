rollPikachu = 0
rollOtaku = 0
rollPulpo = 0
rollAnguila=0
totalPikachu = 0
totalOtaku = 0
totalPulpo = 0
totalAnguila = 0
otraCompra = True
descuentoAplicado=0
otroCod= True
print('Bienvenido a Sushi')
print('¿Que deseas pedir?')

while otraCompra ==True:
    menu = print(' 1. Pikachu Roll\n 2. Otaku Roll\n 3. Pulpo Venenoso Roll\n 4. Anguila Eléctrica Roll')
    respuesta =int( input('Elija una opcion ingresando el numero del roll seleccionado: '))

    if(respuesta == 1 ):
        rollPikachu = rollPikachu + 1
        totalPikachu = rollPikachu * 4500
       
    elif(respuesta == 2):
        rollOtaku = rollOtaku + 1
        totalOtaku = rollOtaku * 5000

    elif(respuesta == 3):
        rollPulpo = rollPulpo + 1
        totalPulpo = rollPulpo * 5200
    elif(respuesta == 4):
        rollAnguila = rollAnguila + 1
        totalAnguila= rollAnguila * 4800
    otraCompra = int(input('¿Desea agregar otro roll a su pedido? 1)si 2)no : '))

totalProductos = rollPikachu  + rollPulpo + rollOtaku + rollAnguila 
totalAntesDescuento = totalPikachu + totalOtaku + totalPulpo + totalAnguila

descuento = input('¿Posee un código de descuento?\n Ingresa el codigo de descuento: ')

if(descuento == 'soyotaku'):
        descuentoAplicado = (totalAntesDescuento * 0.1)
       
else:
    otroCod= input('código no válido\n Desea ingresar otro codigo? si/no: ')
    if(otroCod =='no'):
        volver = input('Desea volver al menu presione X ')
        if(volver):
            otraCompra = True
totalConDescuento = totalAntesDescuento - descuentoAplicado
print('*'*30)
print('TOTAL PRODUCTOS: ' ,totalProductos)
print('*'*30)
print('Pikachu Roll: ' ,rollPikachu )
print('Otaku Roll: ' ,rollOtaku )
print('Pulpo Venenoso Roll: ' ,rollPulpo )
print('Anguila Eléctrica Roll: ' ,rollAnguila )
print('*'*30)
print('Subtotal por pagar: ', totalAntesDescuento)
print('Descuento por código: ', descuentoAplicado)
print('TOTAL: ', totalConDescuento)