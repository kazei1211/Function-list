#import function from utils folder

from utils.utils import *

# A +B
if __name__ == '__main__':
    a, b = 2, 24
    c, d = 3.14, 0.25

    result_float = adder_float(a, b)
    result_int = adder_int(a, b)

    print(f'A+B (int) : {a} + {b} = {result_int}')
    print(f'A+B (float) : {c} + {d} = {result_float}')
# compare A,B
    compare_two_numbers_int(a, b)
# list

nums = [1,3,5,7,9,8,6,10]

print(nums)
print(nums)

nums.append(24)
nums.remove(3)

for i in range(len(nums)):
    print(f'nums[',i,'] = ',nums[i])
