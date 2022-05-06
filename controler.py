
from view import menu_trainee, menu_vagas, tabela_grid
from model import Candidato, Vaga, ValidaCpf
from validacoes import *

vagas = []

vagas.append(Vaga(1, "RH", 3))
vagas.append(Vaga(2, "Suporte", 3))
vagas.append(Vaga(3, "Desenvolvedor", 3))


def Applicacao():

    while True:

        menu_trainee('Chamando Menu Trainee')

        opcao = leia_inteiro('Digite uma opção: ')  # validar

        if opcao == 1:
            menu_vagas(vagas)

            if len(vagas) == 0:
                print('Nenhuma Vaga em Aberto')
                continue

        elif opcao == 2:

            # obrigatoriedade dos dados
            nome = valida_nome()
            sob = valida_sobrenome()

            # validando cpf
            cpf = str(input('CPF: '))
            # true se é valido, false ñ valido
            validando_cpf = ValidaCpf(cpf)
            # formato o cpf de entrada
            new_cpf = re.sub('[^0-9]', '', cpf)
            # se cpf inserido é valido
            if validando_cpf.valida():
                # se cpf nao estiver duplicado, segue o cadastro
                if not duplicidade_cpf(new_cpf):

                    # validar data
                    data = input('Data de Nascimento! (dd/mm/aaaa)')

                    # validar inteiro
                    vaga = leia_inteiro('Vaga: ')

                    # adicionando candidato em memoria
                    candidato = Candidato(nome, sob, new_cpf, data, vaga)

                    # validando a quantidade de vagas
                    valida_qtde_vagas(vagas, vaga, candidato)

            else:
                print('CPF digitado é inválido')


        elif opcao == 3:
            try:
                arq = 'bancodedados.txt'
                arquivo_final(arq)

                for v in vagas:
                    for c in v.candidatos:

                        cadastrar_arquivo(arq, c.nome, c.sobrenome,
                                                        c.cpf, c.data, c.vaga)
                # save checkpoint


                    v.candidatos.clear()
                    # limpeza dos candidatos na lista

                x = tabela_grid(arq)
                print(x)

            except:
                print('ERRO ao Salvar candidato!')

        elif opcao == 9:
            print('Saindo da Aplicação')
            break

        else:
            print('Opção Inválida! Tente novamente!')
            continue

