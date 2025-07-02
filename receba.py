line = int(input("digite o número de linhas da matriz: "))
colunas = int(input("digite o número de colunas da matriz: "))
matriz = []

#recebe valores da matriz
for cortinas in range(line):
    ordemOK = True
    while ordemOK: #garante que o input repita caso os elementos estejam a mais
        entrada = input(f"Digite os valores da linha {cortinas+1}, separados por espaço: ")
        valores = entrada.split()
    
        #verifica se a quantidade de elementos bate com a quantidade de colunas e adiciona os elementos certos na matriz
        if len(valores) == colunas:
            linha = []
            for YE in valores:
                linha.append(int(YE))
            matriz.append(linha)
            ordemOK = False
        else:
            ordemOK = True

#printar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)