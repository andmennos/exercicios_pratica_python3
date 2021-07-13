print("**************************")
print("Bem vindo ao Jogo da Adivinhação")
print("**************************")

numero_secreto = 42
tentativas = 1
total_de_tentativas = 3

for tentativas in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(tentativas, total_de_tentativas))
    chute = int(input("Chute um número entre 1 e 100: "))
    print("Você digitou: ", chute)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!!")
        break

    elif maior:
        print("Você errou! O número que você chutou é maior que o número secreto")

    elif menor:
        print("Você errou! O número que você chutou é menor que o número secreto")

print("Fim do jogo")
