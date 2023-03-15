import requests

def listar_filmes():
    response = requests.get('https://sujeitoprogramador.com/r-api/?api=filmes')
    if response.status_code == 200:
        dados = response.json()
        for filme in dados:
            print(f"ID: {filme['id']} - Nome: {filme['nome']}")

def ver_detalhes_do_filme():
    id_filme = input("Digite o ID do filme: ")
    response = requests.get(f"https://sujeitoprogramador.com/r-api/?api=filmes/{id_filme}")
    if response.status_code == 200:
        dados = response.json()
        print(f"Nome: {dados['nome']}")
        print(f"Descrição: {dados['descricao']}")
        print(f"Ano: {dados['ano']}")

        opcao = input("Deseja ver os comentários? (s/n) ")
        if opcao.lower() == 's':
            print("Comentários:")
            for comentario in dados['comentarios']:
                print(f"- {comentario['usuario']}: {comentario['comentario']}")
        else:
            print("Voltando ao menu principal...")

def fazer_comentario():
    id_filme = input("Digite o ID do filme: ")
    nome_usuario = input("Digite o seu nome: ")
    comentario = input("Digite o seu comentário: ")

    dados = {
        "usuario": nome_usuario,
        "comentario": comentario
    }

    response = requests.post(f"https://sujeitoprogramador.com/r-api/?api=filmes/{id_filme}", data=dados)
    if response.status_code == 201:
        print("Comentário adicionado com sucesso!")
    else:
        print("Erro ao adicionar comentário. Tente novamente.")

def excluir_comentario():
    id_filme = input("Digite o ID do filme: ")
    id_comentario = input("Digite o ID do comentário que deseja excluir: ")

    response = requests.delete(f"https://sujeitoprogramador.com/r-api/?api=filmes/{id_filme}/{id_comentario}")
    if response.status_code == 204:
        print("Comentário excluído com sucesso!")
    else:
        print("Erro ao excluir comentário. Tente novamente.")

def menu():
    print("Escolha uma opção:\n")
    print("1 - Ver detalhes do filme")
    print("2 - Fazer um comentário do filme")
    print("3 - Excluir um comentário")
    print("4 - Sair do programa")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1':
        ver_detalhes_do_filme()
    elif opcao == '2':
        fazer_comentario()
    elif opcao == '3':
        excluir_comentario()
    elif opcao == '4':
        print("Encerrando o programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

while True:
    print("Filmes em cartaz:\n")
    listar_filmes()
    menu()
