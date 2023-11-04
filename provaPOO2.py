class Material():
    def __init__(self, titulo:str, autor_ou_editora:str):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
    def exibir_informacoes(self):
        return f"""
        Titulo: {self.titulo}
        Autor/Editora: {self.autor_ou_editora}
        """
class Livro(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, genero: str):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
    def exibir_informacoes(self):
        return f"""
        Titulo: {self.titulo}
        Autor/Editora: {self.autor_ou_editora}
        Gênero: {self.genero}
        """
class Revista(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, edicao: int):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    def exibir_informacoes(self):
        return f"""
        Titulo: {self.titulo}
        Autor/Editora: {self.autor_ou_editora}
        Edição: {self.edicao}
        """


material1 = Material(titulo="Dracula", autor_ou_editora="Bram")
print(material1.exibir_informacoes())

livro1 = Livro(titulo="Dracula", autor_ou_editora="Bram", genero="Terror")
print(livro1.exibir_informacoes())

revista1 = Revista(titulo="Queen of the universe: Lady Gaga", autor_ou_editora="Capricho", edicao=27)
print(revista1.exibir_informacoes())