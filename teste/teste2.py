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
            instrucoes.append(instrucoes)

        receita = {
            'Título da receita': tituloReceita,
            'Ingredientes': ingredientes,
            'Instruções:': instrucoes
        }
        
        return receita
    
    except TypeError as msg:
        print(msg)


receita = sugestaoReceita()
print (receita)