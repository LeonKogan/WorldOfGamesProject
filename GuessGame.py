from time import sleep


def _generate_number(difficulty):
    import random
    secret_number = int(random.uniform(1, difficulty))
    return secret_number


def _get_guess_from_user(difficulty):
    number = int(input(f"You need to guess a number between 1 to {difficulty}: "))
    return number


def _compare_results(secret_number, number):
    if secret_number == number:
        return True


def play(difficulty):
    secret_number = _generate_number(difficulty)

    print("Generating a Number...")
    sleep(2)
    print("YES!! The number is ready. Now it's Your turn")
    sleep(1)
    number = _get_guess_from_user(difficulty)
    if _compare_results(secret_number=secret_number, number=number):
        return True
    else:
        return False
