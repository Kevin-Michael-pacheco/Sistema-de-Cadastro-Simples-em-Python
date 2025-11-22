lista = []

def cadastrar():
    while True: 
        n=input('digite o  nome: ')
        lista.append(n)
        condicao = input("quer continuar digitando nomes  s/n: ")
        if condicao == "n" or condicao == "N":
            break
cadastrar()