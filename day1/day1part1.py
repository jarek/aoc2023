from typing import List

def find_digits(text: str) -> List[int]:
    digits_as_strings = [c for c in text if c.isdigit()]
    return [int(i) for i in digits_as_strings]

def make_number(text: str) -> int:
    digits_in_number = find_digits(text)
    if not digits_in_number:
        raise ValueError("expecting at least one digit in text")
    first_digit = digits_in_number[0]
    last_digit = digits_in_number[-1]
    return first_digit * 10 + last_digit

def add_up_numbers_in_strings(texts: List[str]) -> int:
    numbers = [make_number(text) for text in texts]
    return sum(numbers)


test_data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
        "4t",
        "5c1",
        ]

for test_string in test_data:
    print(make_number(test_string))

print(add_up_numbers_in_strings(test_data))


def task():
    with open('input', 'r') as f:
        texts = f.readlines()
    print(add_up_numbers_in_strings(texts))

task()

