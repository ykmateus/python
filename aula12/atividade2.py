class Tamagotchi():
    def __init__(self, nome: str, saude:int, energia: int):
        self.nome = nome
        self.saude = saude
        self.energia = energia
    def brincar (self):
        self.energia -= 10
        return f"""
        O {self.nome} está brincando.
        -10 Energia
        Energia atual: {self.energia}
        """
    def lutar (self):
        self.energia -= 20
        return f"""
        O {self.nome} está lutando.
        -20 Energia
        Energia atual: {self.energia}
        """

tama_nome = str(input("Digite o nome do Tamagotchi: "))
tama_energia = 100
tama1 = Tamagotchi(nome = tama_nome, saude = 100, energia=tama_energia)
while True:
    menu = int(input("""
    Escolha uma ação:
    1 - Brincar
    2 - Lutar
    """))
    if menu == 1:
        print(tama1.brincar())
    elif menu == 2:
        print(tama1.lutar())
    else:
        break

    





