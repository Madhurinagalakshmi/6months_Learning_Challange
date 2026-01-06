def count_vowels(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] in ('aeiou'):
            count += 1
    return count

def reverse_string(s):
    reversed = ''
    length = len(s)
    for i in range(length):
        reversed = s[i]+reversed
    return reversed

def word_frequency(sentence):
    sentence = sentence.lower()
    freq = {}
    for word in sentence.split(' '):
        if word in freq:
            freq[word] = freq[word]+1
        else:
            freq[word] = 1
    return freq
if __name__ == "__main__":
    count_vowels("madhuri")
    word_frequency("i am madhuri, i am ramya")
    reverse_string("madhuri")
