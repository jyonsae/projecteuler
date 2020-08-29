my_number = 600851475143


def get_factor(number):
    num_arr = []
    for i in range(1, number + 1):
        if number % i == 0:
            for j in range(1, 10):
                if number % i != 0:
                    num_arr.append(i)

    return num_arr


print(get_factor(50))
