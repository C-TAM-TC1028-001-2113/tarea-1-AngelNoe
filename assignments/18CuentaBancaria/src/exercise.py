def main():
    # escribe tu código abajo de esta línea
    mes_anterior=float(input('Dame el saldo del mes anterior:'))
    ingresos=float(input('Dame los ingresos:'))
    egresos=float(input('Dame los egresos:'))
    cheques=int(input('Numero de cheques expedidos:'))
    costocheq=cheques*13
    
    saldo=(mes_anterior+ingresos-egresos-costocheq)
    interes=saldo*0.075
    saldofinal=saldo-interes
    
    print('El saldo final de la cuenta es:',saldofinal)
if __name__ == '__main__':
    main()
