import number_file_reader as n;

file = 'numbers.txt'
obj = n.NumberReader(file)
nums = obj.read_numbers()
avg = obj.find_average()
print(nums)
print(avg)