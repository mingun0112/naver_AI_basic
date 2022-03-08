num_list=[1,5,7,15,16,22,28,29]

def get_odd_num(num_list):
    for i in num_list:
        if i %2 ==0:
            num_list.remove(i)
    return num_list
print(get_odd_num(num_list))

sentence="way a is there will a is there where"

def reverse_sentence(sentence):
    sentenceList=sentence.split(" ")    
    sentenceList.reverse()
    sentence=" ".join(sentenceList)
    return sentence
print(reverse_sentence(sentence))
