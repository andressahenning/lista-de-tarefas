lista_de_tarefas = []

def adicionar_tarefa():
    nova_tarefa = input("Digite o nome da tarefa: ")
    lista_de_tarefas.append(nova_tarefa)
    print(f"Tarefa {nova_tarefa} adicionada à lista!")

def exibir_tarefa():
    print(lista_de_tarefas)

def alterar_tarefa():
    tarefa = input("Digite a tarefa que deseja alterar: ")
    lista_de_tarefas.

def remover_tarefa():
    tarefa = input("Digite a tarefa que deseja remover: ")
    if tarefa in lista_de_tarefas:
        lista_de_tarefas.remove(tarefa)
        print(f"{tarefa} foi removida da lista.")
    else:
        print(f"{tarefa} não foi encontrada.")


while True:   
