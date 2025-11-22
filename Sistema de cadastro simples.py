lista = []
def cadastrar():
    while True: 
        n=input('digite o  nome: ')
        lista.append(n)
        condicao = input("quer continuar digitando nomes  s/n: ").strip().lower()
        if condicao == "n" :
            print()
            break
    
def listar():
    print()
    if lista:
        print('==========nomes cadastrados============')
        for i in lista:
            print(i)
    else:
        print('nenhum nome encontrado')
        print()
        print('cadastre os nomes antes de tentar listar eles ')
    print()



def remover_usuario():
    print()
    nome=str(input('digite o nome que deseja remover: '))
    if not lista:
        print('a lista esta vazia')
    else:
        if nome in lista:
            lista.remove(nome)
            print('nome removido com sucesso')
        else:
            print('o item não esta na lista')

        
def main():
    while True:
        print('================Menu===================')
        print('1- cadastrar nomes')
        print('2- listar nomes cadastrados')
        print('3-remover nomes')
        print('4-sair')
        print('========================================')
        try:
            op=int(input('digite a opção que deseja : '))
        except:
            print('opção invalida')
            continue
        if op == 1:
            cadastrar()
        elif op == 2:
            listar()
        elif op == 3:
            remover_usuario()
        elif op == 4:
            print('programa encerrado')
            break
        else:
            print('opção invalida digite apenas opções validas')
main()




    

