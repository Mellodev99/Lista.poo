import os
class estudantes:
    def __init__(self, nome, curso, situacao, ):
        self.nome(nome)
        self.curso(curso)
        self.situacao(situacao)
        situacao = True


def exibir_nome_do_progama():
    print('-------------SISTEMA DE GERENCIAMENTO ACADEMICO-------------------')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_estudantes()
        elif opcao_escolhida == 2:
           estudantes.listar_estudantes()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def exibir_opcoes():
    print('1. Cadastrar estudante')
    print('2. Listar estudantes')
    print('4. Sair\n')

def cadastrar_estudantes():
   print('Opcao cadastar estudante selecionada!')

def listar_estudantes():
    print('Opcao listar estudantes escolhida!')   
def alterar_situacao_estudante():
    print('Opção Alterar situação selecionada.')    


def main():
  
    exibir_nome_do_progama
    exibir_opcoes
    escolher_opcao

if __name__ == '__main__':
    main()    