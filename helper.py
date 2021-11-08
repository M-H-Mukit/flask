import random
import string

# generator methods


def generate_random_alphabetical_string(min_length, max_length):
    length_of_string = random.choice(
        range(min_length, max_length))
    return "".join(random.choice(string.ascii_letters) for i in range(length_of_string))


def generate_random_real_number(max_length):
    return random.uniform(-max_length, max_length)


def generate_random_integer(max_length):
    return random.randint(-max_length, max_length)


def generate_random_alphanumeric(min_length, max_length):
    length_of_string = random.choice(
        range(min_length, max_length))
    return "".join(random.choices(string.ascii_letters + string.digits, k=length_of_string))


# checker methods


def is_alphabetical_string(str_obj):
    return str_obj.isalpha()


def is_real_number(str_obj):
    try:
        return float(str_obj)
    except ValueError:
        pass


def is_integer(str_obj):
    try:
        return int(str_obj)
    except ValueError:
        pass
