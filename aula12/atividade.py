class Cachorro():
    def __init__(self, nome:str, raca:str, peso:float):
        self.nome = nome
        self.raca = raca
        self.peso = peso
    def comer (self):
        return f"O cachorro {self.nome} é da raça {self.raca}, pesa {self.peso} quilos e come: croc croc croc"
class Gato():
    def __init__(self, nome:str, raca:str, peso:float):
        self.nome = nome
        self.raca = raca
        self.peso = peso
    def derrubar (self):
        return f"O gato {self.nome} quebrou algo."

cachorro1_nome = str(input("Digite o nome do cachorro: "))
cachorro1_raca = str(input("Digite a raça do cachorro: "))
cachorro1_peso = float(input("Digite o peso do cachorro: "))
cachorro1 = Cachorro(nome = cachorro1_nome, raca = cachorro1_raca, peso = cachorro1_peso)
print(cachorro1.comer())

cachorro2_nome = str(input("Digite o nome do cachorro: "))
cachorro2_raca = str(input("Digite a raça do cachorro: "))
cachorro2_peso = float(input("Digite o peso do cachorro: "))
cachorro2 = Cachorro(nome = cachorro2_nome, raca = cachorro2_raca, peso = cachorro2_peso)
print(cachorro2.comer())

gato1_nome = str(input("Digite o nome do gato: "))
gato1_raca = str(input("Digite a raça do gato: "))
gato1_peso = float(input("Digite o peso do gato: "))
gato1 = Gato(nome = gato1_nome, raca = gato1_raca, peso = cachorro1_peso)
print(gato1.derrubar())