#Entrada de dados
nota1=float(input("Informe sua primeira nota: "))
nota2=float(input("Informe sua segunda nota: "))
nota3=float(input("Informe sua terceira nota: "))

#Processamento de dados
mediaarit=float(nota1 + nota2 + nota3) / 3

print(f"A sua Média Aritmética é: {round(mediaarit,1)}")

if mediaarit >= 0 and mediaarit <= 3:
    print("Você foi Reprovado(a). ")
elif mediaarit >= 3 and mediaarit <= 7:
    print("Você foi Selecionado(a) para o Exame. ")
    notaex = 12 / 2
    print(f"A nota miníma que você precisará tirar é: {notaex}")

elif mediaarit >= 7 and mediaarit <= 10:
    print("Parábens, você foi Aprovado(a). ")

