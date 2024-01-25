from livro.livro_Buscar import buscarPorCodigo
from livro.livro_Editar import editarLivro
from livro.livro_Listar import listarLivros
from livro.livro_Deletar import deletarLivro
from livro.livro_registrar import registrarLivro

def menu()-> None:
    while True:
        print("Bem Vindo ao Menu----")
        print("1- Adicionar Livro")
        print("2- Editar Livro")
        print("3- Deletar Livro")
        print("4- Buscar por codigo ")
        print("5- Listar Todos")
        print("6- Sair")
        opcao = input("Selecione uma opção:")
        if opcao == '1':
            codigo = int(input('Digite oCodigo'))
            titulo =input('Digite otitulo:')
            autor = input('Digite oAutor:')
            editarLivro(codigo,titulo,autor)
        elif opcao == '2':
            codigo = int(input('Digite oCodigo'))
            titulo = input('Digite otitulo:')
            autor = input('Digite oAutor:')
            editarLivro(codigo, titulo, autor)
        elif opcao == '3':
            codigo = int(input('Digite oCodigo'))
            deletarLivro(codigo)
        elif opcao == '4':
            codigo = int(input('Digite oCodigo'))
            print(buscarPorCodigo(codigo))
        elif opcao == '5':
            listarLivros()
        else:
            break







