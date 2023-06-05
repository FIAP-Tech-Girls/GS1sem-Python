import time

# Função para a parte de previsão de vida útil (simulação)
def previsaoVidaUtil():
    # Pegando a categoria de alimentos
    print("Qual a categoria de alimento que você deseja consultar hoje?")
    print("\n 1 - Alimentos perecíveis; \n 2 - Alimentos não perecíveis; \n 3 - Ajuda na categoria.")

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

previsaoVidaUtil()