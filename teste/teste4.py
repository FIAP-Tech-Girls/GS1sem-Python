# Criando receitas pré-definidas para mostrar

receitasDefinidas = {
    'sucoLimaoCasca': {
        'titulo': 'Suco de limão com casca',
        'ingredientes': ['1 limão;', '350 ml de água filtrada;', '10 cubos de gelo (opcional)', 
                         '1 colher de açúcar de sua preferência (opcional)'],
        'instrucoes': ['Lave bem o limão;', 'Tire as pontas do limão, corte-o ao meio e retire as partes brancas e as sementes;', 
                       'Leve ao liquidificador e bata com a água apenas no modo pulsante;', 'Coe e leve ao liquidificador novamente, com o gelo e o açúcar, e bata até ficar espumoso;',
                       'Sirva em seguida.'],
        'creditoAutor': 'Anny Dias.'
    },

    'petiscoBagacoMilho': {
        'titulo': 'Petisco de bagaço de milho verde',
        'ingredientes': ['1 xícara (de chá) de bagaço de milho verde;', '1 colher (de sopa) de farinha de trigo;',
                        '1 ovo;', '1 colher (de chá) de cebola ralada;', '1/2 colher (de café) de sal;',
                         '1 colher (de chá) de fermento em pó;', 'Óleo' ],
        'instrucoes': ['Em um recipiente misture o bagaço de milho, com a farinha de trigo, o ovo, a cebola ralada, o sal e o fermento, fazendo uma massa;',
                       'Coloque uns dois dedos de óleo em uma panela pequena;', 'Aqueça o óleo, mas não tão quente, para que o bolinho fique dourado por fora e cozinhe por dentro;',
                       'Com o auxílio de uma colher, faça bolinhos pequenos, para que fique mais gostoso e crocante. Pode se utilizar uma colher de sobremesa para facilitar!;',
                       'Assim que os bolinhas dourar, retire do óleo e coloque sobre papel absorvente para tirar o excesso de óleo;',
                       'Sirva quente.'],
        'creditoAutor': 'Camila Padalino.'
    }
}

def menuReceitas(receitasDefinidas):
    print("Receitas disponíveis")
    print("Escolha o número em frente a receita para exibi-la")
    for i, receitaID in enumerate(receitasDefinidas, start=1):
        receita = receitasDefinidas[receitaID]
        print(f"{i}. {receita['titulo']}")
    print("----------------")

def exibirReceita(receita):
    print("-------------------")
    print(f"Título: {receita['titulo']}")
    print("Ingredientes:")
    for ingrediente in receita['ingredientes']:
        print(f"- {ingrediente}")
    print("Instruções:")
    for i, instrucao in enumerate(receita['instrucoes'], start=1):
        print(f"{i}. {instrucao}")
    print(f"Os créditos para essa receita vai para: {receita['creditoAutor']}")
    print("-------------------")

def escolherReceita(receitas):
    while True:
        menuReceitas(receitas)

        opcao = input("Digite a opção escolhida aqui (para voltar ao menu principal, digite 0): ")

        if opcao == "0":
            break

        try:
            opcao = int(opcao)
            if opcao < 1 or opcao > len(receitas):
                raise ValueError("Opção inválida. Digite um número válido.")

            receita_escolhida = list(receitas.values())[opcao - 1]
            exibirReceita(receita_escolhida)
        except ValueError as e:
            print(e)

escolherReceita(receitasDefinidas)

