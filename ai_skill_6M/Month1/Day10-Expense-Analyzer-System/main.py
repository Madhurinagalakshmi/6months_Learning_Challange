import expense_reader as er
import expense_analyzer as ea
import os

filename = 'expenses.txt'
reader_obj = er.ExpenseReader(filename)
data = reader_obj.read_file()
print(data)
analyzer_obj = ea.ExpenseAnalayzer(data)
highest = analyzer_obj.find_highest()
lowest = analyzer_obj.find_lowest()
total = analyzer_obj.find_total()
average = analyzer_obj.find_average()

print(highest)
print(lowest)
print(total)
