'''n = 10
cont = 0
while cont < n:
    print(cont)
    cont = cont +1'''

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

cont = 0
produto = 1
while cont < expoente:
    produto = produto*base
    cont = cont + 1

print(f"{base} elevado a {expoente} é = {produto}.")

