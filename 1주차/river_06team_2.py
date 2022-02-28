sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    sentence=" ".join(sentence.split(" ")[::-1])
    return sentence

print(reverse_sentence(sentence))