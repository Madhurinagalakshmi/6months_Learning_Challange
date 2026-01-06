def read_numbers_from_file(sample):
    nums = []
    file = open(sample,'r')
    for line in file:
        if(line!='\n'):
            nums.append(int(line))
    file.close()
    return nums
if __name__=="__main__":
    pass