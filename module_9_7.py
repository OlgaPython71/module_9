def is_prime(func):
    def wrapper(*args):
        result_sum = func(*args)
        for i in range(2, result_sum - 1):
            if result_sum % i == 0:
                result_type = "Составное"
                break
            else:
                result_type = "Простое"
        return f'{result_type}, {result_sum}'

    return wrapper

@is_prime
def sum_three(*args):
    sum1 = 0
    for i in args:
        sum1 += i
    return sum1

result = sum_three(2, 3, 6)
print(result)
