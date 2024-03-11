import re
from decimal import Decimal
from typing import Callable

def generator_numbers(text: str):
    pattern = r'-?\d+\.\d+'
    for match in re.finditer(pattern, text):
        yield Decimal(match.group())


def sum_profit(text: str, func: Callable[[str], Decimal]):
    total_income = Decimal('0')
    for decimal_number in func(text):  
        total_income += decimal_number
    return total_income

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")