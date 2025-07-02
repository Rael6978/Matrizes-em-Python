line = int(input("digite o número de linhas da matriz: "))
colunas = int(input("digite o número de colunas da matriz: "))
matrizA = []

#recebe valores da matriz
for cortinas in range(line):
    ordemOK = True
    while ordemOK: #garante que o input repita caso os elementos estejam a mais
        entrada = input(f"Digite os valores da linha {cortinas+1}, da matriz A separados por espaço: ")
        valores = entrada.split()
    
        #verifica se a quantidade de elementos bate com a quantidade de colunas e adiciona os elementos certos na matriz
        if len(valores) == colunas:
            linha = []
            for YE in valores:
                linha.append(int(YE))
            matrizA.append(linha)
            ordemOK = False
        else:
            ordemOK = True

#printar a matriz
print("Matriz A:")
for linha in matrizA:
    print(linha)


matrizB = []

#recebe valores da matriz B
for cortinas in range(line):
    ordemOK = True
    while ordemOK: #garante que o input repita caso os elementos estejam a mais
        entrada = input(f"Digite os valores da linha {cortinas+1}, da matriz B separados por espaço: ")
        valores = entrada.split()
    
        #verifica se a quantidade de elementos bate com a quantidade de colunas e adiciona os elementos certos na matriz
        if len(valores) == colunas:
            linha = []
            for YE in valores:
                linha.append(int(YE))
            matrizB.append(linha)
            ordemOK = False
        else:
            ordemOK = True


#printar a matriz
print("Matriz B:")
for linha in matrizB:
    print(linha)

#soma das matrizes
for i in range(line):
    linha_soma = []
    for j in range(colunas):
        soma = matrizA[i][j] + matrizB[i][j]
        linha_soma.append(soma)
    print(linha_soma)
