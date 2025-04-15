texto = input()

caractere = input()

if caractere in texto:
    print(texto.index(caractere))
else:
    print(-1)
