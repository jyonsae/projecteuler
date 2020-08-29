my_number = 600851475143
largestNumber = 0


def get_factor(number):
    num_arr = []
    for i in range(1, number + 1):
        if number % i == 0:
            num_arr.append(i)

    return num_arr


def is_prime(number):
    return len(get_factor(number)) == 2


for i in get_factor(my_number):
    if is_prime(i) and i > largestNumber:
        largestNumber = i

print(largestNumber)
