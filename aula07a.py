n = str(input("Digite o nome do aluno:"))
n1 = float(input ("Digite a pimeira nota de {}:".format(n)))
n2 = float(input ("Digite a segunda:"))
s= n1+n2
m = s/2
print("A média final de {} é {}".format(n, m))
if m>6:
    print("{} PASSOU".format(n))
else:
    print("{} NÃO PASSOU".format(n))
