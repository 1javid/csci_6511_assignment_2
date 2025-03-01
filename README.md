# N-Queens Problem Solver

This project solves the N-Queens problem using CSP -> backtracking, Minimum Remaining Values (MRV), Least Constraining Value (LCV), and Arc Consistency (AC3).

## Problem Description
The N-Queens problem involves placing N queens on an N×N chessboard such that no two queens threaten each other. This means no two queens can be in the same row, column, or diagonal.

## Implementation
The solution uses the following components:

- `main.py`: Contains the main function to solve the N-Queens problem using backtracking.
- `input_read.py`: Helper function for reading input.
- `heuristics.py`: Helper functions for heuristic calculations (MRV, LCV, constraints check).
- `ac3.py`: Helper functions for enforcing arc consistency (AC3).
- `backtracking.py`: Helper function for the backtracking algorithm.
- `unit_test.py`: Unit test cases for various components of the solution.


## Input Format
The input is provided via a text file named `input.txt` which contains a single integer N (10 ≤ N ≤ 1000) representing the size of the chessboard and the number of queens.

## Algorithm Details
1. **Backtracking**: The main algorithm used to explore possible placements of queens.
2. **MRV (Minimum Remaining Values)**: Heuristic to select the row with the smallest domain.
3. **LCV (Least Constraining Value)**: Heuristic to sort the domain of a row by how few conflicts each value causes.
4. **AC3 (Arc Consistency 3)**: Algorithm to enforce arc consistency across all pairs of rows.

## Running the Program
To run the program, execute the `main.py` file:
```sh
python main.py
```

## Testing
Run the unit tests with:
```sh
python -m unittest unit_test.py
```