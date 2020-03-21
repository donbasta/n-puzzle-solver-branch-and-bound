# n-puzzle-solver-branch-and-bound
Tugas Kecil 3 IF2211 Stima (Algorithm and Strategy)

N-puzzle is a popular game. This program tries to solve this puzzle given its starting state or determines if solution does not exist. To determine whether solution exist or not, inversion counting is used, and to find the solution step-by-step, branch and bound is used. The program is written in python. Currently the value N is fixed for 4 only, but it can be easily modified for general N.

Detailed report can be seen here: [Laporan Tucil](https://docs.google.com/document/d/1hPSwJk3eXp89Q7qDp9cocr--L_ib6IU-cUslqW8HaG8/edit?usp=sharing)

## Running the Program
Execute `[PYTHON_VERSION] main.py` from this folder inside the terminal. For example:

`python3.7 main.py`

The program will prompt you for the file name containing the initial configuration of the puzzle. So before running the program, you have to create a .txt file consisting this initial configuration in the same folder and insert this file's name inside the program.


