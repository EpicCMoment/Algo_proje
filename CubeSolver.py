from RubiksCubeNode import *
from typing import *

call_list: List = []


def prepare_call_list(cube: RubiksCube):
    call_list.append(cube.back_cw)
    call_list.append(cube.back_ccw)

    call_list.append(cube.front_cw)
    call_list.append(cube.front_ccw)

    call_list.append(cube.left_cw)
    call_list.append(cube.left_ccw)

    call_list.append(cube.right_cw)
    call_list.append(cube.right_ccw)

    call_list.append(cube.up_cw)
    call_list.append(cube.up_ccw)

    call_list.append(cube.down_cw)
    call_list.append(cube.down_ccw)


def Solve(target: RubiksCube) -> RubiksCubeNode:
    root_state = RubiksCubeNode(RubiksCube(), 0, '', [])

    visited = {}

    frontier: List[RubiksCubeNode] = [root_state]

    while len(frontier) != 0:

        current_node: RubiksCubeNode = frontier.pop(0)

        visited[current_node] = 1

        # if this cube is in a solved state
        if is_same_state(current_node.cube, target):
            return current_node

        # if maximum search depth is reached
        if current_node.depth == 20:
            continue

        neighbors = [
            RubiksCubeNode(current_node.cube.front_cw(), current_node.depth + 1, 'Front CCW', current_node.path),
            RubiksCubeNode(current_node.cube.front_ccw(), current_node.depth + 1, 'Front CW', current_node.path),
            RubiksCubeNode(current_node.cube.back_cw(), current_node.depth + 1, 'Back CCW', current_node.path),
            RubiksCubeNode(current_node.cube.back_ccw(), current_node.depth + 1, 'Back CW', current_node.path),
            RubiksCubeNode(current_node.cube.up_cw(), current_node.depth + 1, 'Up CCW', current_node.path),
            RubiksCubeNode(current_node.cube.up_ccw(), current_node.depth + 1, 'Up CW', current_node.path),
            RubiksCubeNode(current_node.cube.down_cw(), current_node.depth + 1, 'Down CCW', current_node.path),
            RubiksCubeNode(current_node.cube.down_ccw(), current_node.depth + 1, 'Down CW', current_node.path),
            RubiksCubeNode(current_node.cube.left_cw(), current_node.depth + 1, 'Left CCW', current_node.path),
            RubiksCubeNode(current_node.cube.left_ccw(), current_node.depth + 1, 'Left CW', current_node.path),
            RubiksCubeNode(current_node.cube.right_cw(), current_node.depth + 1, 'Right CCW', current_node.path),
            RubiksCubeNode(current_node.cube.right_ccw(), current_node.depth + 1, 'Right CW', current_node.path)
        ]

        for n in neighbors:
            if visited.get(n) is None:
                frontier.append(n)
