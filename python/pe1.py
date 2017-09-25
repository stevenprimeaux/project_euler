import time
start_time = time.time()



def sum_multiples(divisor, target):
    n = (target - 1) // divisor
    sum_multiples = divisor * ((n * (n + 1)) / 2)
    return sum_multiples

sol = sum_multiples(3, 1000) + sum_multiples(5, 1000) - sum_multiples(15, 1000)
print 'solution:', sol



stop_time = time.time()
print 'time:', stop_time - start_time
