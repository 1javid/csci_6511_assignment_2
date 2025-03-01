__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

from utils.heuristics import *
from utils.ac3 import *

def backtracking(queen_positions, domains, n):
    """
    Backtracking search for N-Queens using MRV, tie-breaking by row index,
    LCV ordering, and AC3 for constraint propagation.
    
    Args:
        queen_positions (dict): Maps row -> assigned column for rows already assigned.
        domains (dict): Maps row -> list of possible columns.
        n (int): Number of queens/rows.
    
    Returns:
        (bool, list):
            bool - True if a solution is found, False otherwise.
            list - The solution (row -> column) if found, else empty.
    """
    # If all rows have been assigned, we've found a solution.
    if len(queen_positions) == n:
        solution = [queen_positions[i] for i in range(n)]
        return True, solution

    # 1. MRV: select the row with the smallest domain
    row = mrv(domains, queen_positions)

    # 2. LCV: sort row's domain by how few conflicts each value causes in the domains of other unassigned rows
    unassigned_rows = [r for r in domains if r not in queen_positions]
    new_domain = lcv(domains, row, unassigned_rows)

    for value in new_domain:
        # Tentatively assign
        queen_positions[row] = value
        old_domain = domains[row]
        domains[row] = [value]

        found, sol = False, []
        if ac3(domains, n):
            found, sol = backtracking(queen_positions, domains, n)
        if found:
            return True, sol

        # Backtrack
        queen_positions.pop(row, None)
        domains[row] = old_domain

    return False, []