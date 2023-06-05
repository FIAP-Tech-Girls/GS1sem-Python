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
                    print("Continua")

                # Caso sorvetes
                elif alimentoPerecivelCongelado == 2:
                    print("Continua")

                # Caso produtos prontos
                elif alimentoPerecivelCongelado == 3:
                    print("Continua")

        # Caso alimento não perecível (que não estraga fácil)
        elif alimento == 2:
            print("Continua")

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