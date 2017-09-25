import time
start_time = time.time()



def sum_divisibles(divisor, target):
    n = (target - 1) // divisor
    sum_multiples = divisor * (n * (n + 1)) / 2
    return(sum_multiples)

print 'solution:', sum_divisibles(3, 1000) + sum_divisibles(5, 1000) - sum_divisibles(15, 1000)



stop_time = time.time()
print 'time:', stop_time - start_time
