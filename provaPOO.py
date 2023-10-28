class Elevador():
    
    def __init__(self, total_capacidade=int, atual_capacidade=int, total_andar=int, atual_andar=int):
        self.total_capacidade = total_capacidade
        self.atual_capacidade = atual_capacidade
        self.total_andar = total_andar
        self.atual_andar = atual_andar

    def subir():
        if self.atual_andar == self.total_andar:
            return "VOCÊ ESTÁ NO ANDAR MAIS ALTO!"
        else:
            self.atual_andar += 1
            return "Subindo."
    def descer ():
        if self.atual_andar == 0:
            return "VOCÊ JÁ ESTÁ NO TÉRREO!"
        else:
            self.atual_andar -= 1
            return "Descendo"
    def entrar ():
        if self.atual_capacidade == self.total_capacidade:
            return "O ELEVADOR ESTÁ CHEIO!"
        else:
            self.atual_capacidade + 1
            return "Entrando uma pessoa"
