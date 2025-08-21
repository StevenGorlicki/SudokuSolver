**Run the Sudoku Solver**
File format

Each board file begins with two integers p q (sub‑block rows/cols). The overall size is N = p × q.
Example (standard 9×9 Sudoku): p=3, q=3 → N=9
Grid uses base‑36 symbols: 0 = empty, 1–9, then A=10, B=11, … as needed.
ex
3 3
0 0 0 4 0 0 0 0 0
...

**To Generate Test Files**
in terminal you can do 
# python3 board_generator.py BASE_NAME COUNT p q m

# 5 boards, 9x9 (3x3 blocks), 30 givens each:
python3 board_generator.py Boards/board 5 3 3 30

# 3 boards, 12x12 (3x4 blocks), 35 givens each:
python3 board_generator.py Boards/board 3 3 4 35

**Solve Boards**
# to run our build in demo type:
python3 src/main.py

for a single example board:
python3 src/main.py MAD LCV NOR Difficulty_level/file
# specifically
python3 src/main.py MAD LCV NOR generator_expert/generator_0.txt

This can solve 25x25 boards in <1 minute and 36x36 when modifying the input to allow for upper and lowercase letters (1-Z single character only goes to 35 unique inputs) give it a try!
