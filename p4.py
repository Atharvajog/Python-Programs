list1=["john","dave","dave","kiara","john","sansa"]
dic1={}

for i in list1:
    count=0
    for j in list1:
        if j==i:
            count=count+1
    dic1[i]=count
    count=0
print(dic1)