# Importações feitas para auxiliar o processo do programa

import time # intervalo de tempo para o usuário processar as informações
import getpass # apenas para simular a entrada de senha

# Criando dicionário para produtor que representa e um dicionário genérico para aqueles que não possuem empresa/consumidor final
produtorConsumidor = {}
produtorEmpresa = {}

# Criando receitas pré-definidas para mostrar dentro de um dicionário e vetores para ajudar
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

# Funções

# Cadastrando um produtor que representa uma empresa! -> código ficar mais clean no looping
def cadastraProdutorEmpresa():
    print("Certo, precisaremos de algumas informações pessoais sobre você!")
    print("Qual seu nome completo?")
    nome = input("")
    print("Qual seu CPF?")
    cpf = input("")
    print("Qual seu nome da empresa?")
    nomeEmpresa = input("")
    print("Qual CNPJ da empresa?")
    cnpj = input("")
    print("Qual a sua data de nascimento?")
    dataNasc = input("")
    print("Qual seu e-mail para contato?")
    email = input("")
    print("Qual o seu telefone para contato?")
    telRepresentante = input("")
    print("Qual o telefone da empresa para contato?")
    telEmpresa = input("")
    print("Digite sua senha")
    senha = getpass.getpass("Para sua segurança, a senha não mostrará valor enquanto digita. Ao finalizar, aperte enter que será cadastrada automaticamente!", stream=None)

    produtorEmpresa[email] = {
        'Nome representante': nome,
        'CPF': cpf,
        'Nome da empresa': nomeEmpresa,
        'CNPJ': cnpj,
        'Data de nascimento': dataNasc,
        'Telefone do representante': telRepresentante,
        'Telefone da empresa': telEmpresa,
        'Senha': senha
    }

    return nome # Apenas para conseguir conversar com o usuário

# Cadastrando um produtor e/ou consumidor final (Uma vez que, genericamente, são os mesmos dados que são solicitados)
def cadastraConsumidorProdutor():
    print("Qual seu nome completo?")
    nome = input("")
    print("Qual seu CPF?")
    cpf = input("")
    print("Qual a sua data de nascimento?")
    dataNasc = input("")
    print("Qual seu e-mail?")
    email = input("")
    print("Qual o seu telefone para contato?")
    telConsumidor = input("")
    print("Digite sua senha")
    senha = getpass.getpass("Para sua segurança, a senha não mostrará valor enquanto digita. Ao finalizar, aperte enter que será cadastrada automaticamente!", stream=None)

    produtorConsumidor[email] = {
        'Nome': nome,
        'CPF': cpf,
        'Data de nascimento': dataNasc,
        'Telefone': telConsumidor,
        'Senha': senha
    }

    return nome # Apenas para conseguir conversar com o usuário

# Menu de opções caso produtor
def menuProdutor():
    # Lista das opções disponíveis
    print("Digite 1: Realizar uma previsão de demanda;")
    print("Digite 2: Visualizar previsão de vida útil de algum alimento;")
    print("Digite 3: Visualizar os locais de doações mais próximos de você;")
    print("Digite 4: Sugerir de melhorias para a Alice;")
    print("Digite 5: Encerrar Alice.")

    # Validação do menu
    try:
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 5):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente o números dentro das opções disponíveis!")
        time.sleep(1)
    except TypeError:
        print("Opção inválida! Por favor, escolha uma opção válida disponível!")

# Menu de opções caso consumidor final
def menuConsumidor():
    # Lista das opções disponíveis
    print("Digite 1: Visualizar receitas criativas disponíveis;")
    print("Digite 2: Enviar sugestão de receitas;")
    print("Digite 3: Visualizar os locais de doações mais próximos de você;")
    print("Digite 4: Sugerir de melhorias para a Alice;")
    print("Digite 5: Encerrar Alice.")

    # Validação do menu
    try:
        opcao = int(input("Informe a opção desejada: "))
        if (opcao < 1) or (opcao > 5):
            raise TypeError
        return opcao
    except ValueError:
        print("Por favor, informe somente o números dentro das opções disponíveis!")
        time.sleep(1)
    except TypeError:
        print("Opção inválida! Por favor, escolha uma opção válida disponível!")
        time.sleep(1)

# Função para facilitar a entrada do usuário para enviar melhorias a Alice
def enviarMelhorias():
    try:
        print("Escreva embaixo sugestões para melhorias para a Alice!")
        sugestaoUsuario = input("")
        if sugestaoUsuario == "":
            raise TypeError
        print("Obrigada por enviar suas sugestões! Trabalhamos melhor quando trabalhamos em conjunto! A SFOME agradece!")
    except TypeError:
        print("Por favor, não envie sugestões vazias! A SFOME agradece.")


