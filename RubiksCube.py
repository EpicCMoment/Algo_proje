import copy

# cube face indices
front : int = 0
back : int = 1
top : int = 2
bottom : int = 3
left : int = 4
right : int = 5

class RubiksCube:

    def __init__(self, shape=None) -> None:

        '''
            Shape Order:
                Front
                Back
                Top
                Bottom
                Left
                Right

            A face is represented clock-wise from top left corner.
        '''

        solved_shape = [
            ['R', 'R', 'R', 'R'],  # Front
            ['O', 'O', 'O', 'O'],  # Back
            ['W', 'W', 'W', 'W'],  # Top
            ['Y', 'Y', 'Y', 'Y'],  # Bottom
            ['G', 'G', 'G', 'G'],  # Left
            ['B', 'B', 'B', 'B'],  # Right
        ]

        # if no custom shape is provided, create a solved cube

        if shape is None:
            self.shape = copy.deepcopy(solved_shape)
        else:
            self.shape = copy.deepcopy(shape)


    def __repr__(self) -> str:

        fmt = f'Top: {self.shape[top]}\n'
        fmt += f'Left: {self.shape[left]}\n'
        fmt += f'Front: {self.shape[front]}\n'
        fmt += f'Right: {self.shape[right]}\n'
        fmt += f'Bottom: {self.shape[bottom]}\n'
        fmt += f'Back: {self.shape[back]}\n'

        return fmt

    # fully tested
    def up_cw(self):

        # save top two cubes in the front
        saved_cubes = [self.shape[front][0], self.shape[front][1]]

        self.shape[front][0] = self.shape[right][0]
        self.shape[front][1] = self.shape[right][1]

        self.shape[right][0] = self.shape[back][2]
        self.shape[right][1] = self.shape[back][3]

        self.shape[back][2] = self.shape[left][0]
        self.shape[back][3] = self.shape[left][1]

        self.shape[left][0] = saved_cubes[0]
        self.shape[left][1] = saved_cubes[1]

        s = self.shape[top].pop()
        self.shape[top].insert(0, s)

        return RubiksCube(self.shape)

    def u2(self):
        return self.up_cw().up_cw()

    # fully tested
    def up_ccw(self):

        saved_cubes = [self.shape[front][0], self.shape[front][1]]

        self.shape[front][0] = self.shape[left][0]
        self.shape[front][1] = self.shape[left][1]

        self.shape[left][0] = self.shape[back][2]
        self.shape[left][1] = self.shape[back][3]

        self.shape[back][2] = self.shape[right][0]
        self.shape[back][3] = self.shape[right][1]

        self.shape[right][0] = saved_cubes[0]
        self.shape[right][1] = saved_cubes[1]

        s = self.shape[top].pop(0)
        self.shape[top].append(s)

        return RubiksCube(self.shape)

    # fully tested
    def down_cw(self):

        saved_cubes = [self.shape[front][2], self.shape[front][3]]

        self.shape[front][2] = self.shape[left][2]
        self.shape[front][3] = self.shape[left][3]

        self.shape[left][2] = self.shape[back][0]
        self.shape[left][3] = self.shape[back][1]

        self.shape[back][0] = self.shape[right][2]
        self.shape[back][1] = self.shape[right][3]

        self.shape[right][2] = saved_cubes[0]
        self.shape[right][3] = saved_cubes[1]

        s = self.shape[bottom].pop()
        self.shape[bottom].insert(0, s)

        return RubiksCube(self.shape)

    def d2(self):
        return self.down_cw().down_cw()

    # fully tested
    def down_ccw(self):

        saved_cubes = [self.shape[front][2], self.shape[front][3]]

        self.shape[front][2] = self.shape[right][2]
        self.shape[front][3] = self.shape[right][3]

        self.shape[right][2] = self.shape[back][0]
        self.shape[right][3] = self.shape[back][1]

        self.shape[back][0] = self.shape[left][2]
        self.shape[back][1] = self.shape[left][3]

        self.shape[left][2] = saved_cubes[0]
        self.shape[left][3] = saved_cubes[1]


        s = self.shape[bottom].pop(0)
        self.shape[bottom].append(s)

        return RubiksCube(self.shape)

    # fully tested
    def left_cw(self):

        saved_cubes = [self.shape[front][0], self.shape[front][3]]

        self.shape[front][0] = self.shape[top][0]
        self.shape[front][3] = self.shape[top][3]

        self.shape[top][0] = self.shape[back][0]
        self.shape[top][3] = self.shape[back][3]

        self.shape[back][0] = self.shape[bottom][0]
        self.shape[back][3] = self.shape[bottom][3]

        self.shape[bottom][0] = saved_cubes[0]
        self.shape[bottom][3] = saved_cubes[1]

        s = self.shape[left].pop()
        self.shape[left].insert(0, s)

        return RubiksCube(self.shape)

    def l2(self):
        return self.left_cw().left_cw()

    # fully tested
    def left_ccw(self):

        saved_cubes = [self.shape[front][0], self.shape[front][3]]

        self.shape[front][0] = self.shape[bottom][0]
        self.shape[front][3] = self.shape[bottom][3]

        self.shape[bottom][0] = self.shape[back][0]
        self.shape[bottom][3] = self.shape[back][3]

        self.shape[back][0] = self.shape[top][0]
        self.shape[back][3] = self.shape[top][3]

        self.shape[top][0] = saved_cubes[0]
        self.shape[top][3] = saved_cubes[1]

        s = self.shape[left].pop(0)
        self.shape[left].append(s)

        return RubiksCube(self.shape)

    # fully tested
    def right_cw(self):

        saved_cubes = [self.shape[front][1], self.shape[front][2]]

        self.shape[front][1] = self.shape[bottom][1]
        self.shape[front][2] = self.shape[bottom][2]

        self.shape[bottom][1] = self.shape[back][1]
        self.shape[bottom][2] = self.shape[back][2]

        self.shape[back][1] = self.shape[top][1]
        self.shape[back][2] = self.shape[top][2]

        self.shape[top][1] = saved_cubes[0]
        self.shape[top][2] = saved_cubes[1]

        s = self.shape[right].pop()
        self.shape[right].insert(0, s)

        return RubiksCube(self.shape)

    def r2(self):
        return self.right_cw().right_cw()

    # fully tested
    def right_ccw(self):

        saved_cubes = [self.shape[front][1], self.shape[front][2]]

        self.shape[front][1] = self.shape[top][1]
        self.shape[front][2] = self.shape[top][2]

        self.shape[top][1] = self.shape[back][1]
        self.shape[top][2] = self.shape[back][2]

        self.shape[back][1] = self.shape[bottom][1]
        self.shape[back][2] = self.shape[bottom][2]

        self.shape[bottom][1] = saved_cubes[0]
        self.shape[bottom][2] = saved_cubes[1]

        s = self.shape[right].pop(0)
        self.shape[right].append(s)

        return RubiksCube(self.shape)

    # fully tested
    def front_cw(self):

        saved_cubes = [self.shape[top][2], self.shape[top][3]]

        self.shape[top][2] = self.shape[left][1]
        self.shape[top][3] = self.shape[left][2]

        self.shape[left][1] = self.shape[bottom][0]
        self.shape[left][2] = self.shape[bottom][1]

        self.shape[bottom][0] = self.shape[right][3]
        self.shape[bottom][1] = self.shape[right][0]

        self.shape[right][3] = saved_cubes[0]
        self.shape[right][0] = saved_cubes[1]

        s = self.shape[front].pop()
        self.shape[front].insert(0, s)

        return RubiksCube(self.shape)

    def f2(self):
        return self.front_cw().front_cw()

    # fully tested
    def front_ccw(self):

        saved_cubes = [self.shape[top][2], self.shape[top][3]]

        self.shape[top][2] = self.shape[right][0]
        self.shape[top][3] = self.shape[right][3]

        self.shape[right][0] = self.shape[bottom][1]
        self.shape[right][3] = self.shape[bottom][0]

        self.shape[bottom][0] = self.shape[left][1]
        self.shape[bottom][1] = self.shape[left][2]

        self.shape[left][1] = saved_cubes[0]
        self.shape[left][2] = saved_cubes[1]

        s = self.shape[front].pop(0)
        self.shape[front].append(s)

        return RubiksCube(self.shape)

    # fully tested
    def back_cw(self):

        saved_cubes = [self.shape[top][0], self.shape[top][1]]

        self.shape[top][0] = self.shape[right][1]
        self.shape[top][1] = self.shape[right][2]

        self.shape[right][1] = self.shape[bottom][2]
        self.shape[right][2] = self.shape[bottom][3]

        self.shape[bottom][2] = self.shape[left][3]
        self.shape[bottom][3] = self.shape[left][0]

        self.shape[left][0] = saved_cubes[1]
        self.shape[left][3] = saved_cubes[0]

        s = self.shape[back].pop()
        self.shape[back].insert(0, s)

        return RubiksCube(self.shape)

    def b2(self):
        return self.back_cw().back_cw()

    # fully tested
    def back_ccw(self):

        saved_cubes = [self.shape[top][0], self.shape[top][1]]

        self.shape[top][0] = self.shape[left][3]
        self.shape[top][1] = self.shape[left][0]

        self.shape[left][0] = self.shape[bottom][3]
        self.shape[left][3] = self.shape[bottom][2]

        self.shape[bottom][2] = self.shape[right][1]
        self.shape[bottom][3] = self.shape[right][2]

        self.shape[right][1] = saved_cubes[0]
        self.shape[right][2] = saved_cubes[1]

        s = self.shape[back].pop(0)
        self.shape[back].append(s)

        return RubiksCube(self.shape)

    def is_solved(self) -> bool:
        face_color = ''

        # search every face
        for face in self.shape:

            # save face's color for comparison
            face_color = face[0]

            # compare each cubie with the color to determine
            # if the face has the same color for each cubie
            for cubie in face:
                if cubie != face_color:
                    return False

        return True


def is_same_state(c1: RubiksCube, c2: RubiksCube):
    for f1, f2 in zip(c1.shape, c2.shape):

        for c1, c2 in zip(f1, f2):

            if c1 != c2:
                return False

    return True
