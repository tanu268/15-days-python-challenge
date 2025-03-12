# Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence

def word_in_sentence(sentence, word):
    return word in sentence.split()

print(word_in_sentence("Python is fun", "Python"))  # True
print(word_in_sentence("Python is fun", "Java"))  # False
