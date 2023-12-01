"""This File contains all utility functions/classes used for the challenge"""

from typing import List

class FileHandler():
    """Class that contains all utility functions
    to handle files.
    """

    def txt_to_lst(file_path: str) -> List[str]:
        """Read a txt file and put each line in the file
        as a new element in a list
        
        Args:
            file_path (String): Path to the file you want to read
        
        Returns:
            lines (List[str]): a list where each element was a line in
                               the file.
        """
        file_open = open(file_path, 'r')
        return file_open.readlines()