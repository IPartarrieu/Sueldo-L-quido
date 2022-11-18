Ingreso = int(input('\nIngrese su sueldo: '))
#print('Ingreso: ',Ingreso)

TRABAJO =str(input('¿honorario o contrato? '))
#descuentos

while TRABAJO != 'honorario' and TRABAJO != 'contrato':
    TRABAJO=str(input('Ingrese honorario o contrato: '))



if TRABAJO == 'contrato':
    FONASA = Ingreso*0.07
    GES = 0
    AFP = Ingreso*0.1116
    AFC = Ingreso*0.006

    print('\nDESCUENTOS','\nFONASA: ',FONASA,'\nGES: ',GES,'\nAFP PlanVital: ',AFP,'\nAFC: ',AFC)

    imponible = Ingreso-(FONASA+GES+AFP+AFC)
    print('\n\nSUELDO IMPONIBLE: ',imponible)

    if imponible<=821515.5:
        tasa = 'EXENTO'
        impuesto=0
    elif 821515.51<=imponible<=1825590:
        tasa=0.022
        impuesto=imponible*tasa
    elif 1825590.01<=imponible<=3042650:
        tasa=0.0452
        impuesto=imponible*tasa
    elif 3042650.01<=imponible<=4259710:
        tasa=0.0709
        impuesto=imponible*tasa
    elif 4259710.01<=imponible<=5476770:
        tasa=0.1062
        impuesto=imponible*tasa
    elif 5476770.01<=imponible<=7302360:
        tasa=0.1557
        impuesto=imponible*tasa
    elif 7302360.01<=imponible<=18864430:
        tasa=0.2748
        impuesto=imponible*tasa
    elif 18864430.01<=imponible:
        tasa=0.2749
        impuesto=imponible*tasa
elif TRABAJO=='honorario':
    tasa=0.1225
    imponible=Ingreso
    impuesto=imponible*tasa


liquido = imponible-impuesto
print('\nTASA: ',tasa,'\nIMPUESTO: ',impuesto,'\n\nSUELDO LÍQUIDO: ',liquido)

Renta = int(input('\n¿Cuánto pagará mensualmente por su alquiler? '))
while Renta<0:
    Renta = int(input('\n¿Cuánto pagará mensualmente por su alquiler? '))

Comida = int(input('¿Cuánto gastará mensualmente en comida? '))
while Comida<0:
    Comida = int(input('¿Cuánto gastará mensualmente en comida? '))

Transporte = int(input('¿Cuánto gastará mensualmente en transporte? '))
while Transporte<0:
    Transporte = int(input('¿Cuánto gastará mensualmente en transporte? '))

#Cuentas promedio
Gas = 20000
Luz = 10000
Agua = 10000
Internet = 10000


Disponible = liquido-(Renta+Comida+Transporte+Gas+Luz+Agua+Internet)

if Disponible<=0:
    print('\nSUELDO NO VIABLE: ',Disponible)

print('\nCUENTAS PROMEDIO (Gas, luz, agua, internet u otros): ',Gas+Luz+Agua+Internet,'\nGASTOS MENSUALES (arriendo, comida y transporte): ',Renta+Comida+Transporte,'\nDINERO DISPONIBLE: ',Disponible)

#sugeribles
emergencias = Disponible*0.05
futuro = 10000
total = Disponible-(emergencias+futuro)
print('\nSUGERIBLES','\nEmergencias: ',emergencias,'\nAhorros para futuro: ',futuro,'\nTotal disponible: ',total,'\n')
