__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

from utils.input_read import read_n_value
from utils.backtracking import backtracking

def main(input_file):
    """
    Main function to solve the N-Queens problem using backtracking.

    Args:
        input_file (str): The path to the input file containing the value of N.

    The function reads the value of N from the input file, initializes the domains
    for each row, and attempts to find a solution using the backtracking algorithm.
    If a solution is found, it prints the solution; otherwise, it prints that no
    solution was found.
    """
     
    n = read_n_value(input_file)

    initial_positions = list(range(n))

    domains = {}
    for row in range(n):
        init_col = initial_positions[row]
        # Preference is for initial position
        domains[row] = [init_col] + [c for c in range(n) if c != init_col]

    queen_positions = {}

    found_solution, solution = backtracking(queen_positions, domains, n)
    if found_solution:
        print(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main("input.txt")