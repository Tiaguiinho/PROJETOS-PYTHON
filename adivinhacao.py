import random

def jogar_adivinhacao():

    print("***********************************")
    print("*Bem vindo ao jogo de adivinhação!*")
    print("***********************************")

    #INTEIRO
    numero_Secreto = round(random.randrange(1, 101)) #random() gera um numero entre 0.0 e 1.0
    total_DE_tentativas = 0
    pontos = 1000
    #rodada = 1 || antes era declarada para uso no while()

    print("Qual nível de dificuldade?")
    print("(1) FÁCIL (2) MÉDIO (3) DIFÍCIL")

    dificuldade_valida = False
    #input devolve uma string, entao colocamos int p converter...
    while(dificuldade_valida == False):
        nivel = int(input("Digite o nível: "))
        if(nivel == 1):
            total_DE_tentativas = 20
            dificuldade_valida = True
        elif(nivel == 2):
            total_DE_tentativas = 10
            dificuldade_valida = True
        elif(nivel == 3):
            total_DE_tentativas = 5
            dificuldade_valida = True
        else:
            print("Você deve escolher a dificuldade entre 1 (FACIL), 2( MÉDIO) e 3 (DIFICIL)")

    for rodada in range(1, total_DE_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_DE_tentativas)) #string interpolation
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!!!")
            continue

    #BOOLEAN
        acertou = numero_Secreto == chute
        maior = chute > numero_Secreto
        menor = chute < numero_Secreto
        final = rodada == total_DE_tentativas

        if(acertou):
            print("Você acertou! Fez {} pontos" .format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi MAIOR do que o número secreto!")
                if(final):
                    print("O número secreto era {}. Você fez {} pontos" .format(numero_Secreto, pontos))
            elif(menor):
                print("Você errou! Seu chute foi MENOR do que o número secreto!")
                if(final):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_Secreto, pontos))

        pontos_perdidos = abs(numero_Secreto - chute)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("FIM DO JOGO!")

if(__name__== "__main__"):
    jogar_adivinhacao()