import numpy as np

# Mapa será 5x5
mapa = np.random.randint(1,10, size=(5,5))

# Posiciona o tesouro em uma posição aleatória
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posição_do_jogador = (0, 0)

pontuação = 0
