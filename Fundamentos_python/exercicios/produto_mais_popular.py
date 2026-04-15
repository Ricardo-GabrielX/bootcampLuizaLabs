produtos = input().strip().split()

contagem = {}

for p in produtos:
    if p in contagem:
        contagem[p] += 1
    else:
        contagem[p] = 1


mais_frequente = None
maior_contagem = -1


for produto in produtos:
    frequencia_atual = contagem[produto]
    
    if frequencia_atual > maior_contagem:
        maior_contagem = frequencia_atual
        mais_frequente = produto

print(mais_frequente)