# Função para facilitar as sugestões de receita do usuário 
def sugestaoReceita():
    try:
        # Validação para o usuário não enviar informações vazias
        tituloReceita = input("Informe o título da receita: ")
        if tituloReceita == "":
            raise TypeError("O título da receita não pode ficar vazio! Por favor, tente novamente.")
        
        ingredientes = [] # guarda os ingredientes em uma lista para facilitar

        while True:
            ingrediente = input("Informe um ingrediente da receita por vez (para encerrar, digite 0): ")
            if ingrediente == "0":
                break
            elif ingrediente == "":
                raise TypeError("Não envie informações de ingrediente vazias! Por favor, tente novamente.")
            ingredientes.append(ingrediente)

        instrucoes = [] # guarda as instruções em uma lista para facilitar

        while True:
            instrucao = input("Informe uma instrução da receita por vez (para encerrar, digite 0): ")
            if instrucao == "0":
                break
            elif instrucao == "":
                raise TypeError("Não envie instruções vazias! Por favor, tente novamente.")
            instrucoes.append(instrucao)

        receita = {
            'titulo': tituloReceita,
            'ingredientes': ingredientes,
            'instrucoes': instrucoes
        }
        
        return receita
    
    except TypeError as msg:
        print(msg)
        return False

# Função de confirmar se o usuário deseja enviar a receita ou não
def mostrarReceitaConfirmacao(receita):
    print(f"Título da receita: {receita['titulo']}")
    print("Ingredientes")
    for ingrediente in receita['ingredientes']:
        print(f"- {ingrediente}")
    print("Instruções: ")
    for i, instrucao in enumerate(receita['instrucoes'], start=1):
        print(f"{i}. {instrucao}")
     
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
                raise ValueError
            receitaEscolhida = list(receitas.values())[opcao - 1] # converte a opção pra o index correto (pois em vetores, começa a contagem em 0!)
            exibirReceita(receitaEscolhida)
            time.sleep(1)
        except ValueError:
            print("Opção inválida. Digite somente números dentro das opções válidas.")
            time.sleep(1)

# Função para simular a ideia de locais de doações próximos 
def locaisDoacoes():
    try:
        cep = int(input("Informe o seu CEP (somente números): "))
        print(f"Os locais de doações próximos ao CEP {cep} são:")
        # Apenas para simular, nesse sentido. Poderá ser feito de maneira mais trabalhada com API e geolocalizações posteriormente!
        print("\n • ONG Banco de alimentos; \n • Lar das crianças \n • Anjos da noite \n • Conab \n") 
    except ValueError:
        print("Por favor, informe somente números e não envie informações vazias! A SFOME agradece!")

# Função de previsão de demanda conforme visto em Differentiated Problem Solving
def previsaoDemanda(a, b, c, tempo):
    previsao = a * tempo**2 + b * tempo + c
    return previsao

# Programa principal

# Mensagem de boas vindas
print("Seja bem-vindo(a)! Eu me chamo Alice, uma inteligência artificial produzida pela SFOME!")
print("Para prosseguirmos, será necessário a realização do seu cadastro! Vamos lá?!")
time.sleep(1)

cadastro = 0 # para facilitar o looping
while cadastro == 0: # Looping para caso o usuário insira uma opção inválida no cadastro, não fechar!

    # Vendo se o usuário é do tipo produtor ou consumidor final
    print("Você é um produtor ou somente um consumidor final?")
    print("\n 1 - Produtor \n 2 - Consumidor final \n")
    try:
        tipoUsuario = int(input("Informe aqui a opção: "))
        if (tipoUsuario < 1) or (tipoUsuario > 2):
            raise TypeError
        
        elif tipoUsuario == 1:
            print("Você irá representar uma empresa ou não?")
            print("\n 1 - Sim \n 2 - Não \n")
            try:
                representaEmpresa = int(input("Informe aqui a opção: "))
                if (representaEmpresa < 1) or (representaEmpresa > 2):
                    raise TypeError
                
                elif representaEmpresa == 1:
                    nome = cadastraProdutorEmpresa()
                    print(f"{nome}, seja bem-vindo(a) ao nosso sistema!")
                    print(f"Vamos lá!")
                    time.sleep(1)
                    cadastro = 1
                elif representaEmpresa == 2:
                    nome = cadastraConsumidorProdutor()
                    print(f"{nome}, seja bem-vindo(a) ao nosso sistema!")
                    print(f"Vamos lá!")
                    time.sleep(1)
                    cadastro = 1
                
            except ValueError:
                print("Por favor, insira somente números! Tente novamente!")
                time.sleep(1)
            except TypeError:
                print("Por favor, insira uma opção válida disponível!")
                time.sleep(1)
            

        elif tipoUsuario == 2:
            nome = cadastraConsumidorProdutor()
            print(f"{nome}, seja bem-vindo(a) ao nosso sistema!")
            print(f"Vamos lá!")
            time.sleep(1)
            cadastro = 1

    except ValueError:
        print("Por favor, insira somente números! Tente novamente!")
        time.sleep(1)
    except TypeError:
        print("Por favor, insira uma opção válida disponível!")
        time.sleep(1)

