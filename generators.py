def generator():
    n=1
    while n <= 10:
        sq = n*n
        yield sq
        n+=1
for i in generator():
    print(i)