import os
class MarksReader:
    def __init__(self,filename):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir,filename)
        self.filename = file_path
    def read_marks(self):
        try:
            with open(self.filename,'r') as f:
                marks_dict = {}
                for line in f:
                    if(line!='\n'):
                        line_split = line.split(',')
                        try:
                            marks = line_split[1]
                            marks_dict[line_split[0]] = int(marks[:-1])
                        except Exception:
                            pass
                return marks_dict
        except FileNotFoundError:
            return {}
        
   