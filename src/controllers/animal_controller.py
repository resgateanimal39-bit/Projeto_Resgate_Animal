from models.animal_model import *
from tinydb import Query
from models.pets_model import Pet
from models.tutores_model import Tutor
from models.usuarios_model import Usuario


# # Funções de cadastro
def adicionar_tutor():
    nome = input("Nome do tutor: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    status_aptidao = input("Status de aptidão: ")
    novo_id = len(tutores) + 1
    tutor = Tutor(novo_id, nome, telefone, email, endereco, status_aptidao)
    tutores.insert(tutor.to_dict())


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
        TutorQuery = Query()
        tutor_encontrado = tutores.search(TutorQuery.id == tutor_id)
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
    pet = Pet(
        novo_id, nome, especie, idade, local_resgate, status, tutor_id, tutor_nome
    )  # 👈 corrigido
    pets.insert(pet.to_dict())
    print(f"\nPet '{nome}' foi cadastrado com sucesso.\n")


def adicionar_usuario():
    nome = input("Nome do usuário: ")
    idade = int(input("Idade: "))
    novo_id = len(usuarios) + 1
    usuario = Usuario(novo_id, nome, idade)
    usuarios.insert(usuario.to_dict())


# # Funções de mostrar lista
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


# # Funções de doaçao e de devoluçao


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

    pets.update({"tutor_id": tutor_id, "tutor": tutor_nome}, Pet.id == pet_id)

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

    pets.update({"tutor_id": None, "tutor": "Sem tutor"}, Pet.id == pet_id)

    print(f"Pet '{pet[0]['nome']}' foi devolvido e agora está sem tutor.\n")


# # pesquisa


def pesquisar_por_especie():
    Pet = Query()
    especie = input("Digite a espécie (ex: gato, cachorro): ").lower()
    resultados = pets.search(Pet.especie == especie)

    if not resultados:
        print(f"\nNenhum pet da espécie '{especie}' encontrado.\n")
    else:
        print(f"\nPets da espécie '{especie}':")
        for p in resultados:
            print(
                f"ID: {p['id']} | Nome: {p['nome']} | Tutor: {p.get('tutor', 'Sem tutor')}"
            )
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
            print(
                f"ID: {t['id']} | Nome: {t['nome']} | Telefone: {t['telefone']} | Email: {t['email']}"
            )
    print()


# # Funções de resetar o banco
def limpar_banco():
    tutores.truncate()
    pets.truncate()
    usuarios.truncate()
    print("Banco limpo com sucesso.\n")
