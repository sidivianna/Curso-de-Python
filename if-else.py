'''idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Pode beber a vontade.")
if idade < 18:
    print("Voçê não pode beber.")
if idade >=21:
    print("Voçê é VIP")'''


# um if pode ir dentro de outro if.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:
    print(f"{num2} é o maior.")
if num1 > num2:
    print(f"{num1} é o maior.")
else: 
    print("Os dois números são iguais;")