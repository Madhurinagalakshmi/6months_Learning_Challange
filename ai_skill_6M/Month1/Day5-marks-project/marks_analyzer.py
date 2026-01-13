import marks_reader as m
import math
class MarksAnalyzer:
    def find_average(nums):
        if(len(nums)==0):
            return 0
        else:
            total = 0
            for n in nums.keys():
                total += nums[n]
            return int(total/len(nums))
    def find_highest(nums):
        if(len(nums)==0):
            return None
        maxi = -10000
        for n in nums.values():
            if(n>maxi):
                maxi = n
        return maxi
    def find_lowest(nums):
        if(len(nums)==0):
            return None
        mini = 100000
        for n in nums.values():
            if(n<mini):
                mini = n
        return mini
    def count(nums):
        return len(nums)
    def find_median(nums):
        length = len(nums)
        if(len(nums)==0):
            return None
        numbers = []
        for k in nums.keys():
            numbers.append(nums[k])
        numbers.sort()
        if(length%2!=0):
            return numbers[length/2]
        else:
            mid = numbers[int(length/2)]+numbers[int(length/2+1)]
            return mid/2