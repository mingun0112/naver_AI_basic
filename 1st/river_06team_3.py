score=[(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    cnt=0
    for i in score:
        cnt+=1
        avg=sum(i)/2
        print(cnt,"번, 평균 : ",avg)
print(get_avg(score))