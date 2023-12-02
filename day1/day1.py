from typing import List

DIGITS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
}

def find_digits(text: str) -> List[int]:
    text_len = len(text)

    found_digits_in_order = []

    for i in range(len(text)):
        # handle one-character digits
        if text[i].isdigit():
            found_digits_in_order.append(int(text[i]))
        # handle multi-character digits starting at index i
        else:
            for text_digit in DIGITS.keys():
                if text[i : i + len(text_digit)] == text_digit:
                    found_digits_in_order.append(DIGITS[text_digit])

    return found_digits_in_order

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
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        ]

for test_string in test_data:
    print(make_number(test_string))

print(add_up_numbers_in_strings(test_data))


def task():
    with open('input', 'r') as f:
        texts = f.readlines()
    print(add_up_numbers_in_strings(texts))

task()

