from validacoes import ler_arquivo
from tabulate import tabulate


def linha():
    print('-' * 60)


def linha_tabela():
    print('-' * 93)


def menu_trainee(msg):
    titulo = 'Cadastro de Candidatos Trainee XPTO'
    linha()
    print(titulo.center(60))
    linha()
    print('1 - listar vaga')
    print('2 - Cadastrar Candidatos')
    print('3 - Salvar')
    print('9 - Sair')
    linha()


def menu_vagas(vagas):

    linha()
    print('Lista de Vagas')
    linha()
    print(f'Codigo - Vaga')
    for v in vagas:
        print(f'{v.id} - {v.nome}')


def tabela_grid(arq):
    titulo = 'Tabela de Candidatos'
    linha_tabela()
    print(titulo.center(93))
    linha_tabela()

    new_dado = []
    file = ler_arquivo(arq)
    for l in file:
        new_dado.append(l.split(';'))

    x = tabulate(new_dado, headers=['Nome', 'Sobrenome', 'CPF', 'Data de Nascimento', 'Maior de Idade?', 'Vaga'],tablefmt="grid")
    return x




###### testando as funcoes
# menu_trainee()
# menu_vagas(vagas)
