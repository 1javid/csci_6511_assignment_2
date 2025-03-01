__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

import unittest
from utils.input_read import read_n_value
from utils.heuristics import constraints_check, mrv, lcv
from utils.ac3 import remove_inconsistent_values, ac3
from utils.backtracking import backtracking

class TestNQueens(unittest.TestCase):

    def test_read_n_value(self):
        # Create a temporary file with a valid n value
        with open("test_input.txt", "w") as file:
            file.write("15\n")
        self.assertEqual(read_n_value("test_input.txt"), 15)

        # Test with an invalid n value (less than 10)
        with open("test_input_invalid.txt", "w") as file:
            file.write("5\n")
        with self.assertRaises(ValueError):
            read_n_value("test_input_invalid.txt")

        # Test with an invalid n value (greater than 1000)
        with open("test_input_invalid.txt", "w") as file:
            file.write("1001\n")
        with self.assertRaises(ValueError):
            read_n_value("test_input_invalid.txt")

    def test_constraints_check(self):
        self.assertTrue(constraints_check(0, 0, 1, 0))  # Same column
        self.assertTrue(constraints_check(0, 0, 1, 1))  # Same diagonal
        self.assertFalse(constraints_check(0, 0, 1, 2))  # No conflict

    def test_mrv(self):
        domains = {0: [0, 1], 1: [0], 2: [0, 1, 2]}
        queen_positions = {}
        self.assertEqual(mrv(domains, queen_positions), 1)  # Row 1 has the smallest domain

    def test_lcv(self):
        domains = {0: [0, 1], 1: [0, 1], 2: [0, 1, 2]}
        row = 0
        unassigned_rows = [1, 2]
        self.assertEqual(lcv(domains, row, unassigned_rows), [1, 0])  # Value 1 causes fewer conflicts

    def test_remove_inconsistent_values(self):
        domains = {0: [0, 1], 1: [0, 1]}
        self.assertTrue(remove_inconsistent_values(domains, 0, 1))
        self.assertEqual(domains, {0: [1], 1: [0, 1]})

    def test_ac3(self):
        domains = {0: [0, 1], 1: [0, 1], 2: [0, 1, 2]}
        self.assertTrue(ac3(domains, 3))
        self.assertEqual(domains, {0: [0, 1], 1: [0, 1], 2: [0, 1, 2]})

    def test_backtracking(self):
        initial_positions = [0, 1, 2, 3, 4]
        n = len(initial_positions)
        domains = {row: [initial_positions[row]] + [c for c in range(n) if c != initial_positions[row]] for row in range(n)}
        queen_positions = {}
        found_solution, solution = backtracking(queen_positions, domains, n)
        self.assertTrue(found_solution)
        self.assertEqual(len(solution), n)

if __name__ == "__main__":
    unittest.main()