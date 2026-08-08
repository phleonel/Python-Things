#1-

nome = input("Entre com seu nome: ")
nome_minusculo = nome.lower()
nome_maiusculo = nome.upper()
print("Seu nome em minusculo:",nome_minusculo)
print("Seu nome em maiusculo:",nome_maiusculo)

quantidade = len(nome)
print("Quantidade de letras:",quantidade)

nome = nome.split()
nome[-1] = "do Inatel"
nome_modificado = " ".join(nome)
print("Nome modificado:",nome_modificado)

#2-

x = int(input("Seu número: "))
y = int(input("Seu intervalo: "))
for i in range(1, 11, y):
  print(x*i)

#3-
sexo = input("Você é homem ou mulher (M = Homem, F = Mulher): ").upper()

while(sexo != "M" and sexo != "F"):
  sexo = input("Você é homem ou mulher (M = Homem, F = Mulher): ").upper()

if sexo == "M":
    print("Você é homem")
elif sexo == "F":
    print("Você é mulher")

#4-

import math

distancia = float(input("Qual a distância da viagem (em Km): "))
if(200 >= distancia >= 1):
  preco = math.trunc(distancia) * 0.50
elif(1 > distancia >= 0 or distancia == 0):
  print("Inválido")
else:
  preco = math.trunc(distancia) * 0.45

if(preco>=1):
  print("Preço da viagem:",preco)

#5-

numero = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= numero <= 9999:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = numero // 1000

    print(f"Número da unidade: {unidade}")
    print(f"Número da dezena: {dezena}")
    print(f"Número da centena: {centena}")
    print(f"Número do milhar: {milhar}")
else:
    print("Inválido")

#6-

import math

numero = float(input("Digite um número decimal: "))

print("Raiz quadrada:", math.sqrt(numero))
print("Função teto:", math.ceil(numero))
print("Função chão:", math.floor(numero))
print("Parte inteira:", math.trunc(numero))

#7-

palavra = input("Digite uma palavra: ")

vogais = 0
tem_a = False

for letra in palavra:
    print(letra.upper())

    if letra.lower() in "aeiou":
        vogais += 1

    if letra.lower() == "a":
        tem_a = True

print("Quantidade de vogais:", vogais)

if tem_a:
    print('A letra "a" está presente.')
else:
    print('A letra "a" não está presente.')

#8-

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2
potencia = num1 ** num2

print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto da divisão:", resto)
print("Potência:", potencia)

if adicao % 2 == 0:
    print("O resultado da adição é par.")
else:
    print("O resultado da adição é ímpar.")
