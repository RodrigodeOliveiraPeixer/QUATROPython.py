#4- Criar um vetor de cinco posições, solicitar  cinco números e ao fim, imprimir o valor apresentado na posição três.


vetor = []
for i in range(5):
    num = int(input("Insira um número: "))
    vetor.append(num)

print("O valor na posição três é:", vetor[2])
