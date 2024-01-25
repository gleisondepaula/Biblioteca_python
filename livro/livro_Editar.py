from repositorio.livro_repositorio import livro_repositorio
from livro.livro_Buscar import buscarPorCodigo
def editarLivro(codigo:int,titulo:str,autor:str)->None:
    livro = buscarPorCodigo(codigo)
    if livro:
       livro['titulo']= titulo
       livro['autor']= autor
       print('dados alterados com Sucesso!')
    else:
        print('Livro não enconttrado!')
if __name__ == "__main__":
    editarLivro(1,"Clean Code","Artur")
    print(buscarPorCodigo(1))
    editarLivro(2,"AS Cronicas de Narlilia","wells")




