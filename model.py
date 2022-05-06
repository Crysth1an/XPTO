import re

class Pessoa():

    def __init__(self, nome, sobrenome, cpf, data):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data = data

    def validar_nome(self, nome):
        self.nome = nome

    def validar_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def validar_cpf(self, cpf):
        self.cpf = cpf

    def validar_data(self, data):
        self.data = data


class Vaga():
    def __init__(self, id, nome, vagas):

        self.id = id
        self.nome = nome
        self.vagas = vagas
        self.candidatos = []

    def validar_id(self, id):
        self.id = id

    def validar_vagas(self):
        return len(self.candidatos) > self.vagas  # True or False


class Candidato(Pessoa):

    def __init__(self, nome, sobrenome, cpf, data, vaga):
        super().__init__(nome, sobrenome, cpf, data)
        self.vaga = vaga


class ValidaCpf:
    def __init__(self, cpf):
        self.cpf = cpf
        print(self.cpf)

    def valida(self):
        if not self.cpf:
            return False

        novo_cpf = self._calcula_digitos(self.cpf[:9])
        novo_cpf = self._calcula_digitos(novo_cpf)

        if novo_cpf == self.cpf:
            return True
        return False


    @staticmethod
    def _calcula_digitos(fatia_cpf):
        if not fatia_cpf:
            return False

        sequencia = fatia_cpf[0] * len(fatia_cpf)

        if sequencia == fatia_cpf:
            return False

        soma = 0
        for chave, multiplcador in enumerate(range(len(fatia_cpf)+1, 1, -1)):
            soma += int(fatia_cpf[chave]) * multiplcador

        resto = 11 - (soma % 11)
        resto = resto if resto <= 9 else 0

        return fatia_cpf + str(resto)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self.so_numeros(cpf)

    @staticmethod
    def so_numeros(cpf):
       return re.sub('[^0-9]', '', cpf)
