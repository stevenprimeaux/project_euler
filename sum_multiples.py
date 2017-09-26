def sum_multiples(divisor, upper_limit):
    n = (upper_limit - 1) // divisor
    sum_multiples = divisor * ((n * (n + 1)) / 2)
    return sum_multiples
