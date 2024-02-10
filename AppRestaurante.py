import os                       #>> Biblioteca para interagir com o Sistema Operacional
import time                     #>> Biblioteca para adicionar temporizador
from datetime import datetime   #>> Biblioteca para tratar data e hora
import keyboard                 #>> Biblioteca para esperar acionamento de qualquer tecla

restaurantes = [{'nome':'Bom sabor','categoria':'Brasileira','ativo':False},
                {'nome':'Apetito','categoria':'Francesa','ativo':False},
                {'nome':'100 Maneiras','categoria':'Italiana','ativo':True},
                {'nome':'Calçadão','categoria':'Frutos do mar','ativo':False},
                {'nome':'Na Brasa','categoria':'Churrasco','ativo':True}]

def exibir_nome_app():
    print("""

██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░██████╗░██████╗░
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██████╔╝██████╔╝
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██╔═══╝░██╔═══╝░
██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░░░░░██║░░░░░
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░
""")

# Função Limpar tela
def limpar_tela():
    os.system('cls')
    print()

# Função voltar menu
def voltar_menu():
    input('\nPressione Enter para voltar ao menu ')
    main()

# Função valida opção escolhida
def valida_opcao():
    print('\nOpção digitada inválida!\n')
    voltar_menu()

# Função exibir subtitulo
def exibir_subtitulo(texto):
    limpar_tela()
    linha = '#' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# Função exibir data e hora atual
def data_atual():
    data_hora_atual = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_hora_formatada
data_atualizada = data_atual()

# Função listar as opções
def exibir_opcoes():
    print('1. Adicionar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# Função adicionar restaurante
def adicionar_restaurante():
    exibir_subtitulo('Adicionar novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado!\n')
    voltar_menu()

# Função listar restaurantes
def listar_restaurantes():
    #limpar_tela()
    exibir_subtitulo('Lista de restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu()

# Função ativar o cadastro do restaurante
def alterar_status():
    exibir_subtitulo('Alterando status do restaurante')
    nome_restaurante = input('Digite o restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restautante {nome_restaurante} foi ativado!' if restaurante['ativo'] else f'O restautante foi desativado!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu()

# Função finalizar app
def finaliza_app ():
    time.sleep(0.5)
    print('Finalizando o app...')
    time.sleep(0.6)
    print(f'App finalizado em {data_atualizada}!\n')
    time.sleep(0.6)
    limpar_tela()

# Função para escolher uma opção
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))
        if opcao_escolhida == 1:
            adicionar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status()
        elif opcao_escolhida == 4:
            finaliza_app()
        else:
            valida_opcao()
    except:
        valida_opcao()
        
# >> Função principal do programa para agrupar as funções que o programa irá executar
def main():
    limpar_tela()
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()