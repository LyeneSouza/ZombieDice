# Aluna: Lyene de Souza Benvenutti
# Curso: Gestão da Tecnologia da Informação
# Entrega final - Semana 8

import random
import time

# Declarar as funções que serão utilizadas no decorrer do código


def inicializar_dados():
    """
    A função inicializar_dados() estabelece a lista do total de dados do jogo

    :return: retorna a lista composta pelos dados adicionados
    """

    # Adiciona 6 dados na cor verde, representados pela letra 'G'
    # Adiciona 4 dados na cor amarela, representados pela letra 'Y'
    # Adiciona 3 dados na cor vermelha, representados pela letra 'R'
    tubo = ['G', 'G', 'G', 'G', 'G', 'G', 'Y', 'Y', 'Y', 'Y', 'R', 'R', 'R']
    return tubo


def mostrar_dados(dados):
    """
    A função mostrar_dados() imprime a lista com todos os dados que estão no tubo

    :param dados: a lista que contém os dados do tubo
    """

    print(f'Dentro do tubo temos os seguintes dados: {dados}')
    time.sleep(0.8)


def sortear_dados(dados, numero_de_dados):
    """
    A função sortear_dados() sorteia o número de dados solicitado da lista indicada

    :param dados: a lista de dados da qual a função vai sortear os dados
    :param numero_de_dados: quantos dados devem ser sorteados
    :return: retorna quais dados foram sorteados
    """

    dados_sorteados = []
    for i in range(numero_de_dados):
        dados_sorteados.append(random.choice(dados))
    return dados_sorteados


def remover_dados(dados, remover):
    """
    A função remover_dados() remove os dados selecionados da lista indicada

    :param dados: a lista da qual a função vai remover os dados selecionados
    :param remover: uma lista que indica quais dados a função deve remover da lista indicada no parâmetro "dados"
    :return: retorna a lista de dados atualizada, após a remoção dos dados selecionados
    """

    for i in range(len(remover)):
        dados.remove(remover[i])
    return dados


def cores_sorteadas(dados_sorteados):
    """
    A função cores_sorteadas() imprime quais as cores dos dados que foram sorteados

    :param dados_sorteados: a lista contendo os dados sorteados
    """

    print(f'\nOs dados sorteados foram: {dados_sorteados}')
    time.sleep(0.8)


def rolar_dados(dados):
    """
    A função rolar_dados() sorteia uma face de cada dado contido na lista indicada

    :param dados: a lista de dados que devem ser rolados
    :return: a lista com as faces sorteadas dos dados rolados
    """

    # Face 'C' significa 'cérebro'
    # Face 'P' significa 'passos'
    # Face 'T' significa 'tiro'
    GREEN_DICE = ('C', 'C', 'C', 'P', 'P', 'T')
    YELLOW_DICE = ('C', 'C', 'P', 'P', 'T', 'T')
    RED_DICE = ('C', 'P', 'P', 'T', 'T', 'T')
    faces_sorteadas = []
    for i in range(len(dados)):
        if dados[i] == 'G':
            faces_sorteadas.append(random.choice(GREEN_DICE))
        elif dados[i] == 'Y':
            faces_sorteadas.append(random.choice(YELLOW_DICE))
        elif dados[i] == 'R':
            faces_sorteadas.append(random.choice(RED_DICE))
    return faces_sorteadas


def mostrar_faces(faces):
    """
    A função mostrar_faces() imprime a lista com as faces sorteadas após rolar os dados

    :param faces: a lista que contém as faces sorteadas
    """

    print(f'\nAs faces sorteadas foram: {faces}')
    time.sleep(0.8)


def mostrar_placar_rodada(cerebros, passos, tiros):
    """
    A função mostrar_placar_rodada() imprime o número de cérebros, passos e tiros da rodada

    :param cerebros: variável que contém o número de cérebros que o jogador tem na rodada
    :param passos: variável que contém o número de passos que o jogador tem na rodada
    :param tiros: variável que contém o número de tiros que o jogador tem na rodada
    """

    print(f'\nPlacar da rodada:\nCérebros: {cerebros}\nPassos: {passos}\nTiros: {tiros}')
    time.sleep(0.8)


def mostrar_placar(numero_jogadores, nomes, pontos):
    """
    A função mostrar_placar() imprime o placar atualizado, contendo o nome de cada jogador e seus respectivos pontos

    :param numero_jogadores: a lista contendo o número de participantes
    :param nomes: a lista contendo os nomes dos jogadores
    :param pontos: a lista contendo os pontos dos jogadores
    """

    print('Placar:')
    for i in range(numero_jogadores):
        print(f'{nomes[i]}: {pontos[i]}')


def continuar_jogando():
    """
    A função continuar_jogando() pergunta ao usuário se ele deseja continuar jogando

    :return: retorna a resposta do usuário em booleano
    """

    while True:
        continuar = (input('\nDeseja continuar jogando? (Responda s para sim e n para não) '))
        if continuar in 'Ss':
            return True
        elif continuar in 'Nn':
            return False
        else:
            print('Resposta inválida.')


