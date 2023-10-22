class Livro():
    def __init__(self, titulo:str, autor:str, genero:str, pag:int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.pag = pag
    def exibir(self):
        return f"""
        Titulo: {self.titulo}
        Autor: {self.autor}
        Genero: {self.genero}
        Páginas: {self.pag}
        """
    def tamanho(self):
        if self.pag > 350:
            return f"O livro {self.titulo} é um livero longo, com {self.pag} páginas."
        else:
            return f"O livro {self.titulo} é um livero curto, com {self.pag} páginas."

titulo = str(input("Digite o titulo do livro: "))
autor = str(input("Digite o autor do livro: "))
genero = str(input("Digite o genero do livro: "))
pag = int(input("Digite a quantidade de páginas do livro: "))

livro1 = Livro(titulo=titulo, autor=autor, genero=genero, pag=pag)
print(livro1.exibir())
print(livro1.tamanho())
