# Importações feitas para auxiliar o processo do programa

import time # intervalo de tempo para o usuário processar as informações
import getpass # apenas para simular a entrada de senha

# Criando dicionário para produtor que representa e um dicionário genérico para aqueles que não possuem empresa/consumidor final
produtorConsumidor = {}
produtorEmpresa = {}

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

def mostrarReceitaConfirmacao(receita):
    print(f"Título da receita: {receita['titulo']}")
    print("Ingredientes")
    for ingrediente in receita['ingredientes']:
        print(f"- {ingrediente}")
    print("Instruções: ")
    for i, instrucao in enumerate(receita['instrucoes'], start=1):
        print(f"{i}. {instrucao}")
     

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
            print("Implementação futura")
            time.sleep(1)

        # Opção de previsão de vida útil
        if opcao == 2:
            print("Implementação futura")
            time.sleep(1)

        # Opção de locais de doações próximos à você
        if opcao == 3:
            print("Implementação futura")
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
            print("Implementação futura")
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
            print("Implementação futura")
            time.sleep(1)

        # Opção de sugestão de melhorias
        if opcao == 4:
            sugestao = enviarMelhorias()
            time.sleep(1)
        
        # Encerrando a IA generativa
        if opcao == 5:
            print("Obrigada por utilizar a Alice! A SFOME agradece pela sua escolha e confiança!")
            break