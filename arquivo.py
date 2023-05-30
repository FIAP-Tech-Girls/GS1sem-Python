# Importações feitas para auxiliar o processo do programa

import time # intervalo de tempo para o usuário processar as informações
import getpass # apenas para simular a entrada de senha

# Criando dicionário para produtor que representa ou não empresa
produtor = {}
produtorEmpresa = {}

# Criando dicionário para consumidor 
consumidor = {}

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

# Cadastrando um produtor que não representa uma empresa
def cadastraProdutor():
    print("Qual seu nome completo?")
    nome = input("")
    print("Qual seu CPF?")
    cpf = input("")
    print("Qual a sua data de nascimento?")
    dataNasc = input("")
    print("Qual seu e-mail?")
    email = input("")
    print("Qual o seu telefone para contato?")
    telRepresentante = input("")
    print("Digite sua senha")
    senha = getpass.getpass("Para sua segurança, a senha não mostrará valor enquanto digita. Ao finalizar, aperte enter que será cadastrada automaticamente!", stream=None)

    produtor[email] = {
        'Nome representante': nome,
        'CPF': cpf,
        'Data de nascimento': dataNasc,
        'Telefone do representante': telRepresentante,
        'Senha': senha
    }

    return nome # Apenas para conseguir conversar com o usuário

# Programa principal

# Mensagem de boas vindas
print("Seja bem-vindo(a)! Eu me chamo Alice, uma inteligência artificial produzida pela SFOME!")
print("Para prosseguirmos, será necessário a realização do seu cadastro! Vamos lá?!")
time.sleep(1)

while True: # Looping infinito de cadastro para caso o usuário insira uma opção inválida, não fechar o programa!

    # Vendo se o usuário é do tipo produtor ou consumidor final
    print("Você é um produtor ou somente um consumidor final?")
    print("\n 1 - Produtor \n 2 - Consumidor final \n")
    try:
        tipoUsuario = int(input("Informe aqui a opção: "))
        if (tipoUsuario < 1) or (tipoUsuario > 2):
            raise TypeError
        
        elif tipoUsuario == 1:
            print("Você irá representar uma empresa ou não?")
            print("\n 1 - Sim \n 2 - Não")
            try:
                representaEmpresa = int(input("Informe aqui a opção: "))
                if (representaEmpresa < 1) or (representaEmpresa > 2):
                    raise TypeError
                
                elif representaEmpresa == 1:
                    nome = cadastraProdutorEmpresa()
                    print(f"{nome}, seja bem-vindo(a) ao nosso sistema!")
                    print(f"Vamos lá!")
                    break
                elif representaEmpresa == 2:
                    nome = cadastraProdutor()
                    print(f"{nome}, seja bem-vindo(a) ao nosso sistema!")
                    print(f"Vamos lá!")
                    break
                
            except ValueError:
                print("Por favor, insira somente números! Tente novamente!")
                time.sleep(1)
            except TypeError:
                print("Por favor, insira uma opção válida disponível!")
                time.sleep(1)
            

        elif tipoUsuario == 2:
            print("Implementação futura...")
            break

    except ValueError:
        print("Por favor, insira somente números! Tente novamente!")
        time.sleep(1)
    except TypeError:
        print("Por favor, insira uma opção válida disponível!")
        time.sleep(1)


