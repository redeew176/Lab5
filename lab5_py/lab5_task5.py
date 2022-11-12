def get_random_password(n=8) -> str:
    from random import randint
    from random import sample
    from random import shuffle
    n_str_upper = randint(1, n-2)
    n_str_lower = randint(1, n-n_str_upper-1)
    n_str_digit = randint(1, n - n_str_upper-n_str_lower)
    str_upper = sample(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), n_str_upper)
    str_lower = sample(list('abcdefghijklmnopqrstuvwxyz'), n_str_lower)
    str_digit = sample(list('0123456789'), n_str_digit)

    password = str_upper+str_lower+str_digit
    shuffle(password)

    return ("".join(password))


print(get_random_password())
