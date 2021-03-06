import time
import os


def _generate_sequence(difficulty):
    import random
    random_numbers = []
    for number in range(difficulty):
        random_numbers.append(int(random.uniform(1, 101)))
    print(random_numbers)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_numbers


def _get_list_from_user(difficulty):
    user_numbers = []
    print(f"Please Insert {difficulty} numbers")
    for i in range(difficulty):
        i = user_numbers.append(int(input("Import a Number: ")))
    return user_numbers


def _is_list_equal(random_numbers, user_numbers):
    random_numbers.sort()
    user_numbers.sort()
    os.system('cls' if os.name == 'nt' else 'clear')
    if random_numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    random_numbers = _generate_sequence(difficulty)
    user_numbers = _get_list_from_user(difficulty)
    if _is_list_equal(user_numbers=user_numbers, random_numbers=random_numbers):
        return True
    else:
        return False
