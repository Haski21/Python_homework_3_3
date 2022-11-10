"""
Дана последовательность из N чисел. Найти в ней два самых маленьких числа.
Последовательность можно сформировать с помощью функции randint()
Вариант 1.
from random import randint
nums = []
for _ in range(10):
    nums.append(randint(1, 100))  ## Случайное число от 1 до 100 включительно
не используя min(), sort()
"""  
from random import randint
# nums = [10, 2, 1, 5, 2,4]
nums = []
# for _ in range(10):
#     nums.append(randint(1, 100))
print(*nums)
    
var_one = var_two = 101
index = 0
for _ in range(len(nums)):
    if var_one > nums[_]:
        var_one = nums[_]
        index = _
nums.pop(index)
for _ in range(len(nums)):
    if var_two > nums[_]:
        var_two = nums[_]
        index = _
# nums.pop(index)
print(f'Two min number are: {var_one} and {var_two}')
# print(*nums)