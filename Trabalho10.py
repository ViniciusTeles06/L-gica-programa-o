def main():
    n = int(input("Quantidade de números: "))
    numeros = [int(input(f"Número {i+1}: ")) for i in range(n)]

    print("\na) Ordem inversa:")
    for num in reversed(numeros):
        print(num)

    print("\nb) Ordem decrescente:")
    for num in sorted(numeros, reverse=True):
        print(num)

if __name__ == "__main__":
    main()
#terminei