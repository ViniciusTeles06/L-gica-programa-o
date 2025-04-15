def calcular_estatisticas(notas):
    # Calculando a média das notas
    media = sum(notas) / len(notas) #sun=sumario/len=ler e separar
    
    acima_10 = 0 #variaveis
    abaixo_10 = 0
    
    for nota in notas:          #for=pegar a nota e colocar na variaveis notas
        if nota > media * 1.10: #if=se for...
            acima_10 += 1       #elif=else=junção dos dois=if+else
        elif nota < media * 0.90:
            abaixo_10 += 1
    
    return media, acima_10, abaixo_10 #return=acabar o def

def main(): #nome da função principal
    
    n = int(input("Digite o número de alunos: "))
    

    notas = []
    for i in range(n):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    
    media, acima_10, abaixo_10 = calcular_estatisticas(notas)
    
    print(f"Média das notas: {media:.2f}")
    print(f"Notas mais de 10% acima da média: {acima_10}")
    print(f"Notas menos de 10% abaixo da média: {abaixo_10}")

if __name__ == "__main__":
    main()
