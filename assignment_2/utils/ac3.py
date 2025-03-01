__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

from collections import deque
from utils.heuristics import constraints_check

def remove_inconsistent_values(domains, Xi, Xj):
    """
    'Remove' the domain of Xi to ensure arc consistency with Xj.
    
    Args:
        domains (dict): Mapping row -> list of possible columns.
        Xi (int): A row variable.
        Xj (int): Another row variable.
    
    Returns:
        bool: True if any value was removed from Xi's domain, False otherwise.
    """
    removed = False
    for x in domains[Xi][:]: 
        # If there's no y in Xj's domain that can coexist with x in Xi's domain, remove x
        if not any(not constraints_check(Xi, x, Xj, y) for y in domains[Xj]):
            domains[Xi].remove(x)
            removed = True
    return removed

def ac3(domains, n):
    """
    AC3 algorithm to enforce arc consistency across all pairs of rows (Xi, Xj).
    
    Args:
        domains (dict): Mapping row -> list of possible columns.
        n (int): The number of rows/queens.
    
    Returns:
        bool: True if arc consistency is maintained (no domain is empty),
              False if any domain is pruned to empty.
    """
    queue = deque()
    # Initialize queue with all arcs (Xi, Xj) for i != j
    for i in range(n):
        for j in range(n):
            if i != j:
                queue.append((i, j))
    
    while queue:
        Xi, Xj = queue.popleft()
        if remove_inconsistent_values(domains, Xi, Xj):
            # If domain of Xi is empty, no solution possible
            if not domains[Xi]:
                return False
            # If Xi's domain changed, re-check neighbors (Xk, Xi)
            for Xk in range(n):
                if Xk != Xi and Xk != Xj:
                    queue.append((Xk, Xi))
    return True