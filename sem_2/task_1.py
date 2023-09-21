
def num_to_hex(num):
    res = ''
    letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 15: 'E', 16: 'F'}

    while num > 0:
        rest = num % 16
        if rest >= 10:
            res += letters[rest]
        else:
            res += str(rest)
        num //= 16
    return res[::-1]


