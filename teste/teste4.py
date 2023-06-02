# Criando receitas pré-definidas para mostrar
receitasDefinidas = {
    'sucoLimaoCasca': {
        'titulo': 'Suco de limão com casca',
        'descricao': 'Sabe quando você utiliza do limão e não sabe o que fazer com a casca e simplesmente joga fora? Sabia que ele pode virar um delicioso suco para um almoço, lanche da tarde ou janta? Não? Então vem aprender com a gente!',
        'ingredientes': ['1 limão;', '350 ml de água filtrada;', '10 cubos de gelo (opcional)', 
                         '1 colher de açúcar de sua preferência (opcional)'],
        'instrucoes': ['Lave bem o limão;', 'Tire as pontas do limão, corte-o ao meio e retire as partes brancas e as sementes;', 
                       'Leve ao liquidificador e bata com a água apenas no modo pulsante;', 'Coe e leve ao liquidificador novamente, com o gelo e o açúcar, e bata até ficar espumoso;',
                       'Sirva em seguida.'],
        'creditoAutor': 'Anny Dias.'
    },

    'petiscoBagacoMilho': {
        'titulo': 'Petisco de bagaço de milho verde',
        'descricao': 'Sabe quando você come o milho, ou faz algum suco ou bolo e sobra o bagaço? Você sabia que ele pode virar um delicioso aperitivo? Não? Então vem aprender com  gente!',
        'ingredientes': ['Esses ingredientes rendem 15 bolinhos!','1 xícara (de chá) de bagaço de milho verde;', '1 colher (de sopa) de farinha de trigo;',
                        '1 ovo;', '1 colher (de chá) de cebola ralada;', '1/2 colher (de café) de sal;',
                         '1 colher (de chá) de fermento em pó;', 'Óleo' ],
        'instrucoes': ['Em um recipiente misture o bagaço de milho, com a farinha de trigo, o ovo, a cebola ralada, o sal e o fermento, fazendo uma massa;',
                       'Coloque uns dois dedos de óleo em uma panela pequena;', 'Aqueça o óleo, mas não tão quente, para que o bolinho fique dourado por fora e cozinhe por dentro;',
                       'Com o auxílio de uma colher, faça bolinhos pequenos, para que fique mais gostoso e crocante. Pode se utilizar uma colher de sobremesa para facilitar!;',
                       'Assim que os bolinhas dourar, retire do óleo e coloque sobre papel absorvente para tirar o excesso de óleo;',
                       'Sirva quente.'],
        'creditoAutor': 'Camila Padalino.'
    },

    'sufleChocolate': {
        'titulo': 'Suflê de chocolate',
        'descricao': 'Sabe quando sobra aquele monte de chocolate da Páscoa e do Natal? E você comeu tanto que até enjoou e não sabe o que fazer? Transforme em suflê! Uma sobremesa maravilhosa, levinha e que vai deixar tudo mundo de boca aberta!',
        'ingredientes': ['Esses ingredientes rendem 7 porções!', '200g de açúcar de sua preferência;',
                         '4 ovos;', '200g de chocolate, amargo ou ao leite, você decide!;', '200g de manteiga.'],
        'instrucoes': ['Derreta o chocolate em banho-maria;', 'Derreta a manteiga;', 'Separe a gema da clara dos 4 ovos e reserve as gemas;',
                       'Bata as claras até que elas fiquem em ponto de neve, reserve;', 'Misture o açúcar e as gemas e bata até virar um creme;',
                       'Após isso, adicione delicadamente coloque as claras em neve no creme;', 'Adicione a manteiga e o chocolate no creme;',
                        'Misture;', 'Coloque no forno, que não pode estar preaquecido, por cerca de 10 a 15 minutos;',
                        'Tire do forno quando perceber que ele está levemente altinho;', 'Sirva'],
        'creditoAutor': 'Leticia Resina.'
    },
    
    'bolinhoArrozSobra': {
        'titulo': 'Bolinho de arroz com sobras do arroz',
        'descricao': 'Sobrou aquele monte de arroz no domingo? Enjoou do gosto e não sabe o que fazer? Que tal combinar a sobra de arroz e seus temperos favoritos e transformar em um delicioso aperitivo?',
        'ingredientes': ['Esses ingredientes rendem 6 porções. Para ter mais porções, basta multiplicar a quantidade!',
                         '2 xícaras de arroz (sobra);', '3/4 xíc. de farinha de trigo;', '1 xícara de água;',
                         'Temperos variados a gosto. Escolhe o que você mais gosta! Sugestões: cenoura, sal, cebolinha, orégano, pimenta, entre outros;',
                         'Óleo.'],
        'instrucoes': ['Misture tudo muito bem em uma vasilha;', 'Faça os bolinhos com o auxílio de duas colheres. De preferências, não tão grandes;',
                       'Frite até dourar;' 'Coloque um prato com papel para escorrer o óleo e sirva.'],
        'creditoAutor': 'Luana Cabezaolias.'
    }
}


# Função para mostrar o menu de receitas definidas dentro da variável receitasDefinidas
def menuReceitas(receitasDefinidas):
    print("Receitas disponíveis")
    print("Escolha o número em frente a receita para exibi-la")
    for i, receitaID in enumerate(receitasDefinidas, start=1):
        receita = receitasDefinidas[receitaID]
        print(f"{i}. {receita['titulo']}")
    print("----------------")

# Função para exibir a receita a partir da escolha do usuário
def exibirReceita(receita):
    print("-------------------")
    print(f"Título: {receita['titulo']}")
    print(f"{receita['descricao']}")
    print("Ingredientes:")
    for ingrediente in receita['ingredientes']:
        print(f"- {ingrediente}")
    print("Instruções:")
    for i, instrucao in enumerate(receita['instrucoes'], start=1):
        print(f"{i}. {instrucao}")
    print(f"Os créditos para essa receita vai para: {receita['creditoAutor']}")
    print("-------------------")

# Para facilitar o chamado de escolher a receita
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
        except ValueError as msg:
            print(msg)

escolherReceita(receitasDefinidas)

