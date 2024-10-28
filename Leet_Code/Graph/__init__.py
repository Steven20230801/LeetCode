from typing import List, Sequence, Union


def draw(maze: Sequence[Sequence[Union[str, int]]]) -> None:
    for row in maze:
        print("".join(map(str, row)))
