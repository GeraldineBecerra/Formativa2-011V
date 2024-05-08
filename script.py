valorPikachu = 4500
valorOtaku = 5000
valorPulpo = 5200
valorAnguila = 4800
rollPikachu = 0
rollOtaku = 0
rollPulpo = 0
rollAnguila=0
totalPikachu = 0
totalOtaku = 0
totalPulpo = 0
totalAnguila = 0
otraCompra = 1
descuentoAplicado=0
print('Bienvenido a Sushi')
print('¿Que deseas pedir?')
menu = print(' 1. Pikachu Roll\n 2. Otaku Roll\n 3. Pulpo Venenoso Roll\n 4. Anguila Eléctrica Roll')


respuesta =int( input('Elija una opcion ingresando el numero del roll seleccionado: '))
#while otraCompra == '1':
    
if(respuesta == 1 ):
        rollPikachu = rollPikachu + 1
        totalPikachu = rollPikachu * 4500
        print('compraste un pikachu: ' , rollPikachu)
       
elif(respuesta == 2):
        rollOtaku = rollOtaku + 1
        totalOtaku = rollOtaku * 5000

        print('compraste un otaku: ' , rollOtaku)
        print(totalOtaku,'valor')
        
elif(respuesta == 3):
        rollPulpo = rollPulpo + 1
        totalPulpo = rollPulpo * 5200
        print('compraste un pulpo: ' , rollPulpo)
      
elif(respuesta == 4):
        rollAnguila = rollAnguila + 1
        totalAnguila= rollAnguila * 4800
        print('compraste un anguila: ' , rollAnguila)

totalProductos = rollPikachu  + rollPulpo + rollOtaku + rollAnguila 
print('toal productos', totalProductos)

otraCompra = int(input('¿Desea agregar otro roll a su pedido? 1)si 2)no : '))
    
totalAntesDescuento = totalPikachu + totalOtaku + totalPulpo + totalAnguila
print(totalAntesDescuento)
print(totalAntesDescuento)
descuento = input('¿posee un código de descuento?\n Ingresa el codigo de descuento: ')
if(descuento == 'soyotaku'):
    descuentoAplicado = (totalAntesDescuento * 0.1)
    print(descuentoAplicado)
else:
    print('código no válido')
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

