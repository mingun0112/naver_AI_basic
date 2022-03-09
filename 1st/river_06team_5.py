import re

def find_string(inputs):
    ans_list = []
    temp_str=re.sub(r"[0-9]+", " ", inputs)
    ans_list=temp_str.split()
    return ans_list
inputs="cat32dog16cow5"
string_list=find_string(inputs)
print(string_list)