import re
from datetime import date, datetime


def valida_nome():
    while True:
        try:
            nome = str(input('Nome: '))
            if nome == '':
                print('Digite um Nome por favor!')
                continue
            elif nome.isdecimal():
                print('Números não são válidos como NOME!')
                continue
            elif nome.isspace():
                print('Espaços não são válidos como NOME!')
                continue
            else:
                nome_formatado = (re.sub(r'[^A-z]+', '', nome)).title()
                return nome_formatado
            # punctuation

        except TypeError or ValueError:
            print('Digite um NOME válido!')


def valida_sobrenome():
    while True:
        try:
            sobrenome = str(input('Sobrenome: '))
            if sobrenome == '':
                print('Digite um Nome por favor!')
                continue
            elif sobrenome.isdecimal():
                print('Números não são válidos como SOBRENOME!')
                continue
            elif sobrenome.isspace():
                print('Espaços não são válidos como SOBRENOME!')
                continue
            else:
                sobrenome_formatado = (
                    re.sub(r'[^A-z]+', '', sobrenome)).title()
                return sobrenome_formatado
        except TypeError or ValueError:
            print('Digite um SOBRENOME válido!')


def valida_formato(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def calcula_idade(data):
    try:
        if valida_formato(data) is True:
            born = datetime.strptime(data, "%d/%m/%Y").date()

            # Get today's date
            today = date.today()

            calculo = today.year - born.year - \
                ((today.month, today.day) < (born.month, born.day))
            if calculo >= 18:
                return 'Maior de Idade'
            else:
                return 'Menor de Idade'
        else:
            print('Data Fonercida é inválida! Tente: dd/mm/aaaa')
    except TypeError:
        print('Digite uma Data de Nascimento válida!')


# Validacoes_Arquivos
arq = 'bancodedados.txt'


def arquivo_final(arq):
    if not arquivo_existe(arq):
        criar_arquivo(arq)


def arquivo_existe(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arq):
    try:
        file = open(arq, 'wt+')
        print('Arquivo criado ')
        file.close()
    except:
        print('Houve um ERRO na criação do arquivo')


def cadastrar_arquivo(arq, nome, sobrenome, cpf, data, vaga):

    try:
        file = open(arq, 'a+')
    except:
        print('ERRO na abertura do arquivo! CADASTRARARQUIVO')
    else:
        try:
            vidade = calcula_idade(data)
            file.write(
                f'{nome};{sobrenome}; {cpf}; {data}; {vidade}; {vaga}\n')
        except:
            print('ERRO ao escrever os dados! CADASTRARARQUIVO')
        else:
            print(f'Novo Registro de Candidato adicionado! CADASTRARARQUIVO')
            file.close()


def ler_arquivo(arq):
    try:
        file = open(arq, 'rt')
    except:
        print('ERRO ao ler o arquivo! LER ARQUIVO')
    else:
        return file.readlines()


def valida_qtde_vagas(vagas, vaga, candidato):
    # checar se a vaga ainda recebe candidatos
    isValidID = False
    for v in vagas:  # para cada indice / vaga na minha lista de vagas
        if v.id == vaga:  # se minha vaga.id for igual == minha vaga
            if v.validar_vagas() == False:  # se minha validacao for false, adiciono o candidato
                v.candidatos.append(candidato)
            else:
                return 'ERRO! Quantidade de candidatos limite!'
            isValidID = True
            break

    if isValidID == False:
        print('Vaga Inexistente')


def duplicidade_cpf(cpf):
    try:
        file = open(arq, 'rt')
        dado = file.readlines()
        for l in dado:
            x = l.split(';')
            for i in x:
                if (cpf in i):
                    return True
    except:
        return False


def leia_inteiro(texto):
    while True:
        try:
            inteiro = int(input(texto))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número válido.')
            continue
        else:
            return inteiro
