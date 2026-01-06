#ADD TWO NUMBERS
def add_numbers(a,b):
    return a+b

print(add_numbers(2,3))

# EVEN OR ODD
def is_even(a):
    return a%2==0

print(is_even(5))

# count_vowels(s)
def count_vowels(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] in ('aeiou'):
            count += 1
    return count

print(count_vowels("madhuri"))

#find_max(numbers)
def find_max(numbers):
    if len(numbers)==0:
        return None
    maxi = numbers[0]
    for i in range(len(numbers)):
        if(numbers[i]>maxi):
            maxi = numbers[i]
    return maxi

print(find_max([1,2,3,4]))

#reverse_string(s)

def reverse_string(s):
    reversed = ''
    length = len(s)
    for i in range(length):
        reversed = s[i]+reversed
    return reversed
print(reverse_string("madhuri"))
