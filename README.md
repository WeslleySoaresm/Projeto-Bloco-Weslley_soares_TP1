
# Sistema Integrado de Gestão (SIG) - Academia e Tarefas

*Um sistema de gestão de linha de comando, desenvolvido em Python, para praticar conceitos fundamentais de programação através da gestão de alunos e tarefas.*

-----

## 📜 Tabela de Conteúdos

1.  [Sobre o Projeto](Sobre-o-Projeto)
2.  [Funcionalidades](Funcionalidades)
3.  [Tecnologias Utilizadas](Tecnologias-Utilizadas)
4.  [Como Executar](Como-Executar)


-----

### 📖 Sobre o Projeto

O **Sistema Integrado de Gestão (SIG)** é uma aplicação de terminal desenvolvida como um projeto de estudo para solidificar conhecimentos em Python. O programa simula um sistema de gestão que opera em dois módulos independentes:

  * **Módulo de Gestão Acadêmica:** Focado no tema de uma escola de teologia, permite o cadastro e a gestão de alunos.
  * **Módulo de Gestão de Tarefas:** Um gestor de tarefas clássico para adicionar, visualizar e controlar afazeres.

O projeto foi estruturado de forma modular e utiliza as melhores práticas, incluindo funções bem definidas, documentação com DocStrings e uma interface de utilizador interativa.

-----

### ✨ Funcionalidades

O sistema está dividido em dois submenus principais:

#### Módulo de Gestão de Alunos

  * ✅ **Adicionar Novo Aluno:** Regista um novo aluno no sistema com ID, nome, email, status e data de inscrição.
  * ✅ **Listar Todos os Alunos:** Exibe uma tabela formatada com os detalhes de todos os alunos registados.
  * ✅ **Alterar Status de um Aluno:** Permite modificar o status de um aluno (ex: de "Ativo" para "Formado" ou "Inativo").

#### Módulo de Gestão de Tarefas

  * ✅ **Adicionar Tarefa:** Adiciona uma nova tarefa à lista.
  * ✅ **Listar Tarefas:** Exibe uma tabela com todas as tarefas, os seus status e data de criação.
  * ✅ **Marcar Tarefa como Concluída:** Altera o status de uma tarefa para "Concluída".
  * ✅ **Remover Tarefa:** Apaga uma tarefa da lista.

-----

### 🛠️ Tecnologias Utilizadas

  * **[Python 3](https://www.python.org/)**: Linguagem principal do projeto.
  * **[Tabulate](https://pypi.org/project/tabulate/)**: Biblioteca externa para a criação de tabelas de texto bem formatadas no terminal.

-----

### 🚀 Como Executar

Siga os passos abaixo para executar o projeto na sua máquina local.

#### 1\. Pré-requisitos

Certifique-se de que tem o **Python 3** instalado. Pode verificar a sua versão com o comando:

```bash
python3 --version
```

#### 2\. Clonar o Repositório (Exemplo)

Se este projeto estivesse no GitHub, você iria cloná-lo assim:

```bash
git clone https://github.com/seu-usuario/SIG-Python.git
cd SIG-Python
```

#### 3\. Instalar Dependências

Este projeto depende da biblioteca `tabulate`. Instale-a usando o `pip`:

```bash
pip3 install tabulate
```

  * **Boa prática (opcional):** Para projetos futuros, é recomendado criar um ficheiro `requirements.txt` com o conteúdo `tabulate` e instalar com `pip3 install -r requirements.txt`.

#### 4\. Executar o Programa

Navegue até à pasta do projeto no seu terminal e execute o ficheiro principal:

```bash
python3 nome_do_seu_ficheiro.py
```

*Substitua `nome_do_seu_ficheiro.py` pelo nome que deu ao seu script (ex: `sig_main.py` ou `weslley_soares_TP1.py`).*

-----

