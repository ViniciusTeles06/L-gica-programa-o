num=int(input("Digite um número:"))
if num<=1:
 print(num,"não é primo")
else:
 for i in range(2,num):
  if num%i==0:
   print(num,"não é primo")
   break
 else:
  print(num,"é primo")
