# Sistema de Cadastro de Usuários

## Descrição

Este é um sistema simples de cadastro de usuários desenvolvido em Python. Ele permite cadastrar novos usuários, exibir a lista de usuários cadastrados e buscar um usuário específico pelo nome.

## Funcionalidades

- **Cadastrar Usuário**: Coleta o nome, idade e email do usuário e armazena as informações em uma lista.
- **Exibir Usuários**: Exibe a lista de todos os usuários cadastrados.
- **Buscar Usuário**: Busca um usuário específico pelo nome e exibe suas informações.
- **Fechar**: Encerra o programa.

## Estrutura do Projeto

O projeto consiste nos seguintes componentes principais:

- **Função `coletar_dados(nome, idade, email)`**: Coleta os dados do usuário e os adiciona à lista de usuários.
- **Função `exibir_usuarios(usuarios)`**: Exibe todos os usuários cadastrados.
- **Função `buscar_usuario(usuarios, nome_procurado)`**: Busca um usuário pelo nome e exibe suas informações.
- **Menu Interativo**: Permite ao usuário selecionar uma das funcionalidades do sistema.

## Como Executar

1. **Clone o Repositório**


   git clone https://github.com/Brunopln12/sistema-de-cadastro-de-usuarios.git
   cd sistema-de-cadastro-de-usuarios


2. **Execute o Script**


   python sistema_de_cadastro.py


## Exemplo de Uso
```
MENU

[c] Cadastrar usuário
[e] Exibir usuários
[b] Buscar usuário
[x] Fechar

=> c
Digite o nome do Usuário: João
Digite a idade do Usuário: 30
Digite o e-mail do Usuário: joao@example.com
Usuário cadastrado! :)

MENU

[c] Cadastrar usuário
[e] Exibir usuários
[b] Buscar usuário
[x] Fechar

=> e
Usuário:
  nome: João
  idade: 30
  email: joao@example.com

MENU

[c] Cadastrar usuário
[e] Exibir usuários
[b] Buscar usuário
[x] Fechar

=> b
Digite o nome do usuário que você está procurando: João
Usuário encontrado:
  nome: João
  idade: 30
  email: joao@example.com

MENU

[c] Cadastrar usuário
[e] Exibir usuários
[b] Buscar usuário
[x] Fechar

=> x
```

## Requisitos

- Python 3.x

## Estrutura de Arquivos

```
sistema-de-cadastro-de-usuarios/
│
├── sistema_de_cadastro.py
├── README.md
└── .gitignore
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.
