__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

def read_n_value(file_path):
    """
    Reads the value of n from the input file.
    
    Args:
        file_path (str): The path to the input file.
        
    Returns:
        int: The value of n.
    """
    with open(file_path, 'r') as file:
        line = file.readline().strip()
        n = int(line)
        if 10 <= n <= 1000:
            return n
        else:
            raise ValueError("The value of n must be between 10 and 1000.")