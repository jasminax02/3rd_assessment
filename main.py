"""
Blackjack
"""
# Provide your solution here


def calculate_score(int1: int, int2: int, int3: int):
    sum_int = int1 + int2 + int3
    if sum_int <= 21:
        return sum_int
    elif sum_int > 21 and (int1 == 11 or int2 == 11 or int3 == 11):
        if (sum_int - 10) > 21:
            return "BUST"
        else:
            return sum_int - 10
    elif sum_int > 21:
        return "BUST"



"""
Even Numbers
"""
# Provide your solution here


def even_positive_numbers(numbers: list) -> list:
    new_list = []
    for x in numbers:
        if x >= 0 and x % 2 == 0:
            new_list.append(x)
    return new_list



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

    print(calculate_score(9,9,9))
    print(calculate_score(2,8,11))
    print(calculate_score(3,8,11))
    print(calculate_score(11,11,11))

    list_a = [1,2,3]
    return_list_a = even_positive_numbers(list_a)
    print(return_list_a)
    list_b = [10,4,5,-5,-3,34,45,67,23,44]
    return_list_b = even_positive_numbers(list_b)
    print(return_list_b)
    list_c = [34,76,35,21,0,-5]
    return_list_c = even_positive_numbers(list_c)
    print(return_list_c)


