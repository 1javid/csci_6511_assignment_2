__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

from utils.heuristics import *
from utils.ac3 import *

import copy

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
    if len(queen_positions) == n:
        solution = [queen_positions[i] for i in range(n)]
        return True, solution

    row = mrv(domains, queen_positions)
    unassigned_rows = [r for r in domains if r not in queen_positions]
    new_domain = lcv(domains, row, unassigned_rows)

    for value in new_domain:
        domains_copy = copy.deepcopy(domains)
        
        queen_positions[row] = value
        domains[row] = [value]

        if ac3(domains, n):
            found, sol = backtracking(queen_positions, domains, n)
            if found:
                return True, sol
        
        # Restore all domains to their state before this assignment
        domains = domains_copy
        queen_positions.pop(row, None)

    return False, []