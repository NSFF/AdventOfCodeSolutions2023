"""This File contains all utility functions/classes used for the challenge"""

from typing import List

class Utils():
    """Class that contains random utility functions
    for the challenges.
    """

    def convert_to_int(lst):
        """
        Converts a list of strings to a list of integers.

        Args:
            lst (list): The list of strings to be converted.

        Returns:
            list: A new list containing the converted integers.
        """
        return [int(x) for x in lst]
