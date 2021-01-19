from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, rg, cpf, telefone):
        self.nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.telefone = telefone

    @abstractmethod
    def get_rg(self):
        pass

    @abstractmethod
    def get_cpf(self):
        pass

    @abstractmethod
    def set_rg(self, rg):
        pass

    @abstractmethod
    def set_cpf(self, cpf):
        pass


class Medico(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, crm, salario, especialidade):
        super().__init__(nome, rg, cpf, telefone)
        self.__crm = crm
        self.salario = salario
        self.especialidade = especialidade

    def get_rg(self):
        return self.__rg

    def get_cpf(self):
        return self.__cpf

    def get_crm(self):
        return self.__crm

    def set_rg(self, rg):
        self.__rg = rg

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_crm(self, crm):
        self.__crm = crm


class Paciente(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, endereco, data_nasc, medico):
        super().__init__(nome, rg, cpf, telefone)
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.medico = medico

    def get_rg(self):
        return self.__rg

    def get_cpf(self):
        return self.__cpf

    def set_rg(self, rg):
        self.__rg = rg

    def set_cpf(self, cpf):
        self.__cpf = cpf


class Quarto():
    def __init__(self, numero_quarto, andar_quarto, paciente, medico):
        self.paciente = paciente
        self.medico = medico
        self.numero_quarto = numero_quarto
        self.andar_quarto = andar_quarto


class Historico():
    def __init__(self, data, horario, observacao, medico, paciente, quarto):
        self.data = data
        self.horario = horario
        self.observacao = observacao
        self.medico = medico
        self.paciente = paciente
        self.quarto = quarto

    def exibir_historico(self):
        print("Nome do paciente:", self.paciente.nome)
        print("Médico Responsável:", self.medico.nome)
        print("Número do quarto:", self.quarto.numero_quarto)
        print("Andar do quarto:", self.quarto.andar_quarto)
        print("Data:", self.data)
        print("Horario:", self.horario)
        print("Observação:", self.observacao)


def separador():
    separador = '=-' * 30
    print(separador)


'''
INICIO DO PROGRAMA PRINCIPAL: INSTANCIAMENTO
'''
separador()

'''
DADOS DO MEDICO:
'''

nome_m = "BERNARDO"
rg_m = "11.222.333-4"
cpf_m = "111.222.333.44"
tel_m = "(011)95555-6666"
crm = "F111111"
sal = "7800"
espec = "CARDIOLOGISTA"

med = Medico(nome_m, rg_m, cpf_m, tel_m, crm, sal, espec)

'''
DADOS DO PACIENTE:
'''

nome_p = "TADEU"
rg_p = "22.333.444-5"
cpf_p = "222.333.444-55"
tel_p = "(011)92222-3333"
endereco = "AVENIDA PAULISTA, 597"
data_nascimento = "20/03/1994"

pac = Paciente(nome_p, rg_p, cpf_p, tel_p, endereco, data_nascimento, med)

'''
DADOS DO QUARTO:
'''

n_quarto = "05"
a_quarto = "03"

quar = Quarto(n_quarto, a_quarto, pac, med)

'''
DADOS DO HISTÓRICO:
'''

data = "20/10/2020"
horario = "11:35"
obs = "PACIENTE APRESENTOU MELHORA NO QUADRO."
hist = Historico(data, horario, obs, med, pac, quar)

hist.exibir_historico()

separador()

'''
Classe Pessoa: É uma classe abstrata que armazena os atributos em comum
entra a classe Medio e a classe Paciente:
nome, cpf, rg e telefone. Tendo como metodos abstratos get_cpf, get_rg,
set_cpf, set_rg.
Os metodos get retorna o valor do atributo e
o metodo set altera o valor do atributo.
'''

'''
Classe Medico: Possui todas os atributos da classe pessoa, e mais alguns
adicionais, onde somente ele possui: crm, salario e especialidade.
Além dos metodos criados na classe pessoa, existe também o metodo
get_crm, que retorna o valor do atributo e o metodo set_crm que altera
o valor do atributo.
'''

'''
Classe Paciente: Possui todos os atributos da classe pessoa, incluindo
os atributos data de nascimento, endereco. Além de relacionar o paciente
com o medico responsável pelo caso dele.
Como metodos, essa classe apresenta os mesmos metodos abstratos da classe
pessoa.
'''

'''
Classe Quarto: Possui como atributo o andar do quarto e o numero do quarto,
além de possuir um relacionamento com o paciente que está internado nele e
com o medico responsavel pelo paciente internado.
Essa classe não possui metodos.
'''

'''
Classe Historico: armazena os atributos data, horario, observacao, e também
estabelece relacionamento com as classes medico, paciente e quarto.
Essa classe possui, como metodo exibir_historico, onde será exibido
dados como: o nome do paciente, nome do medico, dados a respeito do quarto
(numero e andar), além de exibir o dia da observacao feita pelo medico, o
horario que ele anotou a observacao e também exibe o que o medico anotou.
'''
