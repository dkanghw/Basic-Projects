# Author d.kanghw
# Generate a strong password that consist of
# lowercase, uppercase, symbols, number

import random
import string

# Create password with length of total sum of parameter then randomize the order


def create_password(lower, upper, sym, num):
    password = []
    for _ in range(lower):
        password.append(random.choice(string.ascii_lowercase))
    for _ in range(upper):
        password.append(random.choice(string.ascii_uppercase))
    for _ in range(sym):
        password.append(random.choice(string.punctuation))
    for _ in range(num):
        password.append(random.choice(string.digits))

    random.shuffle(password)
    result = ''.join(password)
    return result


print(create_password(4, 4, 2, 2))
