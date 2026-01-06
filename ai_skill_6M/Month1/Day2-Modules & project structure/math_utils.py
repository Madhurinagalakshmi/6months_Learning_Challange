def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def average(numbers):
    sum = 0
    if(len(numbers)==0):
        return 0
    for n in numbers:
        sum += n
    return sum/len(numbers)
if __name__ == "__main__":
    add(10, 20)
    average([10, 20, 30])
    subtract(5,2)