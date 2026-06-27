import random
import board
from keyboard import read_with_timeout



QUADRADO = [(0, 0), (1, 0), (0, 1), (1, 1)]
LINHA_H = [(0, 0), (1, 0), (2, 0), (3, 0)]
LINHA_V = [(0, 0), (0, 1), (0, 2), (0, 3)]


def nova_peca():
    tipo = random.randint(0, 1)

    if tipo == 0:
        return {
            "x": 4,
            "y": 0,
            "shape": QUADRADO,
            "tipo": "quadrado"
        }
    else:
        return {
            "x": 3,
            "y": 0,
            "shape": LINHA_H,
            "tipo": "linha"
        }


def movimento_valido(tabuleiro, peca, novo_x, novo_y, novo_shape=None):

    if novo_shape is None:
        novo_shape = peca["shape"]

    for dx, dy in novo_shape:

        x = novo_x + dx
        y = novo_y + dy

        if x < 0 or x >= 10:
            return False

        if y < 0 or y >= 20:
            return False

        if tabuleiro[y][x] == "#":
            return False

    return True


def fixar_peca(tabuleiro, peca):

    for dx, dy in peca["shape"]:

        x = peca["x"] + dx
        y = peca["y"] + dy

        if 0 <= y < 20 and 0 <= x < 10:
            tabuleiro[y][x] = "#"


def limpar_linhas(tabuleiro):

    novas = []

    for linha in tabuleiro:
        if " " in linha:
            novas.append(linha)

    removidas = 20 - len(novas)

    while len(novas) < 20:
        novas.insert(0, [" "] * 10)

    return novas


def girar(peca):

    if peca["tipo"] == "quadrado":
        return peca["shape"]

    if peca["shape"] == LINHA_H:
        return LINHA_V

    return LINHA_H
def main():

    tabuleiro = board.create(20, 10)

    peca = nova_peca()

    while True:

        board.draw(tabuleiro, peca)

        tecla = read_with_timeout(1.0)

        if tecla in ["a", "j"]:

            if movimento_valido(tabuleiro, peca, peca["x"] - 1, peca["y"]):
                peca["x"] -= 1

        elif tecla in ["d", "l"]:

            if movimento_valido(tabuleiro, peca, peca["x"] + 1, peca["y"]):
                peca["x"] += 1

        elif tecla in ["s", "k"]:

            if movimento_valido(tabuleiro, peca, peca["x"], peca["y"] + 1):
                peca["y"] += 1

        elif tecla in ["w", "i"]:

            nova_forma = girar(peca)

            if movimento_valido(
                tabuleiro,
                peca,
                peca["x"],
                peca["y"],
                nova_forma
            ):
                peca["shape"] = nova_forma

        elif tecla is not None:
            break

        if movimento_valido(tabuleiro, peca, peca["x"], peca["y"] + 1):

            peca["y"] += 1

        else:

            fixar_peca(tabuleiro, peca)

            tabuleiro = limpar_linhas(tabuleiro)

            peca = nova_peca()

            if not movimento_valido(
                tabuleiro,
                peca,
                peca["x"],
                peca["y"]
            ):
                print("Game Over!")
                break


main()