def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)
    return z2 * 10**(2 * m) + ((z1 - z2 - z0) * 10**m) + z0

# Question 1
result_q1 = karatsuba(4321, 8765)
print(result_q1)
result_q2 = karatsuba(98765432, 12345678)
print(result_q2)
result_q3 = karatsuba(87654321, 87654321)
print(result_q3)

# Question 2
result_q4 = karatsuba(321, 987654)
print(result_q4)
result_q5 = karatsuba(54321, 765)
print(result_q5)
result_q6 = karatsuba(654321, 98765432)
print(result_q6)
