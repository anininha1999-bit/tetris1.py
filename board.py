import copy

def create(lines: int, cols: int) -> list[list[str]]:
    return [[" " for _ in range(cols)] for _ in range(lines)]


def draw(tboard, stone) -> None:
    print("\033[2J\033[H", end="")

    mboard = copy.deepcopy(tboard)

    for dx, dy in stone["shape"]:
        x = stone["x"] + dx
        y = stone["y"] + dy

        if 0 <= y < len(mboard) and 0 <= x < len(mboard[0]):
            mboard[y][x] = "#"

    print((len(mboard[0]) + 2) * "-")
    for linha in mboard:
        print("|" + "".join(linha) + "|")
    print((len(mboard[0]) + 2) * "-")
