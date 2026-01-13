import os
def read_numbers_safely(filename):
        try:
              list_of_numbers = []
              base_dir = os.path.dirname(__file__)
              file_path = os.path.join(base_dir, filename)
              print(file_path)
              with open(file_path,'r') as nums:
                  for line in nums:
                        if(line!='\n'):
                              line = line.strip()
                              try:
                                    int_value = int(line)
                                    list_of_numbers.append(int_value)
                              except ValueError:
                                    pass                        
              return list_of_numbers         
        except FileNotFoundError as e:
              print(e)
              
                          
                          
