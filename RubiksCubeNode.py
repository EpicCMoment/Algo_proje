from RubiksCube import *
from typing import List


class RubiksCubeNode:

    def __init__(self, cube: RubiksCube, depth: int, rotation: str, path: List[str]) -> None:
        self.cube = cube
        self.depth = depth
        self.path = copy.deepcopy(path)

        if path != '':
            self.path.insert(0, rotation)
