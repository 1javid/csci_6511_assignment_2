__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

def constraints_check(i_1, j_1, i_2, j_2):
    """
    Returns True if placing a queen at (i_1, j_1) conflicts with 
    a queen at (i_2, j_2).

    Args:
        i_1 (int): Row index of the first queen.
        j_1 (int): Column index of the first queen.
        i_2 (int): Row index of the second queen.
        j_2 (int): Column index of the second queen.

    Returns:
        bool: True if there is a conflict, False otherwise.
    """
    return (j_1 == j_2) or (abs(j_1 - j_2) == abs(i_1 - i_2))

def mrv(domains, queen_positions):
    """
    Minimum Remaining Values (MRV) heuristic to select the row with the smallest domain.
    
    Args:
        domains (dict): Maps row -> list of possible columns.
        queen_positions (dict): Maps row -> assigned column for rows already assigned.
    
    Returns:
        int: The row with the smallest domain.
    """
    unassigned_rows = [r for r in domains if r not in queen_positions]
    return min(unassigned_rows, key=lambda r: (len(domains[r]), r))

def lcv(domains, row, unassigned_rows):
    """
    Least Constraining Value (LCV) heuristic to sort the domain of a row by how few conflicts each value causes.
    
    Args:
        domains (dict): Maps row -> list of possible columns.
        row (int): The row to sort the domain for.
        unassigned_rows (list): List of unassigned rows.
    
    Returns:
        list: The sorted domain of the row.
    """
    def conflict_count(value):
        count = 0
        for other_row in unassigned_rows:
            if other_row == row:
                continue
            for val in domains[other_row]:
                if constraints_check(row, value, other_row, val):
                    count += 1
        return count

    return sorted(domains[row], key=conflict_count)