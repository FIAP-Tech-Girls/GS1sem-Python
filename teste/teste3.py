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

receita = sugestaoReceita()
if receita == False:
    print("")
else:
    mostrarReceitaConfirmacao(receita)