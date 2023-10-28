# ENCAPSULAMENTO:
class Pessoa:
    def __init__(self, nome, rg, cpf, telefone, endereco):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco


    def informacoes(self):
        return f"""
            Nome: {self.__nome}
            RG: {self.__rg}
            CPF: {self.__cpf}
            Telefone: {self.__telefone}
            Endereço: {self.__endereco}
        """
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    

    def getRG(self):
        return self.__rg
    
    def setRG(self, novo_valor):
        self.__rg = novo_valor
        return self.__rg
    


    def getCPF(self):
        return self.__cpf
    
    def setCPF(self, novo_valor):
        self.__cpf = novo_valor
        return self.__cpf
    


    def getTelefone(self):
        return self.__telefone
    
    def setTelefone(self, novo_valor):
        self.__telefone = novo_valor
        return self.__telefone
    


    def getEndereco(self):
        return self.__endereco
    
    def setEndereco(self, novo_valor):
        self.__endereco = novo_valor
        return self.__endereco


abel = Pessoa(nome="Abelardo", rg="123", cpf="456", telefone="789", endereco="a")

abel.setCPF("123.456.789-00")


print(abel.informacoes())
