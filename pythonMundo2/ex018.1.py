from datetime import date
atual = date.today().year
for i in range(0, 7):
    nasc = int(input("Em que ano a pessoa nasceu? \n"))
    idade = atual - nasc
    if idade >= 18:
        print("Essa pessoa é maior de idade")
    else:
        print("essa pessoa é menor de idade")