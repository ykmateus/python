# #CRIE UMA CLASSE CHAMADA ANIMAL QUE TEM COMO PARAMETRO
# ESPECIE, SEXO, RAÇA, COR, IDADE
# E QUE TENHA COMO FUNÇOES
# ANDAR, CORRER, DORMIR, COMER

# PEDE PRO USUÁRIO ESCREVER OS 4 PARAMETROS
# CRIA UMA VARIAVEL INSTANCIANDO O OBJETO
# E MOSTRA NA TELA UMA DEMOSNTRAÇÃO DE TODAS AS FUNÇÕES
# E TAMBÉM TODOS OS ATRIBUTOS

class Animal():
    #metodo construtor
    #a função __init__ serve para construir o objeto
    def __init__(self, especie:str, sexo:str, raca:str, cor:str, idade:int):
        self.especie = especie
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.idade = idade
    def andar(self):
        return f"O {self.especie} andou"
    def correr(self):
        return f"O {self.especie} correu"
    def dormir(self):
        return f"O {self.especie} dormiu"
    def comer(self):
        return f"O {self.especie} comeu"
    
especie = str(input("Digite a especie: "))
sexo = str(input("Digite o sexo: "))
raca = str(input("Digite a raça: "))
cor = str(input("Digite a cor: "))
idade = int(input("Digite a idade: "))

animal1 = Animal(especie=especie, sexo=sexo, raca=raca, cor=cor, idade=idade)
    
print(animal1)
print(animal1.andar())
print(animal1.comer())
print(animal1.correr())
print(animal1.dormir())
