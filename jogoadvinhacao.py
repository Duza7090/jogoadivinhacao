import random
print('Jogo da advinhação!')

numero = random.randrange(1, 101)
rodada = 0
print('Escolha seu nível de dificuldade:\n(1) Fácil\t(2)Médio\t(3)Difícil')
nivel = int(input('Digite o nível desejado: '))
if nivel == 1:
    tentativa = 20
elif nivel == 2:
    tentativa = 10
else:
    tentativa = 5
pontuacao=100
while rodada <= tentativa:
    chute = int(input('Digite seu número: '))
    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue
    if chute == numero:
        print("Parabéns! Você acertou")
        break
    else:
        if chute < numero:
            print('Seu chute foi menor que o número correto!')
            ponto=abs(numero-chute)
            pontuacao-=ponto
        else:
            print('Seu chute foi maior que o número correto!')
            ponto=abs(numero-chute)
            pontuacao-=ponto
    rodada += 1
print('Fim de jogo')
print('O número correto era {}'.format(numero))
print("Sua pontuação é {} pontos!".format(pontuacao))