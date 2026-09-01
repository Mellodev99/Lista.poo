def cadastrar_estudante():
    """
    Solicita o nome, a matrícula e o curso de um estudante
    e exibe uma mensagem confirmando o cadastro.
    """

    nome = input('Digite o nome do estudante: ')
    matricula = input('Digite a matrícula: ')
    curso = input('Digite o curso: ')

    print(f'Estudante {nome} cadastrado com sucesso!')
    print(f'Matrícula: {matricula}')
    print(f'Curso: {curso}')


cadastrar_estudante()