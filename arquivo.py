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

# Função para a parte de previsão de vida útil (simulação)
def previsaoVidaUtil():
    # Pegando a categoria de alimentos
    print("Qual a categoria de alimento que você deseja consultar hoje?")
    print("\n 1 - Alimentos perecíveis; \n 2 - Alimentos não perecíveis; \n 3 - Ajuda na categoria. \n")

    # Tratamento de erros
    try: 
        alimento = int(input("Informe a opção aqui: "))

        if (alimento < 1) or (alimento > 3): # Apenas opções válidas
            raise TypeError
        
        # Caso alimento perecível (que estraga fácil)
        elif alimento == 1:
            print("Esse alimento é resfriado ou congelado?")
            print("PS: O monitoramento de temperatura é essencial em todos os casos. Para te ajudar, procure conhecer sobre o Arduíno da SFOME!")
            print("\n 1 - Resfriado \n 2 - Congelado \n")

            tipoPerecivel = int(input("Informe a opção desejada aqui: "))
            if (tipoPerecivel < 1) or (tipoPerecivel > 2):
                raise TypeError
            
            # Quando resfriado
            elif tipoPerecivel == 1: 

                print("Alimentos perecíveis resfriados")
                print("Escolha uma das opções abaixo para prosseguir!")
                print("\n 1 - Ovo \n 2 - Leite \n 3 - Legumes \n") # Sujeito à mudanças no futuro

                alimentoPerecivelResfriado = int(input("Informe a opção desejada: "))
                if (alimentoPerecivelResfriado < 1) or (alimentoPerecivelResfriado > 3):
                    raise TypeError

                # Caso ovo
                elif alimentoPerecivelResfriado == 1:
                    print("No geral, os ovos podem ser mantidos refrigerados por um período prolongado de tempo antes de perderem sua qualidade e segurança alimentar.")
                    time.sleep(2)

                    print("Importante: Em condições ideais de armazenamento e transporte, os ovos resfriados podem permanecer seguros para consumo por várias semanas. No entanto, é importante observar que a qualidade dos ovos pode começar a deteriorar-se gradualmente com o tempo, mesmo quando refrigerados.")
                    time.sleep(2)

                    print("Temperatura ideal: 4°C (40°F) constantemente durante o transporte, que evita a proliferação de bactérias e preserva a qualidade do ovo!")
                    time.sleep(2)

                    print("É importante também verificar a legislação e as orientações específicas do seu país ou região em relação ao transporte e armazenamento de ovos resfriados. Além disso, é sempre recomendado verificar a data de validade ou a vida útil indicada na embalagem dos ovos, pois pode variar dependendo das regulamentações locais e das práticas de armazenamento.")
                    time.sleep(2)

                # Caso leite
                elif alimentoPerecivelResfriado == 2:
                    print("A vida útil do leite refrigerado durante o transporte também depende de vários fatores, incluindo a temperatura de armazenamento, a qualidade inicial do leite e as condições de transporte.")
                    time.sleep(2)

                    print("A temperatura ideal do leite fresco é de 0°C e 4°C (32°F - 39°F) para preservar sua qualidade e segurança alimentar.")
                    time.sleep(2)

                    print("Em muitos países, é comum que o leite fresco tenha uma vida útil de aproximadamente 7 a 10 dias quando mantido adequadamente refrigerado. No entanto, é importante verificar as regulamentações e as orientações específicas do seu país ou região, pois os períodos de validade podem variar.")
                    time.sleep(2)

                # Caso legumes
                elif alimentoPerecivelResfriado == 3:
                    print("A vida útil dos legumes durante o transporte pode variar de acordo com o tipo específico de legume, sua maturidade, condições de armazenamento e transporte, bem como o tempo e temperatura de exposição. Também pode ser influenciada por fatores como danos físicos, contaminação bacteriana e exposição a temperaturas inadequadas.")
                    time.sleep(2)

                    print("Alguns legumes têm uma vida útil mais curta do que outros. Por exemplo, folhas verdes, como alface e espinafre, geralmente têm uma vida útil mais curta, enquanto legumes mais robustos, como cenouras e batatas, tendem a ter uma vida útil mais longa.")
                    time.sleep(2)

                    print("Algumas dicas úteis para o transporte dos legumes:")
                    print("1. Legumes frescos geralmente devem ser mantidos em temperaturas frescas, entre 0°C e 10°C (32°F - 50°F), dependendo do tipo de legume. É importante evitar temperaturas muito baixas, pois isso pode causar danos ao produto.")
                    print("2. Evite danos físicos, manuseando com cuidado, pois lesões acabam acelerando o processo de estragar o legume;")
                    print("3. Evite umidades excessivas e formação de condensação! Pois muitos legumes são sensíveis a umidade.")
                    print("4. Coloque os legumes em embalagens apropriadas, que além de proteger de danos físicos, protege da exposição à bactérias")
                    print("5. Se possível, minimize o tempo de transporte e entregue o mais rápido possível!")
                    time.sleep(2)

            # Quando congelado
            elif tipoPerecivel == 2:
                print("Alimentos perecíveis congelados")
                print("Escolha uma das opções abaixo para prosseguir!")
                print("\n 1 - Carnes (bovina, suína ou frango) \n 2 - Sorvetes \n 3 - Produtos prontos congelados \n") # Sujeito à mudanças no futuro
                
                alimentoPerecivelCongelado = int(input("Informe a opção desejada: "))
                if (alimentoPerecivelCongelado < 1) or (alimentoPerecivelCongelado > 3):
                    raise TypeError
                
                # Caso carnes
                elif alimentoPerecivelCongelado == 1:
                    print("É fundamental que, no caso das carnes, sejam elas bovinas, suínas ou frangos, o transporte seja feito de forma apropriada para preservar a qualidade e a segurança do produto.")
                    time.sleep(2)

                    print("A temperatura ideal deve se manter abaixo de -18°C (-0.4°F) para evitar o crescimento de microorganismos e preservar sua qualidade.")
                    time.sleep(2)

                    print("A embalagem adequada é que seja a vácuo, projetadas especificamente para preservar a qualidade de produtos congelados.")
                    print("A embalagem adequada ajuda a evitar a formação de cristais de gelo e a proteger a carne de danos físicos!")
                    time.sleep(2)

                    print("O isolamento térmico é importante, garantindo que a carne congelada eja protegida do ambiente externo e de flutuações de temperatura. O uso de contêineres ou caixas isoladas termicamente pode ajudar a manter a temperatura estável e minimizar o risco de descongelamento parcial.")
                    time.sleep(2)

                    print("Em alguns casos, pode ser necessário utilizar serviços de transporte especializados em produtos congelados para garantir que a carne bovina congelada seja manuseada corretamente e que as condições de temperatura sejam adequadamente mantidas. É importante visualizar as diretrizes locais de onde sairá a carne e de entrega! :)")
                    time.sleep(2)

                # Caso sorvetes
                elif alimentoPerecivelCongelado == 2:
                    print("O transporte de sorvete requer cuidados especiais para garantir que o produto seja mantido em condições ideais, preservando sua textura, sabor e qualidade.")
                    time.sleep(2)

                    print("O sorvete deve ser mantido em temperaturas muito baixas, geralmente abaixo de -18°C (-0,4°F), para evitar a sua descongelação.")
                    time.sleep(2)

                    print("Evite agitações excessivas e movimentos bruscos durante o transporte, pois isso pode afetar a textura e a qualidade do sorvete. Certifique-se de que os pacotes de sorvete estejam devidamente acomodados e protegidos contra impactos.")
                    time.sleep(2)

                    print("Ao chegar ao destino, o sorvete deve ser imediatamente transferido para um freezer ou armazenamento refrigerado para manter sua qualidade. Evite descongelar e congelar repetidamente o sorvete, pois isso pode afetar negativamente sua textura e sabor.")
                    time.sleep(2)

                # Caso produtos prontos
                elif alimentoPerecivelCongelado == 3:
                    print("O transporte de produtos prontos, como pães e nuggets congelados, requer considerações específicas para manter sua qualidade e segurança.")
                    time.sleep(2)

                    print("Verifique as especificações do fabricante para determinar a temperatura de transporte recomendada. Geralmente, pães e nuggets congelados devem ser mantidos a temperaturas abaixo de -18°C (-0,4°F) para evitar a deterioração e o crescimento bacteriano.")
                    time.sleep(2)

                    print("Utilize embalagens isoladas termicamente, como caixas de isopor ou contêineres apropriados para produtos congelados. Isso ajuda a manter a temperatura baixa durante o transporte e reduz a exposição ao calor externo.")
                    time.sleep(2)

                    print("Evite descongelar parcialmente os produtos durante o transporte. Isso pode comprometer a qualidade e segurança dos alimentos. Certifique-se de que o veículo de transporte seja adequado e capaz de manter a temperatura constante durante todo o percurso.")
                    time.sleep(2)

        # Caso alimento não perecível (que não estraga fácil)
        elif alimento == 2:
                print("Alimentos não perecíveis")
                print("Escolha uma das opções abaixo para prosseguir!")
                print("\n 1 - Arroz \n 2 - Milho enlatado \n 3 - Leite em pó \n") # Sujeito à mudanças no futuro

                alimentoNaoPerecivel = int(input("Informe a opção desejada: "))
                if (alimentoNaoPerecivel < 1) or (alimentoNaoPerecivel > 3):
                    raise TypeError
                
                # Caso arroz
                elif alimentoNaoPerecivel == 1:
                    print("O arroz é um alimento não perecível amplamente consumido em todo o mundo.")
                    time.sleep(2)

                    print("O arroz pode ser armazenado e transportado em temperatura ambiente, entre 15°C e 25°C. Evite expor o arroz a temperaturas extremas, como calor excessivo ou frio intenso, pois isso pode afetar sua qualidade e textura.")
                    time.sleep(2)

                    print("O arroz deve ser mantido em um local seco, pois a umidade pode levar à formação de mofo e ao apodrecimento dos grãos.")
                    time.sleep(2)

                    print("A exposição à luz solar direta pode afetar a cor e o sabor do arroz ao longo do tempo. Portanto, é recomendável armazenar o arroz em um local escuro ou em recipientes opacos que bloqueiem a entrada de luz.")
                    time.sleep(2)

                    print("Para evitar a infestação de insetos ou roedores, é importante armazenar o arroz em um local limpo e protegido. Utilize recipientes herméticos ou sacos de armazenamento fechados para impedir a entrada de pragas.")
                    time.sleep(2)

                    print("O arroz tem a capacidade de absorver odores e sabores do ambiente ao seu redor. Portanto, é recomendável armazená-lo longe de produtos com odores fortes, como produtos químicos, detergentes ou alimentos com cheiros intensos.")
                    time.sleep(2)

                # Caso milho enlatado
                elif alimentoNaoPerecivel == 2:
                    print("O milho enlatado é um alimento não perecível que passa por um processo de conservação adequado para garantir sua durabilidade.")
                    time.sleep(2)

                    print("O milho em lata pode ser armazenado e transportado em temperatura ambiente, entre 15°C e 25°C. Evite expor as latas de milho a temperaturas extremas, como calor excessivo ou frio intenso, pois isso pode comprometer a qualidade e a segurança do produto.")
                    time.sleep(2)

                    print("Durante o transporte, é importante manipular as latas de milho com cuidado para evitar danos físicos. Evite quedas, impactos ou compressão excessiva que possam amassar ou danificar as embalagens.")
                    time.sleep(2)

                    print("É importante manter as latas de milho em um ambiente seco para evitar a formação de mofo ou corrosão nas embalagens. Evite locais úmidos ou com alta umidade relativa do ar durante o armazenamento e transporte.")
                    time.sleep(2)

                    print("O milho enlatado deve ser protegido da exposição direta à luz solar, pois a luz pode afetar a cor e a qualidade do produto ao longo do tempo. Armazene as latas de milho em locais escuros ou utilize embalagens opacas que bloqueiem a entrada de luz.")
                    time.sleep(2)

                    print("Ao armazenar milho enlatado, é recomendável seguir o princípio da primeiro a entrar, primeiro a sair (FIFO, do inglês first in, first out). Isso significa que você deve utilizar as latas de milho mais antigas antes das mais novas, garantindo assim que o estoque seja consumido dentro do prazo de validade.")
                    time.sleep(2)

                # Caso leite em pó
                elif alimentoNaoPerecivel == 3:
                    print("O leite em pó é um produto desidratado que tem uma vida útil prolongada e requer condições adequadas de armazenamento e transporte para manter sua qualidade.")
                    time.sleep(2)

                    print("O leite em pó deve ser armazenado e transportado em temperatura ambiente estável, entre 15°C e 25°C. Evite exposição a variações extremas de temperatura, como calor excessivo ou frio intenso, pois isso pode afetar a qualidade do produto. Manter uma temperatura constante é importante para evitar a absorção de umidade.")
                    time.sleep(2)

                    print("O leite em pó é altamente suscetível à absorção de umidade, o que pode resultar na formação de grumos e deterioração do produto. Portanto, é essencial armazená-lo em um local seco, longe de fontes de umidade, como pias, janelas ou áreas úmidas. Utilizar recipientes hermeticamente fechados também ajuda a proteger o leite em pó da umidade.")
                    time.sleep(2)

                    print("O leite em pó é sensível à luz, especialmente à luz solar direta, pois pode levar a alterações na cor e no sabor do produto. Portanto, é recomendável armazenar o leite em pó em um local escuro ou em recipientes opacos que bloqueiem a entrada de luz.")
                    time.sleep(2)

                    print("O leite em pó tem a capacidade de absorver odores e sabores do ambiente ao seu redor. Portanto, é importante armazená-lo longe de produtos com odores fortes, como produtos químicos, detergentes ou alimentos com cheiros intensos. Armazená-lo em um recipiente hermético também ajuda a evitar a contaminação cruzada de odores e sabores.")
                    time.sleep(2)

                    print(" Para evitar a infestação de insetos ou roedores, é importante armazenar o leite em pó em um local limpo e protegido. Utilize recipientes herméticos ou sacos de armazenamento fechados para impedir a entrada de pragas.")
                    time.sleep(2)

                    print("Durante o transporte, é importante manipular o leite em pó com cuidado para evitar danos físicos à embalagem e ao produto. Evite quedas, impactos e vibrações excessivas que possam resultar em amassamento ou ruptura da embalagem.")
                    time.sleep(2)

        # Caso o usuário precise de ajuda na categoria para escolher
        elif alimento == 3:
            print("Para te ajudar, iremos trazer a definição em texto de cada categoria dos alimentos!")
            time.sleep(1)

            print("Alimentos perecíveis, o que são?")
            print("- São produtos alimentícios, alimentos in natura, produtos semi preparados ou produtos preparados para o consumo que, pela sua natureza ou composição, necessitam de condições especiais de temperatura para a sua conservação. Encaixando alimentos como ovos, leite, frutos do mar, carnes, legumes, entre outros.")
            time.sleep(2)

            print("Alimentos não perecíveis, o que são?")
            print("- São aqueles que podem ser guardados por períodos longos e trazem menores dificuldades à conservação, porque podem ficar à temperatura ambiente. Consequentemente, são cargas mais simples de serem transportadas.")
            time.sleep(2)

    except TypeError:
        print("Por favor, informe somente opções válidas!")
        time.sleep(1)
    except ValueError:
        print("Por favor, informe somente o números dentro das opções disponíveis!")
        time.sleep(1)

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
            
            # Tratamento de erros caso o usuário digite informações inválidas
            try:
                a = float(input("Informe a variação quadrática da demanda, ou seja, a variação da demanda ao longo do tempo: "))
                b = float(input("Informe o termo linear da demanda, ou seja, a taxa de variação da demanda conforme o tempo: "))
                c = float(input("Informe o termo constante da demanda, ou seja, o valor inicial da demanda: "))
                tempo = int(input("Informe o tempo desejado, em semanas, da demanda futura: "))
                previsao = previsaoDemanda(a, b, c, tempo)
                print(f"A previsão de demanda no tempo de {tempo} semanas é de aproximadamente {previsao}")
                time.sleep(1)
            except ValueError:
                print("Por favor, informe somente números! E de preferência, não envie informações vazias! A SFOME agradece")
                time.sleep(1)
                
        # Opção de previsão de vida útil
        if opcao == 2:
            previsaoVidaUtil()
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
                print("Não foi enviada nenhuma receita. Voltando ao menu principal.")
                time.sleep(1)
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