class BombaCombustivel ():
    def __init__(self, tipoCombustivel: str, valorLitro: float, quantidadeCombustivel: int):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustive = quantidadeCombustivel
    def abastecerPorValos (self, valor):
        return f"Foi asbastecido {valor/self.valorLitro} litros."
    def abastecerPorLitro (self, litro):
        return f"Foi abastecido {litro} litros, valor a pagar: R${litro*self.valorLitro}"
    def alterarValor (self, novoValor):
        self.valorLitro = novoValor
        return f"Valor do litro atualizado para R$:{self.valorLitro}"
    def alterarCombustivel (self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        return f"Tipo de combustivel alterado para: {self.tipoCombustivel}"
    def alterarQuantidade (self, novoValor):
        self.quantidadeCombustivel = novoValor
        return f"Quantidade de combustivel alterada para: {self.quantidadeCombustivel} litros"


posto1 = BombaCombustivel(tipoCombustivel="Gasolina", valorLitro=5.29, quantidadeCombustivel=50)
carro1 = posto1.abastecerPorValos(50)
print(carro1)
carro2 = posto1.abastecerPorLitro(5)
print(carro2)
litro = posto1.alterarValor(6.23)
print(litro)
combustivel = posto1.alterarCombustivel("Diesel")
print(combustivel)
quantidade = posto1.alterarCombustivel(75)
print(quantidade)

