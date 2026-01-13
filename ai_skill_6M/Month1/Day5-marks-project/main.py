import marks_analyzer as ma
import marks_reader as mr

obj = mr.MarksReader("marks.txt")
nums = obj.read_marks()
avg = ma.MarksAnalyzer.find_average(nums)
cnt = ma.MarksAnalyzer.count(nums)
high = ma.MarksAnalyzer.find_highest(nums)
low = ma.MarksAnalyzer.find_lowest(nums)
med = ma.MarksAnalyzer.find_median(nums)
print(avg)
print(cnt)
print(high)
print(low)
print(med)