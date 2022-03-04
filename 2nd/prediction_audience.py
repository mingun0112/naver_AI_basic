import csv
movie_data=[]
header=[]
rownum=0

with open("movies_train.csv","r",encoding='utf8')as p_file:
    csv_data=csv.reader(p_file)
    for row in csv_data:
        if rownum==0:
            header=row
        distributor=row[2]
        if distributor.find("액션")!=-1:
            movie_data.append(row)
        rownum+=1

with open("movies_Lotte_train.csv","w",encoding="utf8")as s_p_file:
    writer=csv.writer(s_p_file,delimiter='\t',quotechar="'",quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    for row in movie_data:
        writer.writerow(row)