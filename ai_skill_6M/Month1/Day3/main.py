from data_utils_safe import read_numbers_safely
if __name__=='__main__':
    nums = read_numbers_safely('numbers.txt')
    print(nums)
    print("Average:", sum(nums)/len(nums) if nums else 0)

'''
1.possible crashes possible in day 2?
  if does not exist,if the line cosists of non numeric characters, if did not closed properly
2.How does with open() prevent bugs?
  with open is helpful and prevent bugs by its properties like automaticaly closing files which could cause potential errors if forgot to close,
3.Difference between ValueError and FileNotFoundError?
  value error means if the value can not be created usong opeations we made for eg: converting string to int or float...
  filenotfound error means if the file does not exist in the same directory or standard libraries, we can resolve it by adding its path in env variables or sys.path
4.When should you NOT catch an exception?
  if the code has bugs , outofmemory or stackoverflow error
'''