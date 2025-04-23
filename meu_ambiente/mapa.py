import numpy as np

# Mapa será 5x5
mapa = np.random.randint(1, 10, size=(5, 5))  # valores aleatórios inteiros e matriz 5x5

# Posiciona o tesouro em uma posição aleatória
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

# Função para mostrar o mapa
def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()  # Cria uma cópia da matriz original
    linha, coluna = posicao_jogador  # Posição atual do jogador
    mapa_com_jogador[linha, coluna] = -1  # Marca a posição do jogador com -1

    mapa_com_jogador_str = np.char.mod('%2d', mapa_com_jogador)  # Converte números para string
    mapa_com_jogador_str[mapa_com_jogador == -1] = 'P'  # Substitui o número -1 por 'P'

    print("\nMapa Atual:")
    for linha in mapa_com_jogador_str:
        print(" ".join(linha))

# Fluxo principal
while True:
    mostrar_mapa(mapa, posicao_jogador)

    direcao = input("Direção que deseja mover? (cima, baixo, esquerda, direita) ").strip().lower()
    movimentos = {
        "cima": (-1, 0),
        "baixo": (1, 0),
        "esquerda": (0, -1),
        "direita": (0, 1),
        "c": (-1, 0),
        "b": (1, 0),
        "e": (0, -1),
        "d": (0, 1)
    }

    if direcao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcao][0], posicao_jogador[1] + movimentos[direcao][1])
    else:
        print("Direção inválida! Tente novamente.")
        continue  # Reinicia o loop para permitir nova tentativa

    # Verifica se a nova posição é válida
    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0 <= nova_posicao[1] < mapa.shape[1]):
        print("Movimento fora dos limites. Tente novamente.")
        continue  # Reinicia o loop para impedir movimentos fora do mapa

    posicao_jogador = nova_posicao
    pontuacao += 1

    # Verifica se o jogador encontrou o tesouro
    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n\n==== Parabéns! Você encontrou o tesouro! ====")
        print(f"Pontuação final: {pontuacao}")
        print(f"O tesouro estava na posição {(tesouro_linha, tesouro_coluna)}")
        break
