import time
import math
start_time = time.time()


def largest_prime_factor(x):
    to_factor = x

    if to_factor % 2 == 0:
        last_factor = 2
        to_factor /= 2
        while to_factor % 2 == 0:
            to_factor /= 2
    else:
        last_factor = 1

    test_factor = 3
    max_factor = int(math.sqrt(to_factor))

    while to_factor > 1 and max_factor <= max_factor:
        if to_factor % test_factor == 0:
            to_factor /= test_factor
            last_factor = test_factor
            while to_factor % test_factor == 0:
                to_factor /= test_factor
            max_factor = int(math.sqrt(to_factor))
        test_factor += 2

    if to_factor == 1:
        return last_factor
    else:
        return to_factor


sol = largest_prime_factor(600851475143)
print 'solution:', sol

stop_time = time.time()
print 'time:', stop_time - start_time
