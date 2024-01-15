from CubeSolver import *


def main():
    cube_layout = prompt()

    cube = RubiksCube(cube_layout)

    print("\nCube is being solved... Please wait.\n")

    path = Solve(cube).path

    path.pop()

    print(f"To solve the cube:\n{cube}\nYou can apply these rotations:")

    for rot, i in zip(path, range(len(path))):
        print(f'{i + 1}-) {rot}')


color_list = [
    'R',
    'G',
    'B',
    'O',
    'W',
    'Y',
]

face_list = [
    "Front",
    "Back",
    "Top",
    "Bottom",
    "Left",
    "Right"
]


def prompt():
    print("Welcome to the Cube Solver Xtreme")
    print("This program solves any 2x2x2 Rubik's Cube in no time! (not really)")
    print("Go ahead and enter a cube! For more information, type 'help'.")

    faces = []

    face_counter = 0

    while face_counter < len(face_list):

        inp: str = input(f'{face_list[face_counter]} Face => ')

        if inp == "help":
            print_help()
            continue

        parsed_line = inp.strip().upper().split()

        invalid_face = False

        for ch in parsed_line:

            if len(ch) > 1:
                invalid_face = True
                continue

            if ch not in color_list:
                invalid_face = True
                continue

        if invalid_face:
            print("!!!!!! Please provide a valid face layout !!!!!!\n")
            continue

        faces.append(parsed_line)

        print(f'{face_list[face_counter]} Face Layout => {faces[face_counter]}\n')

        face_counter += 1

    return faces


def print_help():
    print("\n****** HELP ******")
    print("You need to provide the cube's faces one by one in the requested order.")
    print("The order of the faces is: ")
    print("1-) Front")
    print("2-) Back")
    print("3-) Top")
    print("4-) Bottom")
    print("5-) Left")
    print("6-) Right\n")
    print("For providing a face, you need to enter 4 characters seperated by a space.")
    print("Each character represents a color and must be uppercase and one of these: W R Y G B O\n")
    print("Example: W R R G  is a valid face with colors =>\nWhite\nRed\nRed")
    print("Green, starting from top left corner of the face and counting clockwise.")
    print("Go ahead and enter a cube!\n")


if __name__ == '__main__':
    main()
