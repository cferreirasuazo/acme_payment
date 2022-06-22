
class InvalidRecordFormatError(Exception):
    def __init__(self, string_record):
        self.message = f"!! Invalid String Record Format: {string_record}"
        super().__init__(self.message)

class InvalidDayPaymentFormatError(Exception):
    def __init__(self, day_payment_string):
        self.message = f"!! Invalid Day Payment Format: {day_payment_string}"
        super().__init__(self.message)
        


