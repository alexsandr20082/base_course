def dimapidor(a):
    return(a%3 == 0)
nums = [24,65,23,-32,75]
result = list(map(dimapidor, nums))
print(result)


num1 = [6,7,8,9,10]
num2 = [1,2,3,4,5]
nums_multiply = list(map(dimapidor, num1, num2))
print(nums_multiply)
