from itertools import groupby


def increment(passwd):
    return increment(passwd[:-1]) + 'a' if passwd[-1] == 'z' \
        else passwd[:-1] + chr(ord(passwd[-1]) + 1)


def correct(passwd):
    return not(any(c in passwd for c in 'iol')) and \
        any(ord(passwd[i]) == ord(passwd[i + 1]) - 1 == ord(passwd[i + 2]) - 2
            for i in range(len(passwd) - 3)) and \
        len([c for c, g in groupby(passwd) if len(list(g)) > 1]) >= 2


def get_next_password(passwd=None):
    if passwd is None:
        with open('input.txt') as data:
            passwd = data.read()

    passwd = increment(passwd)
    while not correct(passwd):
        passwd = increment(passwd)
    return passwd
