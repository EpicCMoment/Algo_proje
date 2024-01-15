CENG303 - Design and Analysis of Algorithms Term Project

2x2x2 Rubik's Cube Solver

Definition: This program solves a 2x2x2 Rubik's cube by using
graph traversal. When the program is run, it requests number
layouts of each face of a cube, parses these inputs, generates
an array based cube model and solves it.

Algorithm overview: After parsing the input, the program creates
a new, solved cube and assigns this cube as the root of the graph.
After this assignment it generates its neighbor nodes by rotating
the cube with defined methods inside the RubiksCube class. Our
algorithm uses BFS to traverse graph.

**** Running the Program ****

This program is tested in Python 3.11.6 with CPython interpreter.
Later or previous versions could cause unanticipated problems,
so it is advised to run this program with Python 3.11 with CPython.

This program doesn't use any external library.

Instructions:

This program requires user to provide inputs. If you generate a file
like the 'example.txt' file you can pass it directly to the program
with the command given in the 'Automatic Input' section.

Manual Input:

1-) run 'python main.py'

2-) type 'help' and read the instructions

3-) Enjoy (We hope so)


Automatic Input:

1-) run 'python main.py < <cube_layout>' where <cube_layout> is the path
of your file containing the layout of the cube as in the 'example.txt' file

2-) Enjoy (kinda)

Group Members:
Beyhan Kandemir 20050111051
Zehra Inoz 20050111019
Arif Fil 20050111037