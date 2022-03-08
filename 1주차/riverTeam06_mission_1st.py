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

score=[(100, 100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    cnt=1
    for i in score:
        print(cnt,"번, 평균",sum(i)/2)
        cnt+=1

get_avg(score)

