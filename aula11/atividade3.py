class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return self.saldo
        else:
            print("Saldo insuficiente")
        
    def exibir(self):
        return f"Seu saldo atual é: R${self.saldo}"
    
nome = str(input("Digite seu nome: "))
saldo = float(input("Digite seu saldo: "))
conta1 = ContaBancaria(nome=nome, saldo=saldo)

while True:
    menu = int(input("""
            1 - Depositar
            2 - Sacar
            3 - Exibir saldo
            0 - Sair
    """))

    if menu == 1:
        valor = float(input("Digite o valor que você quer depositar: "))
        conta1.depositar(valor)
    elif menu == 2:
        valor = float(input("Digite o valor que você quer sacar: "))
        conta1.sacar(valor)
    elif menu == 3:
        print(conta1.exibir())
    elif menu == 0:
        break
    else:
        print("Opção inválida")