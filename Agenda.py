def adicionar_contato(contatos, nome_contato, telefone, email):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favoritado": False, "ativo": True}
    contatos.append(contato)
    print(f"\n{nome_contato} foi adicionado na agenda!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "★" if contato["favoritado"] else " "
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"\n{indice}. [{favorito}] Nome: {nome_contato} - Telefone: {telefone} - Email: {email}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    nome_atual = contatos[indice_contato_ajustado]["nome"]
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if novo_nome_contato != "":
            contatos[indice_contato_ajustado]["nome"] = novo_nome_contato

        if novo_telefone != "":
            contatos[indice_contato_ajustado]["telefone"] = novo_telefone

        if novo_email != "":
            contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"\nContato {nome_atual} atualizado!")

    else:
        print("\nÍndice do contato inválido")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favoritado"] = True
    nome_atual = contatos[indice_contato_ajustado]["nome"]
    print(f"\n{nome_atual} favoritado na sua agenda!")
    return

def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if contatos[indice_contato_ajustado]["favoritado"]:
        contatos[indice_contato_ajustado]["favoritado"] = False
        nome_atual = contatos[indice_contato_ajustado]["nome"]
        print(f"\n{nome_atual} desmarcado como favoritado na sua agenda!")
    else:
        print("\nVocê escolheu um contato que não está nos favoritos")
        return
    
def ver_contatos_favoritados(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favoritado"]:
            favorito = "★"
            nome_contato = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"\n{indice}. [{favorito}] Nome: {nome_contato} - Telefone: {telefone} - Email: {email}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        nome_atual = contatos[indice_contato_ajustado]["nome"]
        del contatos[indice_contato_ajustado]
        print(f"\nContato {nome_atual} apagado da sua agenda!")
    else:
        print("\nÍndice do contato inválido")
    return

contatos = []

while True:
    print("\nVocê acessou sua agenda de contatos!\n")
    print("1. Adicione um contato")
    print("2. Visualizar minha lista de contatos")
    print("3. Editar um contato")
    print("4. Favoritar um contato")
    print("5. Tirar contato dos favoritos")
    print("6. Visualizar meus contatos favoritos")
    print("7. Apagar um contato")
    print("8. Sair da agenda")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(contatos, nome_contato, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o índice do contato: ")
        if int(indice_contato)>=0 and int(indice_contato)<=len(contatos):
            novo_nome = input("Digite o nome do contato caso queira alterar: ")
            novo_telefone = input("Digite o número do telefone caso queira alterar: ")
            novo_email = input("Digite o email do contato caso queira alterar: ")
            editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
        else:
            print("\nÍndice não encontrado ou inválido")

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o índice do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o índice do contato que deseja desfavoritar: ")
        desfavoritar_contato(contatos, indice_contato)

    elif escolha == "6":
        ver_contatos_favoritados(contatos)

    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = input("\nDigite o índice do contato que desejar apagar: ")
        apagar_contato(contatos, indice_contato)

    elif escolha == "8":
        break

print("\nVocê fechou a agenda!")