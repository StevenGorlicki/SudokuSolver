import os
import time
import subprocess
import pandas as pd

# CONFIGURATION
PYTHON = "python3"
BOARD_GEN = "./venv/bin/python3 venv/Board_Generator.py"  # Adjust if different
MAIN_SCRIPT = "src/main.py"
BOARD_DIR = "generated_boards"
BASE_NAME = "test_board"
HEURISTICS = [("MRV", "LCV", "FC"), ("MAD", "LCV", "NOR")]
BOARDS_PER_SIZE = 5
SIZES = [(1, 3), (2, 2), (1, 5), (2, 3)]  # (p, q) pairs for 3x3 to 6x6
M = 10  # Initial filled cells

# Ensure board output dir
os.makedirs(BOARD_DIR, exist_ok=True)

results = []

# Loop over all sizes
for p, q in SIZES:
    N = p * q
    for i in range(BOARDS_PER_SIZE):
        board_filename = f"{BASE_NAME}_{N}x{N}_{i}.txt"
        board_path = os.path.join(BOARD_DIR, board_filename)

        # Generate board
        subprocess.run([
            PYTHON, "board_generator.py",
            os.path.join(BOARD_DIR, f"{BASE_NAME}_{N}x{N}"),
            "1", str(p), str(q), str(M)
        ], check=True)

        # Test each heuristic combo
        for var_h, val_h, cc in HEURISTICS:
            cmd = [PYTHON, MAIN_SCRIPT, var_h, val_h, cc, board_path]
            print(f"Running: {' '.join(cmd)}")
            start = time.time()
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            end = time.time()
            elapsed = round(end - start, 4)

            # Parse stdout
            output = result.stdout
            trail_pushes = None
            backtracks = None
            solved = "Failed to find a solution" not in output

            for line in output.split("\n"):
                if "Trail Pushes:" in line:
                    trail_pushes = int(line.split(":")[1].strip())
                elif "Backtracks:" in line:
                    backtracks = int(line.split(":")[1].strip())

            results.append({
                "Board": f"{N}x{N}_{i}",
                "Size": f"{N}x{N}",
                "Var Heuristic": var_h,
                "Val Heuristic": val_h,
                "Consistency": cc,
                "Solved": solved,
                "Time (s)": elapsed,
                "Trail Pushes": trail_pushes,
                "Backtracks": backtracks
            })

# Output DataFrame
df = pd.DataFrame(results)
print(df.to_string(index=False))
df.to_csv("sudoku_solver_results.csv", index=False)
