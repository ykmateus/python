#Cadatro do time
class Time():
    def __init__(self, nome_time: str, cidade: str, mascote: str):
        self.__nome_time = nome_time
        self.__cidade = cidade
        self.__mascote = mascote
    def exibir_informacoes(self):
        return f"""
        Time: {self.__nome_time}
        Cidade: {self.__cidade}
        Mascote: {self.__mascote}
        """
    #Encapsulameto
    def getNome(self):
        return self.__nome_time
    def getCidade(self):
        return self.__cidade
    def getMascote(self):
        return self.__mascote
    
    def setNome(self, novo_valor):
        self.__nome_time = novo_valor
        return self.__nome_time
    def setCidade(self, novo_valor):
        self.__cidade = novo_valor
        return self.__cidade
    def setMascote(self, novo_valor):
        self.__mascote = novo_valor
        return self.__mascote

#Cadastro do jogador
class Jogador():
    def __init__(self, nome:str, time: str, camisa:int):
        self.__nome = nome
        self.__time = time
        self.__camisa = camisa
    def exibir_informacoes(self):
        return f"""
        Jogador: {self.__nome}
        Time: {self.__time}
        Camisa: {self.__camisa}
        """
    #Encapsulameto
    def getNome(self):
        return self.__nome
    def getTime(self):
        return self.__time
    def getCamisa(self):
        return self.__camisa
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    def setTime(self, novo_valor):
        self.__time = novo_valor
        return self.__time
    def setCamisa(self, novo_valor):
        self.__camisa = novo_valor
        return self.__camisa
    

#Cadastro comissão
class Comissao():
    def __init__(self, nome:str, time:str):
        self.__nome = nome
        self.__time = time
    #Encapsulameto
    def getNome(self):
        return self.__nome
    def getTime(self):
        return self.__time
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    def setTime(self, novo_valor):
        self.__time = novo_valor
        return self.__time


class Tecnico(Comissao):
    def __init__(self, nome: str, time: str, esquema:str):
        super().__init__(nome, time)
        self.__esquema = esquema
    def exibir_informacoes(self):
        return f"""
        Técnico: {self.__nome}
        Time: {self.__time}
        Esquema: {self.__esquema}
        """
    def dar_coletiva(self):
        return f"O Técnico {self.__nome} está dando uma coletiva de imprensa."
    #Encapsulameto
    def getEsquema(self):
        return self.__esquema
    def setEsquema(self, novo_valor):
        self.__esquema = novo_valor
        return self.__esquema
    
class Auxiliar(Tecnico):
    def __init__(self, nome: str, time: str, esquema: str):
        super().__init__(nome, time, esquema)
    def exibir_informacoes(self):
        return f"""
        Auxiliar: {self.__nome}
        Time: {self.__time}
        Esquema: {self.__esquema}
        """
    def dar_coletiva(self):
        return f"O Auxiliar {self.__nome} está dando uma coletiva de imprensa."
    
class Preparador(Comissao):
    def __init__(self, nome: str, time: str, elenco: str):
        super().__init__(nome, time)
        self.__elenco = elenco
    def exibir_informacoes(self):
        return f"""
        Preparador: {self.__nome}
        Time: {self.__time}
        Elenco: {self.__elenco}
        """
    def dar_coletiva(self):
        return f"O Preparador {self.__nome} está dando uma coletiva de imprensa."
    #Encapsulameto
    def getElenco(self):
        return self.__elenco
    def setElenco(self, novo_valor):
        self.__elenco = novo_valor
        return self.__elenco
    

menu = int(input("""
Escola uma opção de cadastro:
1 - Time
2 - Jogador 
3 - Comissão Técnica         
"""))

if menu == 1:
    nome_time = str(input("Digite o nome do time: "))
    cidade = str(input("Digite a cidade do time mandante: "))
    mascote = str(input("Digite o nome do mascote: "))
    time1 = Time(nome_time=nome_time, cidade=cidade, mascote=mascote)
    print(time1.exibir_informacoes())
elif menu == 2:
    nome = str(input("Digite o nome do jogador: "))
    time = str(input("Digite o time do jogador: "))
    camisa = int(input("Digite o número da camisa do jogador: "))
    jogador1 = Jogador(nome=nome, time=time, camisa=camisa)
    print(jogador1.exibir_informacoes())
elif menu == 3:
    menu_comissao = int(input("""
    Escolha uma opção de cadastro:
    1 - Técnico
    2 - Auxiliar
    3 - Preparador Físico
    """))
    if menu_comissao == 1:
        nome_tecnico = str(input("Digite o nome do técnico: "))
        time_tecnico = str(input("Digite o time do técnico: "))
        esquema_tecnico = str(input("Digite o esquema do técnico: "))
        tecnico1 = Tecnico(nome=nome_tecnico, time=time_tecnico, esquema=esquema_tecnico)
        print(tecnico1.exibir_informacoes())
        print(tecnico1.dar_coletiva())
    elif menu_comissao == 2:
        nome_auxiliar = str(input("Digite o nome do auxiliar: "))
        time_auxiliar = str(input("Digite o time do auxiliar: "))
        esquema_auxiliar = str(input("Digite o esquema do auxiliar: "))
        auxiliar1 = Auxiliar(nome=nome_auxiliar, time=time_auxiliar, esquema=esquema_auxiliar)
        print(auxiliar1.exibir_informacoes())
        print(auxiliar1.dar_coletiva())
    elif menu_comissao == 3:
        nome_preparador = str(input("Digite o nome do preparador: "))
        time_preparador = str(input("Digite o time do preparador: "))
        elenco = str(input("Digite o elenco do preparador: "))
        preparador1 = Preparador(nome=nome_preparador, time=time_preparador, elenco=elenco)
        print(preparador1.exibir_informacoes())
        print(preparador1.dar_coletiva())
    else:
        print("Opção inválida")
else:
    print("Opção inválida")