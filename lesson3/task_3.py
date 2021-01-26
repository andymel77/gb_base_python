"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    nums_ = [a, b, c]
    nums = sorted(nums_)
    return nums[1] + nums[2]

print(my_func(4, 3, 5))