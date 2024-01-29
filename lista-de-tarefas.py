lista_de_tarefas = ["Ler", "Escrever"]

def adicionar_tarefa():
    exibir_tarefa()
    nova_tarefa = input("Digite o nome da tarefa: ")
    lista_de_tarefas.append(nova_tarefa)
    print(f"Tarefa {nova_tarefa} adicionada à lista!")

def exibir_tarefa():
    print("\n")
    for i, tarefa in enumerate(lista_de_tarefas):
        print(f"{i}-{tarefa}")


def alterar_tarefa():
    exibir_tarefa()
    index_tarefa = int(input("Digite o indice da tarefa que deseja alterar: "))
    for i, tarefa in enumerate(lista_de_tarefas):
        if i == index_tarefa:
            lista_de_tarefas[i] = input("Digite o nome da nova tarefa: ")
        else:
            print(f"{tarefa} não foi encontrada.")



def remover_tarefa():
    exibir_tarefa()
    index_tarefa = input("Digite a indice da tarefa que deseja remover: ")

    for i, tarefa in enumerate(lista_de_tarefas):
        if i == index_tarefa:
            lista_de_tarefas.remove(tarefa)
            print(f"{tarefa} foi removida da lista.")
        else:
            print(f"{tarefa} não foi encontrada.")


while True:

    try:
        print("1-Adionar tarefa")
        print("2-Exibir tarefa")
        print("3-Remover tarefa")
        print("4-Alterar tarefa")
        print("5-Sair \n")

        opcao = int(input("Qual tarefa deseja executar ? "))

        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                exibir_tarefa()
            case 3:
                remover_tarefa()
            case 4:
                alterar_tarefa()
            case 5:
                break
            case _:
                print("Opção inválida \n")
    except(ValueError):
        print("Favor digitar um número válido: ")
                       