import time
start_time = time.time()



def fibonacci_sum(x):
    limit = x
    current_sum = 0
    a = 1
    b = 1
    c = a + b
    while c < limit:
        current_sum += c
        a = b + c
        b = c + a
        c = a + b
    return current_sum

print fibonacci_sum(4000000)



stop_time = time.time()
print 'time:', stop_time - start_time
