count = 2000000
sum_of_numbers = 0
prime_arr = []
i = 0


def is_prime(n):
    if n > 1:
        for j in range(2, n//2):
            if (n % j) == 0:
                return False
            else:
                return True
    else:
        return False


while i < count:
    i += 1
    if is_prime(i):
        sum_of_numbers += i

print(sum_of_numbers)
