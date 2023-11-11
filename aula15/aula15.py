# FAÇA UMA CLASSE CHAMADA TELEVISAO QUE TEM OS ATRIBUTOS:
# NOME
# GÊNERO
# LANÇAMENTO
# E O MÉTODO:
# ASSISTIR (QUE RETORNA, VOCÊ ESTÁ ASSISTINDO {NOME})
# VER INFORMAÇÕES (QUE RETORNA TODAS AS INFORMAÇÕES EM QUESTÃO)

# CRIE UMA CLASSE FILHA CHAMADA FILME QUE HERDE TUDO DE TELEVISAO E CRIE UM NOVO ATRIBUTO CHAMADO duração
# E UM NOVO MÉTODO CHAMADO em_cartaz QUE RETORNA (O FILME {NOME} ESTÁ EM CARTAZ)
# POLIMORFISMO DO MÉTODO VER INFORMAÇÕES ADICIONANDO NO RETORNO A DURAÇÃO

# CRIE UMA CLASSE FILHA CHAMADA SERIE QUE HERDE TUDO DE TELEVISAO E CRIE UM NOVO ATRIBUTO CHAMADO temporadas 
# E UM NOVO MÉTODO CHAMADO maratonar QUE RETORNA (VOCÊ ESTÁ MARATONANDO A SÉRIO {NOME})
# POLIMORFISMO DO MÉTODO VER INFORMAÇÕES ADICIONANDO NO RETORNO AS TEMPORADAS


# FAÇA UM PROGRAMA COM UM MENU QUE PERGUNTA:
# 1 - ADICIONAR FILME
# 2 - VER FILMES
# 3 - DELETAR FILME
# 4 - ADICIONAR SÉRIE
# 5 - VER SÉRIES
# 6 - DELETAR SÉRIES
# 0 - SAIR

################################################################################################################

class Teste:
    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2
    
    def getN1(self):
        return self.__n1
    
    def setN1(self, novo_valor):
        self.__n1 = novo_valor
        return self.__n1
    

    def getN2(self):
        return self.__n2
    
    def setN2(self, novo_valor):
        self.__n2 = novo_valor
        return self.__n2
    
    def testando(self):
        return f"algo sobre o {self.getN1()}"
    
    def ver_infos(self):
        return f"""
            Nome: {self.getN1()}
            Gênero:
            Lançamento: 
        """
    
lista_n = []

while True:
    menu = int(input("""
        Escolha uma opção:
        1 - Adicionar N
        2 -Ver n's adicionados
        3 - Deletar N
    """))
    match menu:
        case 1:
            n1 = int(input("Digite o n1:"))
            n2 = int(input("Digite o n2:"))
            teste1 = Teste(n1=n1, n2=n2)
            lista_n.append(teste1)
        case 2:
            for item in lista_n:
                print(f"""
                Valor do n1: {item.getN1()}
                Valor do n2 : {item.getN2()}
                """)
        case 3:
            contador = 1
            for item in lista_n:
                print(f"""
                Item Nº{contador}
                Valor do n1: {item.getN1()}
                Valor do n2 : {item.getN2()}
                """)
                contador += 1
            selecionar = int(input("Digite o número do item que você quer deletar: "))
            lista_n.pop(selecionar -1)





class Televisao:
    def __init__(self, nome, genero, ano_lancamento):
        self.__nome = nome
        self.__genero = genero
        self.__ano_lancamento = ano_lancamento

    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    

    def getGenero(self):
        return self.__genero
    
    def setGenero(self, novo_valor):
        self.__genero = novo_valor
        return self.__genero
    

    def getAnoLancamento(self):
        return self.__ano_lancamento
    
    def setAnoLancamento(self, novo_valor):
        self.__ano_lancamento = novo_valor
        return self.__ano_lancamento
    

    def assitir(self):
        return f"Você está assistindo {self.getNome()}"
    
    def ver_informacoes(self):
        return f"""
        Nome - {self.getNome()}
        Gênero - {self.getGenero()}
        Ano de Lançamento - {self.getAnoLancamento()}
        """
    

class Filme(Televisao):
    def __init__(self, nome, genero, ano_lancamento, duracao):
        super().__init__(nome, genero, ano_lancamento)
        self.__duracao = duracao

    def getDuracao(self):
        return self.__duracao
    
    def setDuracao(self,novo_valor):
        self.__duracao = novo_valor
        return self.__duracao
    
    def ver_informacoes(self):
        return f"""
        Nome - {self.getNome()}
        Gênero - {self.getGenero()}
        Ano de Lançamento - {self.getAnoLancamento()}
        Duração - {self.getDuracao()}
        """

