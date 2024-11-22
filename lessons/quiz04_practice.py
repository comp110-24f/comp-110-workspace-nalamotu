def sum_of_natural_numbers(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)


def sum_of_digits(n: int) -> int:
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


def power(n: int, exp: int) -> int:
    if exp == 0:
        return 1
    else:
        return n * power(n, exp - 1)


def gcd(n1: int, n2: int) -> int:
    if n1 == 0 or n2 == 0:
        return 0
    else:
        div: int = 1
        if n1 % div == 0 and n2 % div == 0:
            div += 1
            return gcd(n1, n2)
        else:
            return div - 1
