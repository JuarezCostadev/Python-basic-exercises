
def salvar_em_arquivo(produtos):
    with open('produtos.txt', 'w') as arquivo:
        for produto, preco in produtos.items():
            arquivo.write(f"{produto} {preco:.2f}\n")


def carregar_do_arquivo():
    produtos = {}
    try:
        with open('produtos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                partes = linha.split()
                if len(partes) == 2:
                    produto, preco = partes
                    produtos[produto] = float(preco)
    except FileNotFoundError:
        #
        return produtos
    return produtos


def main():
    produtos = carregar_do_arquivo()

    while True:
        print("SISTEMA DE CONTROLE DE PRODUTOS")
        print("1. Listar produtos")
        print("2. Adicionar produto")
        print("3. Sair")
        print("4. Remover produto")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Lista de produtos:")
            for produto, preco in produtos.items():
                print(f"{produto}: R${preco:.2f}")
        elif opcao == '2':
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            produtos[produto] = preco
            salvar_em_arquivo(produtos)
            print(f"{produto} adicionado com sucesso!")
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            

if __name__ == "__main__":
    main()
