class NegativeNumbersException(Exception):
    def __init__(self):
        self.message = f"negatives not allowed- {','.join(negative_numbers)}"
        super().__init__(self.message)


class NewLineAtEndException(Exception):
    def __init__(self):
        self.message = f"New line charater at the end of string"
        super().__init__(self.message)


class DelimiterParsingException(Exception):
    def __init__(self):
        self.message = f"Delimiter parsing failed"
        super().__init__(self.message)