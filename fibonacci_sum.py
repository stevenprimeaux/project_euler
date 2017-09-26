def fibonacci_sum(max_term):
    current_sum = 0
    a = 1
    b = 1
    c = a + b
    while c < max_term:
        current_sum += c
        a = b + c
        b = c + a
        c = a + b
    return current_sum
