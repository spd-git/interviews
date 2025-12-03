
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

modifiers = {
    "double": 2,
    "triple": 3
}

def find_phone_numbers(input_string):
    phone_numbers = []
    dump = 1
    for word in input_string.split(" "):
        if word in numbers:
            phone_numbers.append(numbers[word] * dump)
            dump = 1
        elif word in modifiers:
            dump = modifiers[word]
    return "".join(phone_numbers)


if __name__ == "__main__":
    sample_input = "one double two triple three double four"
    print(find_phone_numbers(sample_input))