# Depois de ter feito o cadastro, inicia a execução do programa principal em um outro looping para não voltar TUDO quando opção inválida no menu
while True:
    # Quando o usuário é produtor
    if tipoUsuario == 1:
        print(f"{nome}, veja as opções disponíveis para navegar pela Alice!")
        opcao = menuProdutor()

        # Opção de previsão de demanda
        if opcao == 1:
            # Comentário inicial falando sobre a previsão de demanda e importância
            print("Você sabia que a previsão de demanda é um processo analítico que visa estimar a quantidade" 
                " de produtos ou serviços que serão procurados pelos consumidores em um determinado período"
                " de tempo?")
            print("É essencial para você, produtor, que deseja planejar suas operações, desde a produção até"
                " a gestão de estoque e distribuição, evitando o desperdício de alimentos, e"
                " consequentemente, diminuindo os gastos e aumentando seu lucro, além de atender às" 
                "expectativas dos clientes.")
            time.sleep(1)
            print("")
            
            a = float(input("Informe a variação quadrática da demanda, ou seja, a variação da demanda ao longo do tempo: "))
            b = float(input("Informe o termo linear da demanda, ou seja, a taxa de variação da demanda conforme o tempo: "))
            c = float(input("Informe o termo constante da demanda, ou seja, o valor inicial da demanda: "))
            tempo = int(input("Informe o tempo desejado, em semanas, da demanda futura: "))
            previsao = previsaoDemanda(a, b, c, tempo)
            print(f"A previsão de demanda no tempo de {tempo} semanas é de aproximadamente {previsao}")
            time.sleep(1)

        # Opção de previsão de vida útil
        if opcao == 2:
            print("Implementação futura")
            time.sleep(1)

        # Opção de locais de doações próximos à você
        if opcao == 3:
            locaisDoacoes()
            time.sleep(1)

        # Opção de sugestões de melhorias
        if opcao == 4:
            sugestao = enviarMelhorias()
            time.sleep(1)

        # Encerrando a IA generativa
        if opcao == 5:
            print("Obrigada por utilizar a Alice! A SFOME agradece pela sua escolha e confiança!")
            break

    # Quando o usuário é consumidor final
    elif tipoUsuario == 2:

        print(f"{nome}, veja as opções disponíveis para navegar pela Alice!")
        opcao = menuConsumidor()

        # Opção de visualizar receitas disponíveis
        if opcao == 1:
            print("Você sabia que há diferentes formas de aproveitar os alimentos, ao invés de descarta-los?")
            print("Veja abaixo algumas opções de receitas e escolha qual desejar para ver com mais detalhes!")
            escolherReceita(receitasDefinidas)
            time.sleep(1)

        # Opção de sugestão de receitas
        if opcao == 2:
            receita = sugestaoReceita()
            if receita == False:
                print("")
            else:
                mostrarReceitaConfirmacao(receita)
                print("Deseja confirmar a receita? \n 1 - Para sim \n 2 - Para não")
                try:
                    confirma = int(input(""))
                    if (confirma < 1) or (confirma > 2):
                        raise TypeError
                    elif confirma == 1:
                        print("Obrigada por enviar a sua sugestão de receita!")
                        print("A equipe da SFOME irá revisar e em breve, sua receita aparecerá em receitas criativas!")
                        time.sleep(1)
                    elif confirma == 2:
                        print("Obrigada, de qualquer forma! A SFOME agradece!")
                        time.sleep(1)
                except ValueError:
                    print("Por favor, insira somente números! Tente novamente!")
                    time.sleep(1)
                except TypeError:
                    print("Por favor, insira uma opção válida disponível!")
                    time.sleep(1)
                    
            time.sleep(1)

        # Opção de locais de doações próximos à você
        if opcao == 3:
            locaisDoacoes()
            time.sleep(1)

        # Opção de sugestão de melhorias
        if opcao == 4:
            sugestao = enviarMelhorias()
            time.sleep(1)
        
        # Encerrando a IA generativa
        if opcao == 5:
            print("Obrigada por utilizar a Alice! A SFOME agradece pela sua escolha e confiança!")
            break