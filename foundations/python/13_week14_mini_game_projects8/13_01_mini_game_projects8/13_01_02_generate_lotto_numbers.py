import random

def generate_lotto_numbers():
    lotto_numbers = random.sample(range(1,46),6)

    lotto_numbers.sort(reverse = True)
    return lotto_numbers

print("Generated lotto numbers:", generate_lotto_numbers())
