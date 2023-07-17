import random
import os

random_list = random.sample(range(1000), 100)
random_list.sort()
print(random_list)
number = int(input("Digite o número procurado: "))
divisor = len(random_list) / 2
posicao_atual = divisor
i = 0
while i < 50:
    atual = random_list[int(posicao_atual)]
    if atual == number:
        print("Número encontrado na posição " + str(int(posicao_atual) + 1))
        print("Foram necessárias " + str(i + 1) + " iterações")
        break
    else:
        divisor /= 2
        if atual > number:
            posicao_atual = posicao_atual - divisor
        else:
            posicao_atual = posicao_atual + divisor
    if i == 49:
        print(-1)
    i += 1
os.system("pause")
