from controllers.animal_controller import*

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
