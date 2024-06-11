usuarios = []

def coletar_dados(nome, idade, email):
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
    }
    usuarios.append(usuario)
    return "Usuário cadastrado! :)"


def exibir_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for usuario in usuarios:
        print("Usuário:")
        for chave, valor in usuario.items():
            print(f"  {chave}: {valor}")
        print("\n")


def buscar_usuario(usuarios, nome_procurado):
    for usuario in usuarios:
        if usuario['nome'] == nome_procurado:
            print("Usuário encontrado:")
            for chave, valor in usuario.items():
                print(f"  {chave}: {valor}")
            return
    print("Usuário não cadastrado.")

while True:
    menu = """
    MENU
    
    [c] Cadastrar usuário
    [e] Exibir usuários
    [b] Buscar usuário
    [x] Fechar

    => """
    
    selecao = input(menu).lower()

    if selecao == 'c':
        nome = input("Digite o nome do Usuário: ")
        idade = int(input("Digite a idade do Usuário: "))
        email = input("Digite o e-mail do Usuário: ")
        print(coletar_dados(nome, idade, email))
    
    elif selecao == 'e':
        exibir_usuarios(usuarios)
    
    elif selecao == 'b':
        nome = input("Digite o nome do usuário que você está procurando: ")
        buscar_usuario(usuarios, nome)

    elif selecao == 'x':
        break

    else:
        print("Opção inválida!!!")