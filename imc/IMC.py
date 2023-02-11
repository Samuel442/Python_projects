
# Cálculo imc sem interface

massa = float(input("Digite o sua massa em [Kg]:"))
altura = float(input("Digite sua altura em [m]:"))

calculo = massa / (altura ** 2)

if calculo < 18.5:
    print("Magreza")
elif calculo >= 18.5 and calculo <= 24.9:
    print("Saudavel")
elif calculo >= 25 and calculo <= 29.9:
    print("Sobrepeso")
elif calculo >= 30 and calculo <= 34.9:
    print("Obesidade grau I")
elif calculo >= 35 and calculo <= 39.9:
    print("Obesidade grau II")
elif calculo > 40:
    print("Obesidade grau III")