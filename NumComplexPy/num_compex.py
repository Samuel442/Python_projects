# Calculando números complexos na forma algébrica

import cmath


p_real1 = float(input("Digite a parte real do primeiro número complexo: "))
p_imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
z1 = complex(p_real1,p_imag1)
print("Número complexo digitado: ",z1)

p_real2 = float(input("Digite a parte real do segundo número complexo: "))
p_imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
z2 = complex(p_real2,p_imag2)
print("Número complexo digitado: ",z2)

print(" ")

# Operações

soma = z1 + z2
subtracao = z1 - z2
produto = z1 * z2
divisao = z1 / z2

print("Soma :",soma)
print("Subtração :",subtracao)
print("Multiplicação :",produto)
print("Divisão :",divisao)