feriados = [
    {"date":"2023-01-01","name":"Confraternização mundial","type":"national"},
    {"date":"2023-02-21","name":"Carnaval","type":"national"},
    {"date":"2023-04-07","name":"Sexta-feira Santa","type":"national"},
    {"date":"2023-04-09","name":"Páscoa","type":"national"},
    {"date":"2023-04-21","name":"Tiradentes","type":"national"},
    {"date":"2023-05-01","name":"Dia do trabalho","type":"national"},
    {"date":"2023-06-08","name":"Corpus Christi","type":"national"},
    {"date":"2023-09-07","name":"Independência do Brasil","type":"national"},
    {"date":"2023-10-12","name":"Nossa Senhora Aparecida","type":"national"},
    {"date":"2023-11-02","name":"Finados","type":"national"},
    {"date":"2023-11-15","name":"Proclamação da República","type":"national"},
    {"date":"2023-12-25","name":"Natal","type":"national"}
]

comentarios = {}

while True:
    print("Lista dos Feriados:")
    for i, feriado in enumerate(feriados):
        print(f"{i+1} - {feriado['date'][8:10]}/{feriado['date'][5:7]}/{feriado['date'][:4]} - {feriado['name']}")
    print("\nEscolha uma opção:\n")
    print("1 - Ver detalhes do feriado")
    print("2 - Fazer um comentário sobre o feriado")
    print("3 - Excluir um comentário\n")
    opcao = int(input())

    if opcao == 1:
        id_feriado = int(input("Digite o id do feriado: ")) - 1
        feriado = feriados[id_feriado]
        print(f"\nDetalhes do Feriado:")
        print(f"Data: {feriado['date'][8:10]}/{feriado['date'][5:7]}/{feriado['date'][:4]}")
        print(f"Nome: {feriado['name']}")
        print(f"Tipo: {feriado['type']}\n")
        if id_feriado in comentarios:
            print("Comentários:")
            for i, comentario in enumerate(comentarios[id_feriado]):
                print(f"{i+1} - {comentario['nome']}: {comentario['texto']}")
            print()
        else:
            print("Não há comentários sobre este feriado.\n")

    elif opcao == 2:
        id_feriado = int(input("Digite o id do feriado: ")) - 1
        nome = input("Digite o seu nome: ")
        texto = input("Digite o seu comentário: ")
        comentario = {"nome": nome, "texto": texto}
        if id_feriado in comentarios:
            comentarios[id_feriado].append(comentario)
        else:
            comentarios[id_feriado] = [comentario]
        print("Comentário adicionado com sucesso!\n")

    elif opcao == 3:
        id_feriado = int(input("Digite o id do feriado: ")) - 1
        if id_feriado in comentarios:
            print("Comentários:", comentarios)
           
