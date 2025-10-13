from tinydb import TinyDB, Query

# ======== Banco de dados =====================================================================
db = TinyDB("src/data/db.json")
tutores = db.table("tutores")
pets = db.table("pets")
usuarios = db.table("usuarios")

# ======== Funções de listagem =================================================================
def listar_tutores():
    dados = tutores.all()
    if not dados:
        print("\nBanco de Tutores está vazio.")
    else:
        print("\nLista de Tutores cadastrados:")
        for t in dados:
            print(
                f"[ID: {t.get('id', '?')}  "
                f"Nome: {t.get('nome', '?')}  "
                f"Telefone: {t.get('telefone', '?')}  "
                f"Endereço: {t.get('endereco', 'Não informado')}  "
                f"Status: {t.get('status_aptidao', 'Não definido')}]"
            )
    print()


def listar_pets():
    dados = pets.all()
    if not dados:
        print("\nBanco de Pets está vazio.")
    else:
        print("\nLista de Pets cadastrados:")
        for y in dados:
            print(
                f"[ID: {y.get('id', '?')}  "
                f"Nome: {y.get('nome', '?')}  "
                f"Espécie: {y.get('especie', '?')}  "
                f"Idade estimada: {y.get('idade', '?')}  "
                f"Local do resgate: {y.get('local_resgate', 'Não informado')}  "
                f"Status: {y.get('status', 'Não definido')}  "
                f"ID do tutor: {y.get('tutor_id', 'Não informado')}  "
                f"Nome do tutor: {y.get('tutor', 'Não informado')}]"
            )
    print()


def listar_usuarios():
    dados = usuarios.all()
    if not dados:
        print("\nBanco de Usuários está vazio.")
    else:
        print("\nLista de Usuários cadastrados:")
        for u in dados:
            print(
                f"[ID: {u.get('id', '?')}  "
                f"Nome: {u.get('nome', '?')}  "
                f"Idade estimada: {u.get('idade', '?')}]"
            )
    print()


# ======== Funções de cadastro =======================================================================

