# Importações feitas para auxiliar o processo do programa

import time # intervalo de tempo para o usuário processar as informações

# Funções


# Programa principal

cadastro = 0 # Variável para ser utilizada como looping do cadastro (para não encerrar caso usuário digite algo errado)

# Mensagem de boas vindas
print("Seja bem-vindo(a)! Eu me chamo Alice, uma inteligência artificial produzida pela SFOME!")
print("Para prosseguirmos, será necessário a realização do seu cadastro! Vamos lá?!")
time.sleep(1)

while cadastro == 0:
    # Vendo se o usuário é do tipo produtor ou consumidor final
    print("Você é um produtor ou somente um consumidor final?")
    print("\n 1 - Produtor \n 2 - Consumidor final \n")
    try:
        tipoUsuario = int(input("Informe aqui a opção: "))
        if (tipoUsuario < 1) or (tipoUsuario > 2):
            raise TypeError
        
        elif tipoUsuario == 1:
            print("Implementação futura...")
            cadastro = 1

        elif tipoUsuario == 2:
            print("Implementação futura...")
            cadastro = 1

    except ValueError:
        print("Por favor, insira somente números! Tente novamente com uma opção válida!")
        time.sleep(1)
    except TypeError:
        print("Por favor, insira um número válido das opções disponíveis!")
        time.sleep(1)
