# class Animal:
#     def __init__(self, especie, raca, cor, idade):
#         self.especie = especie
#         self.raca = raca
#         self.cor = cor
#         self.idade = idade
    
#     def comer(self, alimento):
#         return f"O {self.especie} comeu o {alimento}"
    
#     def som(self):
#         return "Som indefinido"

# class Cachorro(Animal):
#     def __init__(self, raca, cor, idade):
#         super().__init__(especie = "cachorro", raca=raca, cor=cor, idade=idade)
    
#     def som(self):
#         return "Au au"
    
# class Gato(Animal):
#     def __init__(self, raca, cor, idade):
#         super().__init__(especie = "gato", raca=raca, cor=cor, idade=idade)

#     def som(self):
#         return "Miau"
    
# cachorro1 = Cachorro(raca="Pinsher", cor="caramelo", idade=1)
# gato1 = Gato(raca="Siamês", cor="branco", idade=3)

# print(cachorro1.som())
# print(gato1.som())

class Veiculo():
    def __init__(self, nome, qntd_motor, tem_roda):
        self.nome = nome
        self.qntd_motor = qntd_motor
        self.tem_roda = tem_roda
    def buzina(self):
        return "Buzina não identificado"
class Carro(Veiculo):
    def __init__(self, nome, qntd_motor, tem_roda):
        super().__init__(nome, qntd_motor, tem_roda)
    def buzina(self):
        return "Biiiii"
class Barco(Veiculo):
    def __init__(self, nome, qntd_motor, tem_roda):
        super().__init__(nome, qntd_motor, tem_roda)
    def buzina(self):
        return "Fooom"
class Aviao(Veiculo):
    def __init__(self, nome, qntd_motor, tem_roda):
        super().__init__(nome, qntd_motor, tem_roda)
    def buzina(self):
        return "Tem buzina?"
    
carro1 = Carro(nome="Gol", qntd_motor=2, tem_roda=4)
print(carro1.buzina())

barco1 = Barco(nome="Gol", qntd_motor=2, tem_roda=4)
print(barco1.buzina())

aviao1 = Aviao(nome="Gol", qntd_motor=2, tem_roda=4)
print(aviao1.buzina())