class Serie(Televisao):
    def __init__(self, nome, genero, ano_lancamento, temporadas):
        super().__init__(nome, genero, ano_lancamento)
        self.__temporadas = temporadas

    def getTemporadas(self):
        return self.__temporadas
    
    def setTemporadas(self,novo_valor):
        self.__temporadas = novo_valor
        return self.__temporadas
    
    def ver_informacoes(self):
        return f"""
        Nome - {self.getNome()}
        Gênero - {self.getGenero()}
        Ano de Lançamento - {self.getAnoLancamento()}
        Temporadas - {self.getTemporadas()}
        """
    
lista_de_filmes = []
lista_de_series = []

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Filmes
    2 - Séries
    0 - Sair
    """))

    match menu:
        case 1:
            submenu = int(input("""
                Escolha uma opção:
                1 - Adicionar Filme
                2 - Ver Filmes
                3 - Deletar Filme
                4 - Editar Filme
            """))

            match submenu:
                case 1:
                    nome_filme = str(input("Digite o nome do filme: "))
                    genero_filme = str(input("Digite o genero do filme: "))
                    lancamento_filme = str(input("Digite o lancamento do filme: "))
                    duracao_filme = str(input("Digite o duração do filme: "))

                    filme = Filme(nome= nome_filme, genero=genero_filme, ano_lancamento=lancamento_filme, duracao=duracao_filme)

                    lista_de_filmes.append(filme)
                case 2:
                    for filme in lista_de_filmes:
                        print(filme.ver_informacoes())
                case 3:
                    contador = 1
                    for filme in lista_de_filmes:
                        print(f"{contador} - {filme.getNome()}")
                        contador += 1
                    selecionado = int(input("Digite o número do filme que deseja deletar: "))

                    lista_de_filmes.pop(selecionado -1)
                case 4:
                    contador = 1
                    for filme in lista_de_filmes:
                        print(f"""{contador}
                              {filme.ver_informacoes()}""")
                        contador += 1
                    selecionado = int(input("Digite o número do filme que deseja deletar: "))
                    
                    escolha = int(input("""
                        O que você deseja editar:
                        1 - Nome
                        2 - Gênero
                        3 - Ano de Lançamento
                        4 - Duração
                    """))

                    match escolha:
                        case 1:
                            novo_nome_filme = str(input("Digite o novo nome do filme: "))
                            lista_de_filmes[selecionado - 1].setNome(novo_nome_filme)
                        case 2:
                            novo_genero_filme = str(input("Digite o novo genero do filme: "))
                            lista_de_filmes[selecionado - 1].setGenero(novo_genero_filme)
                        case 3:
                            novo_ano_lancamento_filme = str(input("Digite o novo ano lancamento do filme: "))
                            lista_de_filmes[selecionado - 1].setAnoLancamento(novo_ano_lancamento_filme)
                        case 4:
                            novo_duracao_filme = str(input("Digite o novo duracao do filme: "))
                            lista_de_filmes[selecionado - 1].setDuracao(novo_duracao_filme)

        case 2:
            submenu = int(input("""
                Escolha uma opção:
                1 - Adicionar Série
                2 - Ver Séries
                3 - Deletar Série
            """))
            match submenu:
                case 1:
                    nome_serie = str(input("Digite o nome da serie: "))
                    genero_serie = str(input("Digite o genero da serie: "))
                    lancamento_serie = str(input("Digite o lancamento da serie: "))
                    temporadas_serie = str(input("Digite a quantidade de temporadas da serie: "))

                    serie = Serie(nome= nome_serie, genero=genero_serie, ano_lancamento=lancamento_serie, temporadas=temporadas_serie)

                    lista_de_series.append(serie)
                case 2:
                    for serie in lista_de_series:
                        print(serie.ver_informacoes())
                case 3:
                    contador = 1
                    for serie in lista_de_series:
                        print(f"{contador} - {serie.getNome()}")
                        contador += 1
                    selecionado = int(input("Digite o número do série que deseja deletar: "))

                    lista_de_series.pop(selecionado - 1)
        case 0:
            print("Obrigado, volte nunca")
            break
        case _:
            print("Opção inválida")