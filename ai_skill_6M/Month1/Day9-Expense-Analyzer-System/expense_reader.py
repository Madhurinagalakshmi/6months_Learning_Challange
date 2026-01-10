import os
class ExpenseReader:
    def __init__(self,filename):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir,filename)
        self.filename = file_path
    def read_file(self):
        try:
            with open (self.filename,'r') as f:
                nums = {}
                for line in f:
                    if(line.strip()!='\n'):
                        record = line.split(',')
                        try:
                            key = record[0]
                            value = float(record[1].strip())
                            nums[key] = value
                        except Exception :
                            pass
                return nums
        except Exception :
            return {}
        