def verificar_ganhador(numero_jogadores, nomes, pontos):
    """
    A função verificar_ganhador() verifica se algum jogador alcançou 13 pontos ou mais e, se houver ganhador,
    mostra quem ganhou.

    :param numero_jogadores: a lista contendo o número de participantes
    :param nomes: a lista contendo os nomes dos jogadores
    :param pontos: a lista contendo os pontos dos jogadores
    :return: retorna se o jogo acabou em booleano
    """

    # Verificar se algum jogador ganhou
    fim_jogo = False
    bigger_score = pontos[0]
    winner_player = nomes[0]
    for i in range(numero_jogadores):
        if pontos[i] >= 13:
            fim_jogo = True
        if pontos[i] > bigger_score:
            bigger_score = pontos[i]
            winner_player = nomes[i]

    # Mostrar quem ganhou
    if fim_jogo:
        time.sleep(0.8)
        print('\nO jogo terminou!')
        mostrar_placar(numero_jogadores, nomes, pontos)
        print(f'{winner_player} venceu!!')

    return fim_jogo


# Tela inicial do jogo
JOGO = 'Zombie Dice'
print('=' * 38)
print(f'===Sejam bem-vindos ao {JOGO}!===')
print('=' * 38)

# Definir quantos jogadores
while True:
    # Verificar se o valor digitado pelo usuário é válido
    try:
        n_players = int(input('\nQuantos jogadores vão participar? '))
        # Verificar se o número de jogadores indicado pelo usuário segue a regra de mínimo de 2 jogadores
        while n_players < 2:
            print('\nNúmero de jogadores insuficiente. Para jogar, são necessários no mínimo 2 jogadores!')
            n_players = int(input('Defina novamente o número de jogadores: '))
        break
    except ValueError:
        print('\nValor inválido!')

print('\nVamos jogar!')
time.sleep(0.8)

# Definir os nomes dos jogadores
print('\nAntes de começarmos, vamos registrar quem são os jogadores!')
time.sleep(0.5)
player_names = []
for i in range(n_players):
    player_names.append(input(f'Qual o nome do(a) jogador(a) {i + 1}? '))

print('\nAgora sim, vamos começar! Boa sorte!')
time.sleep(0.5)

# Armazenar a pontuação dos jogadores
player_score = []
for i in range(n_players):
    player_score.append(0)

# Definir a rodada
end_game = False
end_round = True
index_player = 0

while not end_game:

    # Garantir que todos os participantes joguem o mesmo número de rodadas
    same_round_number = False

    if end_round:
        cerebros = 0
        passos = 0
        tiros = 0
        dices_passos = []
        dices = inicializar_dados()
        print('\nNOVA RODADA:')

        # Mostrar o placar
        mostrar_placar(n_players, player_names, player_score)

        # Definir o jogador da vez
        print(f'\nVEZ DO(A) JOGADOR(A): {player_names[index_player]}')
        time.sleep(0.8)
    else:
        print(f'\nO(A) JOGADOR(A) {player_names[index_player]} DECIDIU CONTINUAR!')

    # Começar a rodada
    print('\nVamos sortear os dados de dentro do tubo!')
    time.sleep(0.8)

    # Sortear os dados de dentro do tubo totalizando 3 (considerar se há dados de "passos" para rerrolar)
    sorted_dices = sortear_dados(dices, 3 - len(dices_passos))
    remover_dados(dices, sorted_dices)
    sorted_dices.extend(dices_passos)
    dices_passos = []

    # Mostrar as cores dos dados que foram sorteados e os que ainda restam no tubo
    cores_sorteadas(sorted_dices)
    mostrar_dados(dices)

    # Rolar os 3 dados sorteados
    sorted_faces = rolar_dados(sorted_dices)
    mostrar_faces(sorted_faces)

    # Contabilizar os cérebros, passos e tiros da rodada sorteados nas faces
    for i in range(len(sorted_faces)):
        if sorted_faces[i] == 'C':
            cerebros += 1
        elif sorted_faces[i] == 'P':
            passos += 1
            dices_passos.append(sorted_dices[i])
        elif sorted_faces[i] == 'T':
            tiros += 1

    # Mostrar o placar da rodada
    mostrar_placar_rodada(cerebros, passos, tiros)

    # Conferir se saiu "tiro" 3 vezes ou mais
    if tiros >= 3:
        print(f'Você levou {tiros} tiros! Por isso não pontuou nessa rodada...')
        time.sleep(0.8)
        index_player += 1
        end_round = True
        if index_player >= len(player_names):
            index_player = 0
            same_round_number = True
    else:
        # Perguntar se o usuário deseja continuar jogando
        if continuar_jogando():
            end_round = False
            passos = 0
        else:
            # Atualizar o placar
            player_score[index_player] += cerebros
            index_player += 1
            end_round = True
            if index_player >= len(player_names):
                index_player = 0
                same_round_number = True

    # Definir quando o jogo acaba
    if same_round_number:
        end_game = verificar_ganhador(n_players, player_names, player_score)
