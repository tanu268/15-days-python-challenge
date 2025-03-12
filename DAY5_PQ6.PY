def longest_word_length(sentence):
    return max(len(word) for word in sentence.split())

print(longest_word_length("Python is an amazing language"))