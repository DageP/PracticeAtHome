from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
#10 is the initial value
#It is used as the first argument passed to the function
#3 becomes the second element
print(result)
