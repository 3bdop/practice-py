def is_armstrong_number(number):
    s = 0
    n_t_s = str(number)
    digits = len(n_t_s)
    for i in range(digits):
        s += int(n_t_s[i])**digits

    if s == number:
        return True
    return False
