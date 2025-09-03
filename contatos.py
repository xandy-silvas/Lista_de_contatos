def Adicionar_Contato(Contatos, nome_contato, numero_contato, email_contato):
    contato = {"nome": nome_contato, "numero": numero_contato, "email": email_contato, "favorita": False}
    Contatos.append(contato)
    print(f"*****O contato {nome_contato} salvo com sucesso")
    return


def Lista_contato(Contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(Contatos, start=1):
        fav = '☆' if contato['favorita'] else ""
        nome_contato = contato["nome"]
        numero_contato = contato["numero"]
        print(f"{indice} - ({fav}) {nome_contato}, Numero: {numero_contato}")
    return

def Editar_contatoNome(Contatos, IndiceContato, novoNome):
    IndiceContatoNew = int(IndiceContato) - 1
    if IndiceContatoNew >= 0 and IndiceContatoNew < len(Contatos):
        Contatos[IndiceContatoNew] ["nome"] = novoNome 
        print(f"\n Contato de {nome_contato} atualizado para {novoNome}")
    else:
        print("Indice Invalido")

def Editar_contatoNumero(Contatos, IndiceContato, novoNumero):
    IndiceContatoNew = int(IndiceContato) - 1
    if IndiceContatoNew >= 0 and IndiceContatoNew < len(Contatos):
        Contatos[IndiceContatoNew] ["numero"] = novoNumero 
        print(f"\nO numero de {nome_contato} foi atualizado para {novoNumero}")
    else:
        print("Indice Invalido")

def Editar_contatoEmail(Contatos, IndiceContato, novoEmail):
    IndiceContatoNew = int(IndiceContato) - 1
    if IndiceContatoNew >= 0 and IndiceContatoNew < len(Contatos):
        Contatos[IndiceContatoNew] ["email"] = novoEmail 
        print(f"\n O email de {nome_contato} atualizado para {novoEmail}")
    else:
        print("Indice Invalido")

def Favoritar_contato(Contatos, IndiceContato):
    IndiceContatoNew = int(IndiceContato) - 1
    if IndiceContatoNew >= 0 and IndiceContatoNew < len(Contatos):
        Contatos[IndiceContatoNew] ["favorita"] = True 
        print(f"Contato favoritado com sucesso")
    else:
        print("Indice de contato invalido")
    return

def Remove_Favoritar_contato(Contatos, IndiceContato):
    IndiceContatoNew = int(IndiceContato) - 1
    if IndiceContatoNew >= 0 and IndiceContatoNew < len(Contatos):
        Contatos[IndiceContatoNew] ["favorita"] = False 
        print(f"Contato de {nome_contato} favoritado com sucesso")
    else:
        print("Indice de contato invalido")
    return

def Lista_contatoFAV(Contatos):
    for contato in Contatos:
        if contato['favorita'] == True:
            fav = '☆' if contato['favorita'] else ""
            nome_contato = contato["nome"]
            numero_contato = contato["numero"]
            print(f"({fav}) {nome_contato}, Numero: {numero_contato}")
    return

def deleta_contato(Contatos):
    IndiceContatoNew = int(IndiceContato) - 1
    if IndiceContatoNew >= 0 and IndiceContatoNew < len(Contatos):
        for contato in Contatos:
            Contatos.remove(contato)
            print("contato apagado com sucesso")
    return

Contatos = []

while True:
    print  ("\nSeja Bem-Vindo")
    print  ("1- Adicionar Contato")
    print  ("2- Ver Contatos Salvos")
    print  ("3- Editar Contato")
    print  ("4- Marcar Contato Como Favorito")
    print  ("5- Desmarcar Contato Como Favorito")
    print  ("6- Ver Favoritos")
    print  ("7- Deletar contato")
    print  ("8- Sair do APP")


    Escolha = input("\nSelecione a Opção desejada: ")

    if Escolha == "1":
        nome_contato = input("Digite o nome do contato que deja adicionar: ")
        numero_contato = input("Digite o Numero: ")
        email_contato = input("Digite o Email: ")
        Adicionar_Contato(Contatos, nome_contato, numero_contato, email_contato)
    
    elif Escolha == "2":
        Lista_contato(Contatos)
    
    elif Escolha == "3":
        print("\nOque gostaria de editar? ")
        print("1 - Nome")
        print("2 - Numero")
        print("3 - Email")
        Opcao_Mudar = input("\nEscolha a opção que deseja: ")

        if Opcao_Mudar == "1":
            Lista_contato(Contatos)
            IndiceContato = input("Digite o indice do contato que quer editar ")
            novoNome = input("Digite o novo nome: ")
            Editar_contatoNome(Contatos, IndiceContato, novoNome)

        elif Opcao_Mudar == "2":
            Lista_contato(Contatos)
            IndiceContato = input("Digite o indice do contato que quer editar: ")
            novoNumero = input("Digite o novo numero: ")
            Editar_contatoNumero(Contatos, IndiceContato, novoNumero)

        elif Opcao_Mudar == "3":
            Lista_contato(Contatos)
            IndiceContato = input("Digite o indice do contato que quer editar ")
            novoEmail = input("Digite o novo email  : ")
            Editar_contatoEmail(Contatos, IndiceContato, novoEmail)
        
        else: print("Indice Invalido")
    
    elif Escolha == "4":
        Lista_contato(Contatos)
        IndiceContato= input("Digite o ID do contato que deseja favoritar: ")
        Favoritar_contato(Contatos, IndiceContato)
    
    elif Escolha == "5":
        Lista_contatoFAV(Contatos)
        IndiceContato= input("Digite o ID do contato que deseja favoritar: ")
        Remove_Favoritar_contato(Contatos, IndiceContato)
    
    elif Escolha == "6":
        Lista_contatoFAV(Contatos)
        print("Contatos salvos como favoritos: ")
    
    elif Escolha == "7":
        Lista_contato(Contatos)
        IndiceContato= input("Digite o ID do contato que deseja favoritar: ")
        deleta_contato(Contatos)
    
    elif Escolha == "8":
        print("Obrigado por utilizar")
        break

    else: 
        print("\n***Opção Invalida***")