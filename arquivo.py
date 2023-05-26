# Importações feitas para auxiliar o processo do programa

import time # intervalo de tempo para o usuário processar as informações

# Funções


# Programa principal

# Mensagem de boas vindas
print("Seja bem-vindo(a)! Eu me chamo Alice, uma inteligência artificial produzida pela SFOME!")
print("Para prosseguirmos, será necessário a realização do seu cadastro! Vamos lá?!")
time.sleep(1)

while True: # Looping infinito para caso o usuário insira uma opção inválida, não fechar o programa!

    # Vendo se o usuário é do tipo produtor ou consumidor final
    print("Você é um produtor ou somente um consumidor final?")
    print("\n 1 - Produtor \n 2 - Consumidor final \n")
    try:
        tipoUsuario = int(input("Informe aqui a opção: "))
        if (tipoUsuario < 1) or (tipoUsuario > 2):
            raise TypeError
        
        elif tipoUsuario == 1:
            print("Implementação futura...")
            break

        elif tipoUsuario == 2:
            print("Implementação futura...")
            break

    except ValueError:
        print("Por favor, insira somente números! Tente novamente!")
        time.sleep(1)
    except TypeError:
        print("Por favor, insira uma opção válida disponível!")
        time.sleep(1)
