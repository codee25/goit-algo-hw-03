import re


def normalize_phone(phone_number):
    pattern = r"[^0-9\+]"
    replacement = ""
    modified_text = re.sub(pattern, replacement, phone_number)

    if not modified_text or modified_text == '+':
        return modified_text

    if modified_text[0] == '+':
        return modified_text

    if modified_text[0:3] == '380':
        normalized_number = '+' + modified_text

    elif modified_text[0] == '0':
        normalized_number = '+38' + modified_text

    else:
        normalized_number = '+380' + modified_text

    return normalized_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+4912345678",
    "4912345678"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
