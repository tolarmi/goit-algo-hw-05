import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    yield from map(float, numbers)

def sum_profit(text: str, func: Callable):
    total_sum = sum(func(text))
    return total_sum

