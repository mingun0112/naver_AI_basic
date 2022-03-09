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

import copy
dict_first={'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second={'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first,dict_second):
    temp=copy.deepcopy(dict_first)
    temp.update(dict_second)
    for i in dict_first:
        if i in dict_second:
            temp[i]=dict_first[i]+dict_second[i]
    print(temp)

merge_dict(dict_first,dict_second)

import re

def find_string(inputs):
    ans_list = []
    temp_str=re.sub(r"[0-9]+", " ", inputs)
    ans_list=temp_str.split()
    return ans_list
inputs="cat32dog16cow5"
string_list=find_string(inputs)
print(string_list)

