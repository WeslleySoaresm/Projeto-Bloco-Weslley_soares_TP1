# Importação de bibliotecas necessárias
# datetime para gerar a data de inscrição automaticamente
from datetime import datetime
# tabulate para exibir as listas de forma organizada
from tabulate import tabulate

# --- Base de Dados em Memória ---
# A lista principal que irá armazenar os dados dos alunos durante a execução.
# Cada aluno é um dicionário com os seus "metadados".
lista_de_alunos = []
# Variável para garantir que cada aluno tenha um ID único.
proximo_id_aluno = 1

# --- Funções do Sistema ---

def adicionar_aluno(lista, *, nome, email, curso="Teologia Geral"):
    """
    Adiciona um novo aluno ao sistema.

    Gera um ID único e a data de inscrição automaticamente. O status inicial
    é sempre "Ativo". Utiliza parâmetros por palavra-chave (keywords).

    Args:
        lista (list): A lista de alunos onde o novo aluno será adicionado.
        nome (str): O nome completo do aluno.
        email (str): O email de contacto do aluno.
        curso (str, optional): O curso em que o aluno está inscrito. 
                               O valor padrão é "Teologia Geral".
    
    Returns:
        None
    """
    global proximo_id_aluno
    
    novo_aluno = {
        "id": proximo_id_aluno,
        "nome": nome,
        "email": email,
        "curso": curso,
        "status": "Ativo",
        "data_inscricao": datetime.now().strftime("%d/%m/%Y")
    }
    
    lista.append(novo_aluno)
    proximo_id_aluno += 1
    print(f"\n Aluno '{nome}' adicionado com sucesso!")

def listar_alunos(lista):
    """
    Exibe todos os alunos cadastrados numa tabela formatada.

    Se a lista estiver vazia, exibe uma mensagem informativa.

    Args:
        lista (list): A lista de alunos a ser exibida.
    
    Returns:
        None
    """
    if not lista:
        print("\n Nenhum aluno cadastrado no sistema.")
        return

    cabecalho = ["ID", "Nome", "Email", "Curso", "Status", "Data de Inscrição"]
    dados_tabela = []
    
    for aluno in lista:
        dados_tabela.append([
            aluno["id"],
            aluno["nome"],
            aluno["email"],
            aluno["curso"],
            aluno["status"],
            aluno["data_inscricao"]
        ])
    
    print("\n--- LISTA DE ALUNOS ---")
    print(tabulate(dados_tabela, headers=cabecalho, tablefmt="fancy_grid"))

def alterar_status_aluno(lista, id_aluno, novo_status="Formado"):
    """
    Altera o status de um aluno específico (mapeado de "Marcar como Concluída").

    Procura um aluno pelo ID e atualiza o seu status.

    Args:
        lista (list): A lista de alunos.
        id_aluno (int): O ID do aluno a ser modificado.
        novo_status (str, optional): O novo status a ser atribuído.
                                     O valor padrão é "Formado".
    
    Returns:
        bool: True se o aluno foi encontrado e atualizado, False caso contrário.
    """
    for aluno in lista:
        if aluno["id"] == id_aluno:
            aluno["status"] = novo_status
            print(f"\n Status do aluno {id_aluno} alterado para '{novo_status}'.")
            return True
    
    print(f"\n Erro: Aluno com ID {id_aluno} não encontrado.")
    return False

def remover_aluno(lista, id_aluno):
    """
    Remove um aluno da lista.

    Args:
        lista (list): A lista de alunos.
        id_aluno (int): O ID do aluno a ser removido.
    
    Returns:
        bool: True se o aluno foi encontrado e removido, False caso contrário.
    """
    aluno_para_remover = None
    for aluno in lista:
        if aluno["id"] == id_aluno:
            aluno_para_remover = aluno
            break # Encontrámos o aluno, podemos parar o loop
            
    if aluno_para_remover:
        lista.remove(aluno_para_remover)
        print(f"\n Aluno com ID {id_aluno} removido com sucesso.")
        return True
    else:
        print(f"\n Erro: Aluno com ID {id_aluno} não encontrado.")
        return False

def mostrar_menu():
    """
    Apenas exibe o menu de opções para o utilizador.
    """
    print("\n--- Sistema de Gestão Acadêmica (Teologia) ---")
    print("1. Adicionar Novo Aluno")
    print("2. Listar Todos os Alunos")
    print("3. Alterar Status de um Aluno")
    print("4. Remover Aluno")
    print("5. Sair")
    print("---------------------------------------------")

# --- Loop Principal do Programa ---

# O bloco if __name__ == "__main__": é uma boa prática em Python para
# indicar o ponto de partida do programa.
if __name__ == "__main__":
    
    # O loop `while` garante que o menu seja exibido repetidamente.
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # Adicionar Aluno
            nome_aluno = input("Digite o nome do aluno: ")
            email_aluno = input("Digite o email do aluno: ")
            curso_aluno = input("Digite o curso (ex: Teologia Geral, Grego Bíblico): ")
            adicionar_aluno(lista_de_alunos, nome=nome_aluno, email=email_aluno, curso=curso_aluno)

        elif escolha == '2':
            # Listar Alunos
            listar_alunos(lista_de_alunos)

        elif escolha == '3':
            # Alterar Status
            listar_alunos(lista_de_alunos)
            try:
                id_para_alterar = int(input("Digite o ID do aluno para alterar o status: "))
                novo_status = input("Digite o novo status (ex: Formado, Inativo) ou pressione Enter para 'Formado': ")
                if novo_status:
                    alterar_status_aluno(lista_de_alunos, id_para_alterar, novo_status=novo_status)
                else:
                    alterar_status_aluno(lista_de_alunos, id_para_alterar)
            except ValueError:
                print("\n Erro: Por favor, digite um número de ID válido.")

        elif escolha == '4':
            # Remover Aluno
            listar_alunos(lista_de_alunos)
            try:
                id_para_remover = int(input("Digite o ID do aluno a ser removido: "))
                remover_aluno(lista_de_alunos, id_para_remover)
            except ValueError:
                print("\n Erro: Por favor, digite um número de ID válido.")

        elif escolha == '5':
            # Sair
            print("\n A encerrar o Sistema de Gestão Acadêmica. Até à próxima!")
            break

        else:
            # Opção Inválida
            print("\n Opção inválida! Por favor, escolha um número de 1 a 5.")