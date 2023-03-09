import traceback

from typing import List
from src.config import delimiters
from src.exceptions.stringcalculatorexceptions import *


class StringCalculator:
    """
    A String calculator class to sum numbers in the input string.

    Methods
    -------
    Add(numbers: str):
        Return the sum of numbers in the string
    checkNegativeNumbers(numbers: List):
        Checks for the negative numbers in the numbers list and raise exception
    parseStringToNumbers(numbers: str):
        Return the list of numbers in the string after removing the delimiters
    replaceAllDelimitersToOne(numbers: str, all_delimiters: List):
        Replace and return the list of characters between delimiters
    containsCustomDelimiter(numbers: str)
        Checks if the string contains custom delimiter
    extractDelimiters(delimiter_string: str)
        Extracts the multiple/single variable length delimiters from the delimiter string
    containsNewLineAtEnd(cls, numbers: str)
        Checks if the string contains new line character at end
    """
    def __init__(self):
        pass

    @classmethod
    def Add(cls, numbers: str) -> int:
        """
        Return the sum of numbers in the string

        Parameters
        ----------
        numbers : str
        """
        try:
            if not numbers.strip():
                return 0
            parsed_numbers = StringCalculator.parseStringToNumbers(numbers)
            StringCalculator.checkNegativeNumbers(parsed_numbers)
            return sum([number for number in parsed_numbers if number <= 1000])
        except ValueError as e:
            print("Error in changing string to integer", traceback.format_exc())
            raise e
        except TypeError as e:
            print("Error in changing string to integer", traceback.format_exc())
            raise e

    @classmethod
    def checkNegativeNumbers(cls, numbers: List) -> None:
        """
        Checks for the negative numbers in the numbers list and raise exception

        Parameters
        ----------
        numbers : str
        """
        negative_numbers = [number for number in numbers if number < 0]
        if len(negative_numbers) > 0:
            raise NegativeNumbersException([str(i) for i in negative_numbers])

    @classmethod
    def parseStringToNumbers(cls, numbers: str) -> List:
        """
        Return the list of numbers in the string after removing the delimiters

        Parameters
        ----------
        numbers : str
        """
        if StringCalculator.containsNewLineAtEnd(numbers):
            raise NewLineAtEndException()
        if StringCalculator.containsCustomDelimiter(numbers):
            delimiter_string = numbers[:numbers.find('\n')]
            if len(delimiter_string) > 0:
                custom_delimiters = StringCalculator.extractDelimiters(delimiter_string)
                numbers = numbers.replace(delimiter_string, "")
                # Replace all delimiters with one unique delimiter
                parsed_numbers = [int(i) for i in StringCalculator.replaceAllDelimitersToOne(numbers, custom_delimiters)
                                  if len(i) > 0]
                return parsed_numbers
            else:
                raise DelimiterParsingException()
        else:
            parsed_numbers = [int(i) for i in StringCalculator.replaceAllDelimitersToOne(numbers, delimiters)
                              if len(i) > 0]
        return parsed_numbers

    @classmethod
    def replaceAllDelimitersToOne(cls, numbers: str, all_delimiters: List) -> List:
        """
         Replace and return the list of characters between delimiters

         Parameters
         ----------
         numbers : str
         all_delimiters: List
         """
        change_delimiter = all_delimiters[0]
        for delimiter in all_delimiters[1:]:
            numbers = numbers.replace(delimiter, change_delimiter)
        return numbers.split(change_delimiter)

    @classmethod
    def containsCustomDelimiter(cls, numbers: str) -> bool:
        """
         Checks if the string contains custom delimiter

         Parameters
         ----------
         numbers : str
         """
        return numbers.startswith('/')

    @classmethod
    def extractDelimiters(cls, delimiter_string: str) -> List:
        """
         Extracts the multiple/single variable length delimiters from the delimiter string

         Parameters
         ----------
         delimiter_string : str
         """
        delimiter_string.replace('//', '').replace('[', ']').split(']')
        delimiter_string = [i for i in delimiter_string if len(i) > 0]
        return delimiter_string

    @classmethod
    def containsNewLineAtEnd(cls, numbers: str) -> bool:
        """
         Checks if the string contains new line character at end

         Parameters
         ----------
         numbers : str
         """
        return numbers.endswith('\n')


if __name__ =="__main__":
    print(StringCalculator.Add('1\n2,3'))

