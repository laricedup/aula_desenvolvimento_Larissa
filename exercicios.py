#Exercício 1:

valorA = int(input("Digite um valor: "))
valorB = int(input("Digite um segundo valor: "))
valorC = int(input("Digite um terceiro valor: "))
valorD = int(input("Digite um quarto valor: "))
valorE = int(input("Digite um quarto valor: "))


soma = (valorA + valorB + valorC + valorD + valorE)
print(soma)

#Exercício 2:
valorA = int(input("Digite um valor: "))
valorB = int(input("Digite um segundo valor: "))
valorC = int(input("Digite um terceiro valor: "))
valorD = int(input("Digite um quarto valor: "))


lista = [valorA, valorB, valorC, valorD]
print(min(lista))
print(max(lista))


#Exercício 3:
contador = 0
palavra = input("Digite uma palavra: ")
lista_vogais = ['a', 'e', 'i', 'o', 'u']


for letra in palavra:
    for vogal in lista_vogais:
        if(letra == vogal):
            contador += 1


print(f'O Número de vogais na palavra {palavra} é de {contador}')

#Exercício 4:
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int (input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int (input("Digite o quinto numero: "))
numero6 = int(input("Digite o sexto numero: "))


lista_pares = []
lista_numeros = [numero1, numero2, numero3, numero4, numero5, numero6]


for numero_digitado in lista_numeros:
    if numero_digitado % 2 == 0:
        lista_pares.append(numero_digitado)
if len(lista_pares) == 0:
    print(f'Lista de numeros {lista_numeros} não possui nenhum numero par' )


else:
    print(f'A lista digitada contém os seguntes números pares {lista_pares}')


#Exercício 5:
valorA = float(input("Digite sua primeira nota: "))
valorB = float(input("Digite sua segunda nota: "))
valorC = float(input("Digite sua terceira nota: "))
valorD = float(input("Digite sua quarta nota: "))


som_media = (valorA + valorB + valorC + valorD )
media_final = (som_media / 4)
print (media_final)


#Exercício 6:
numeroDigitado = int(input("Digite um número: "))
for numero in range(1,11):
    print(f"{numeroDigitado} x {numero} = {numeroDigitado * numero}")


#Exercício 07:
numeroDigitado = int(input("Digite um número: "))


for numero in range(1,numeroDigitado + 1):
  print(f'{numero}')

#Exercício 08:
palavraDigitada= input("Digite uma Palavra: ")


palavraReversa =  palavraDigitada [:: -1]


print(f'O contrário da palavra {palavraDigitada} é: {palavraReversa}')


#Exercício 09:
numeroDigitado = int(input(“Digite um número: “))
if numeroDigitado %3== 0:
    print(f'o numero {numeroDigitado} é multiplo de 3')
else:
    print (f'O numero {numeroDigitado} não é multiplo de 3')


#Exercício 10:
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")


listaDeNomes = [nome1, nome2, nome3]


listaDeNomes.sort(reverse=False)


print(f'Os nomes em ordem alfabética são: {listaDeNomes}')


