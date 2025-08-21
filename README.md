**Sudoku Solver**  

**File Format**  
-------------
Each board file begins with two integers p q (sub-block rows/cols).  
The overall size is N = p × q.  

Example (standard 9×9 Sudoku):  
p = 3, q = 3 → N = 9  

Grid uses base-36 symbols:  
0 = empty, 1–9, A=10, B=11, ... as needed  


**Generate Test Files**  
-------------------
Use the board generator to create Sudoku boards.  
Syntax:
```
python3 board_generator.py BASE_NAME COUNT p q m
```
Example: 5 boards, 9x9 (3x3 blocks), 30 givens each
```
python3 board_generator.py board_0.txt 5 3 3 30
```
**Solve Boards  **
------------
Run the solver with optional heuristics and a board file.

Default Demo Build
```
python3 src/main.py
```
Run optimally on a specific board
```
python3 src/main.py MAD LCV NOR generator_expert/generator_0.txt
```
**Heuristic Options  **
-----------------
- MRV   → Minimum Remaining Value  
- MAD   → MRV with degree tie-breaker  
- LCV   → Least Constraining Value  
- FC    → Forward Checking  
- NOR   → Norvig’s propagation
- 

**Performance Notes  **
-----------------
- Can solve 25x25 boards in under a minute.  
- 36x36 boards are possible if you extend the symbol set to include upper and lowercase letters (default base-36 only supports 35 unique symbols).  
