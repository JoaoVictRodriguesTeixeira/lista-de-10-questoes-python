conceito:str

#Entrada de dados
trblab = float(input('Informe sua nota do Trabalho do Laboratório: '))
avalsem = float(input('Informe sua nota da Avaliação Semestral: '))
exfinal = float(input('Informe sua nota do Exame Final: '))

ps1 = 2
ps2 = 3
ps3 = 5

#Processamento de dados
mediap=float(trblab *ps1 + avalsem *ps2 + exfinal *ps3) / (ps1+ps2+ps3)


if (mediap >= 8) and (mediap <= 10):
    conceito = "A"
elif (mediap >= 7) and (mediap < 8):
    conceito = "B"
elif (mediap >= 8) and (mediap < 7):
    conceito = "C"
elif (mediap >= 5) and (mediap < 6):
    conceito = "D"
elif (mediap >= 0) and (mediap < 5):
    conceito = "E"

#Saída de dados
print(f"A sua Média Ponderada é: {mediap}, e o seu Conceito é: {conceito} ")