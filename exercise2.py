import random


def get_numbers_ticket(min, max, quantity):
    is_valid_range = 1 <= min <= max <= 1000
    population_size = max - min + 1
    is_valid_quantity = 0 < quantity <= population_size

    if is_valid_range and is_valid_quantity:
        unique_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(unique_numbers)
    else:
        return []


lottery_numbers = get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(-10, 10, 5)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1000, 1200, 10)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)
