#mini logic phase
def word_frequency(sentence):
    sentence = sentence.lower()
    freq = {}
    for word in sentence.split(' '):
        if word in freq:
            freq[word] = freq[word]+1
        else:
            freq[word] = 1
    for word in freq:
        print(word,":",freq[word])
word_frequency("AI is the future and AI is powerful")
