nome = str(input("Qual é o seu nome: "))
idade = int(input("Qual a sua idade? "))

autor = idade > 18
print(autor)

if autor == True:
    print(nome, "Autorizado!")
else:
    print(nome, "Não autorizado! ")