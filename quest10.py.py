print('Informe duas datas para saber qual a maior: ')
#primeira data
dia1 = int(input("Informe um dia: "))
mes1 = int(input("Informe um mês: "))
ano1 = int(input("Informe um ano: "))
# Segunda data.
dia2 = int(input("Informe outro dia: "))
mes2 = int(input("Informe outro mês: "))
ano2 = int(input("Informe outro ano: "))
 
if ano1>ano2 or (ano1==ano2 and mes1>mes2) or (ano1==ano2 and mes1==mes2 and dia1>dia2):
    print("Data1 é maior.")
elif ano1==ano2 and mes1==mes2 and dia1==dia2:
    print("As duas datas são iguais!")
else:
    print("Data2 é maior!")