def adicionar_tutor():
    nome = input("Nome do tutor: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    status_aptidao = input("Status de aptidão: ")
    novo_id = len(tutores) + 1
    tutores.insert({
        "id": novo_id,
        "nome": nome.lower(),
        "telefone": telefone,
        "email": email.lower(),
        "endereco": endereco.lower(),
        "status_aptidao": status_aptidao.lower()
    })
    print(f"\nTutor '{nome}' foi cadastrado com sucesso.\n")


def adicionar_pet():
    nome = input("Nome do pet: ")
    especie = input("Espécie (cão/gato/etc): ")
    idade = int(input("Idade: "))
    local_resgate = input("Local de resgate: ")
    status = input("Status (Em Avaliação Veterinária, Disponível, Adotado, etc): ")

    print("\nTutores disponíveis:")
    listar_tutores()
    tutor_id = input("Digite o ID do tutor (ou aperte Enter se não tiver): ")

    if tutor_id.strip():
        tutor_id = int(tutor_id)
        Tutor = Query()
        tutor_encontrado = tutores.search(Tutor.id == tutor_id)
        if tutor_encontrado:
            tutor_nome = tutor_encontrado[0]["nome"]
        else:
            print("Tutor não encontrado. O pet será cadastrado sem tutor.")
            tutor_id = None
            tutor_nome = "Sem tutor"
    else:
        tutor_id = None
        tutor_nome = "Sem tutor"

    novo_id = len(pets) + 1
    pets.insert({
        "id": novo_id,
        "nome": nome.lower(),
        "especie": especie.lower(),
        "idade": idade,
        "local_resgate": local_resgate.lower(),
        "status": status.lower(),
        "tutor_id": tutor_id,
        "tutor": tutor_nome
    })
    print(f"\nPet '{nome}' foi cadastrado com sucesso.\n")


def adicionar_usuario():
    nome = input("Nome do usuário: ")
    idade = int(input("Idade: "))

    novo_id = len(usuarios) + 1
    usuarios.insert({
        "id": novo_id,
        "nome": nome.lower(),
        "idade": idade
    })
    print(f"\nUsuário '{nome}' foi cadastrado com sucesso.\n")


# ======== Adoção e devolução =======================================================================================

def adotar_pet():
    Tutor = Query()
    Pet = Query()

    print("\nLista de Tutores cadastrados:")
    listar_tutores()
    tutor_id = input("Digite o ID do tutor que vai adotar: ")

    if not tutor_id.strip():
        print("Erro: é necessário informar o ID do tutor.\n")
        return

    tutor_id = int(tutor_id)
    tutor = tutores.search(Tutor.id == tutor_id)
    if not tutor:
        print("Tutor não encontrado.\n")
        return
    tutor_nome = tutor[0]["nome"]

    print("\nLista de Pets disponíveis:")
    pets_disponiveis = pets.search((Pet.tutor == "Sem tutor") | (Pet.tutor == None))

    if not pets_disponiveis:
        print("Nenhum pet disponível para adoção.\n")
        return

    for p in pets_disponiveis:
        print(
            f"[ID: {p.get('id', '?')}  "
            f"Nome: {p.get('nome', '?')}  "
            f"Espécie: {p.get('especie', '?')}  "
            f"Idade: {p.get('idade', '?')}  "
            f"Local do resgate: {p.get('local_resgate', 'Não informado')}  "
            f"Status: {p.get('status', 'Não definido')}]"
        )

    pet_id = input("\nDigite o ID do pet que será adotado: ")
    if not pet_id.strip():
        print("Erro: é necessário informar o ID do pet.\n")
        return

    pet_id = int(pet_id)
    pet = pets.search(Pet.id == pet_id)
    if not pet:
        print("Pet não encontrado.\n")
        return

    pets.update({
        "tutor_id": tutor_id,
        "tutor": tutor_nome
    }, Pet.id == pet_id)

    print(f"Pet '{pet[0]['nome']}' foi adotado por {tutor_nome}.\n")


def devolver_pet():
    Pet = Query()
    print("\nLista de Pets atualmente adotados:")
    pets_com_tutor = pets.search(Pet.tutor != "Sem tutor")
    if not pets_com_tutor:
        print("Nenhum pet com tutor no momento.\n")
        return

    for p in pets_com_tutor:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Tutor atual: {p['tutor']}")

    pet_id = input("\nDigite o ID do pet que será devolvido: ")
    if not pet_id.strip():
        print("É necessário informar o ID do pet.\n")
        return

    pet_id = int(pet_id)
    pet = pets.search(Pet.id == pet_id)
    if not pet:
        print("Pet não encontrado.\n")
        return

    pets.update({
        "tutor_id": None,
        "tutor": "Sem tutor"
    }, Pet.id == pet_id)

    print(f"Pet '{pet[0]['nome']}' foi devolvido e agora está sem tutor.\n")


# ======== Consultas =============================================================================

def pesquisar_por_especie():
    Pet = Query()
    especie = input("Digite a espécie (ex: gato, cachorro): ").lower()
    resultados = pets.search(Pet.especie == especie)

    if not resultados:
        print(f"\nNenhum pet da espécie '{especie}' encontrado.\n")
    else:
        print(f"\nPets da espécie '{especie}':")
        for p in resultados:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Tutor: {p.get('tutor', 'Sem tutor')}")
    print()


def consultar_tutor():
    Tutor = Query()
    print("\nConsulta de tutor:")
    escolha = input("Buscar por (1) ID ou (2) Nome? ")

    if escolha == "1":
        id_tutor = int(input("Digite o ID do tutor: "))
        resultado = tutores.search(Tutor.id == id_tutor)
    elif escolha == "2":
        nome_tutor = input("Digite o nome do tutor: ")
        resultado = tutores.search(Tutor.nome.matches(nome_tutor, flags=2))
    else:
        print("Opção inválida.")
        return

    if not resultado:
        print("\nTutor não encontrado.\n")
    else:
        print("\nTutor encontrado:")
        for t in resultado:
            print(f"ID: {t['id']} | Nome: {t['nome']} | Telefone: {t['telefone']} | Email: {t['email']}")
    print()


# ======== Resetar Banco =================================================================================
def limpar_banco():
    tutores.truncate()
    pets.truncate()
    usuarios.truncate()
    print("Banco limpo com sucesso.\n")


# ======== Menu principal ========================================================================================

def menu():
    while True:
        print("""
=========== MENU ===========
1. Adicionar Tutor
2. Adicionar Pet
3. Adicionar Usuário
4. Listar Tutores
5. Listar Pets
6. Listar Usuários
7. Tutor Adotar Pet
8. Devolver Pet
9. Pesquisar Pets por Espécie
10. Consultar Tutor
11. Limpar Banco
0. Sair
============================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tutor()
        elif opcao == "2":
            adicionar_pet()
        elif opcao == "3":
            adicionar_usuario()
        elif opcao == "4":
            listar_tutores()
        elif opcao == "5":
            listar_pets()
        elif opcao == "6":
            listar_usuarios()
        elif opcao == "7":
            adotar_pet()
        elif opcao == "8":
            devolver_pet()
        elif opcao == "9":
            pesquisar_por_especie()
        elif opcao == "10":
            consultar_tutor()
        elif opcao == "11":
            limpar_banco()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
