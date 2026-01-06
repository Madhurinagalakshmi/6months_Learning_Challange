import marks_reader as m
class MarksAnalyzer:
    def find_average(nums):
        if(len(nums)==0):
            return 0
        else:
            sum = 0
            for n in nums.keys():
                sum += nums[n]
            return int(sum/len(nums))
    def find_highest(nums):
        if(len(nums)==0):
            return None
        maxi = 0
        for n in nums.values():
            if(n>maxi):
                maxi = n
        return maxi
    def find_lowest(nums):
        if(len(nums)==0):
            return None
        mini = 100
        for n in nums.values():
            if(n<mini):
                mini = n
        return mini
    def count(nums):
        return len(nums)