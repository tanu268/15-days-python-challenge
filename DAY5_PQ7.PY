#Create a function that takes a sentence as input and returns the sentence in reverse orde

def reverse_sentence(sentence):
    return "".join(sentence.split()[::-1])

print(reverse_sentence("Hello world python"))