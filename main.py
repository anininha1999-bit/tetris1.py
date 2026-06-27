import board
from keyboard import read_with_timeout


def main():
    mboard = board.create(20, 10)
    stone = (0, 4)
    while True:
        board.draw(mboard, stone)
        key = read_with_timeout(1.0)
        match key:
            case "l":
                stone = (stone[0], min(9, stone[1] + 1))
            case "h":
                stone = (stone[0], max(0, stone[1] - 1))
            case None:
                # timeout
                stone = (stone[0]+1, stone[1])
                if stone[0] == 20:
                    # fechando o programa,
                    # você deve detectar colisões com outros blocos
                    # fixados ou o fundo do tabuleiro
                    break
            case _:
                break


main()
