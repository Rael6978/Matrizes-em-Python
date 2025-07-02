#criando uma matriz
line = int(input("digite o número de linhas da matriz: "))
colunas = int(input("digite o número de colunas da matriz: "))
matriz = []

#recebendo os elementos da matriz
for i in range(line):
    print(f"digite os valores da linha {i+1}, separados")
    entrada = (input())
    valores = entrada.split()
    linha = []
    for YE in valores:
        linha.append(int(YE))
    matriz.append(linha)

#printar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)