import random


def pass_gen(letters_up='', letters_down='', numbers='', special='', num=0):
    rand_list = [*letters_up, *letters_down, *numbers, *special]
    password = []
    for i in range(num):
        password.append(rand_list[random.randint(0, len(rand_list)-1)])

    return ''.join(map(str, password))
