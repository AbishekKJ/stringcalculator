import traceback

from typing import List
from src.config import delimiters
from src.exceptions.stringcalculatorexceptions import *


class StringCalculator:

    def __init__(self):
        pass

    @classmethod
    def Add(cls, numbers: str) -> int:
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
    def checkNegativeNumbers(cls, numbers):
        negative_numbers = [number for number in numbers if number < 0]
        if len(negative_numbers) > 0:
            raise NegativeNumbersException([str(i) for i in negative_numbers])

    @classmethod
    def parseStringToNumbers(cls, numbers: str) -> List:
        if StringCalculator.containsNewLineAtEnd(numbers):
            raise NewLineAtEndException()
        parsed_numbers = []
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
    def replaceAllDelimitersToOne(cls, numbers: str, all_delimiters: List) -> str:
        change_delimiter = all_delimiters[0]
        for delimiter in all_delimiters[1:]:
            numbers = numbers.replace(delimiter, change_delimiter)
        return numbers.split(change_delimiter)

    @classmethod
    def containsCustomDelimiter(cls, numbers: str) -> bool:
        return numbers.startswith('/')

    @classmethod
    def extractDelimiters(cls, delimiter_string: str) -> List:
        delimiter_string.replace('//', '').replace('[', ']').split(']')
        delimiter_string = [i for i in delimiter_string if len(i) > 0]
        return delimiter_string

    @classmethod
    def containsNewLineAtEnd(cls, numbers: str) -> bool:
        return numbers.endswith('\n')

if __name__ =="__main__":
    print(StringCalculator.Add('1\n2,3'))

