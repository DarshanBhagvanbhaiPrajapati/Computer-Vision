import string

def is_pangram(sentence):
    alphabet_set = set(string.ascii_lowercase)
    sentence_lower = sentence.lower().replace(" ", "")
    sentence_set = set(sentence_lower)
    return sentence_set >= alphabet_set

input_sentence = input("Enter a sentence to check if it's a pangram: ")
if is_pangram(input_sentence):
    print("The input sentence is a pangram.")
else:
    print("The input sentence is not a pangram.")
