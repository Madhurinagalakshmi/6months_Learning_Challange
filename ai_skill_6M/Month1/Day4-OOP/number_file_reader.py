import os
class NumberReader:
    def __init__(self,filename):
        base_dir  = os.path.dirname(__file__)
        file_path = os.path.join(base_dir,filename)
        self.filename = file_path
    def read_numbers(self):
        try:
            with open(self.filename,'r') as f:
                numbers = []
                for line in f:
                    if (line!='\n'):
                        try:
                            intform = int(line)
                            numbers.append(intform)
                        except ValueError:
                            pass
                return numbers
        except FileNotFoundError as e:
            return[]
    def find_average(self):
        nums = self.read_numbers()
        if(len(nums)==0):
            return 0
        else :
            sum = 0
            for n in nums:
                sum += n
            return int(sum/len(nums))