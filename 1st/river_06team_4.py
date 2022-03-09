import copy
dict_first ={'사과':30,'배':15,'감':10,'포도':10}
dict_second={'사과':5,'감':25,'배':15,'귤':25}

def merge_dict(dict_first,dict_second):
    temp=copy.deepcopy(dict_first)
    temp.update(dict_second)
    for i in dict_first:
        if i in dict_second:
            temp[i]=dict_first[i]+dict_second[i]
    print(temp)

merge_dict(dict_first,dict_second)