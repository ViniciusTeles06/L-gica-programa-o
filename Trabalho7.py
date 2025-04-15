string=input("Digite uma palavra:")
if len(string)>=100:
    print("A palavra digitada é muito longa!")
    exit()
letra1=input("Digite a letra que deseja substituir:")
letra2=input("Digite a letra que deseja colocar no lugar:")
stringalterada=string.replace(letra1,letra2)
print("A palavra alterada é:", stringalterada)