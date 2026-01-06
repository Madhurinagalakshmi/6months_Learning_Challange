#DEBUGGING EXERCISE
def average(nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum / len(nums)

print(average([]))


#ANSWER

def average(nums):
    if len(nums)==0 :   # Bug: dividing by zero when list is empty
        return 0
    sum = 0
    for i in nums:
        sum = sum + i
    return sum / len(nums)

print(average([]))
