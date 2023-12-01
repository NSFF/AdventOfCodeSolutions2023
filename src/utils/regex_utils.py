"""This File contains all utility functions/classes used for the challenge"""

from typing import List

class RegexUtils():
    """Class that contains all utility functions
    to handle files.
    """

    def lst_words2regex(word_lst: List[str], 
                        extra_regex_prefix: str) -> str:
        """Convert a list of words into the right regex format
        to be used in a re.findAll() to exclude everything
        except the words listed in the list.
        
        Args:
            word_lst (List[String]): List of words
        
        Returns:
            regex_words (String): the correct raw regex string
        """
        regex_words = r""

        for word in word_lst:
            regex_words = regex_words + "|" + word
        regex_words = "(?=(" + extra_regex_prefix + regex_words + "))"
        return regex_words