import random


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000:
        unique_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(unique_numbers)


lottery_numbers = get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_numbers)
