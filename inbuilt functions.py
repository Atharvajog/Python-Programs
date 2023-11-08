l1=[1,34,12,45,23,56,24,2]
t1=((34,12),(345,23),(456,34),(12,78),(56,90),(56,43))
d1={'a':13,'e':32,'c':2,'x':34,'v':15}
#Sorted(iterator,key=function,reverse=True/False)
print(sorted(l1,reverse=True))
print(sorted(t1,key=lambda x:x[1],reverse=True))
 #filter(function,iterator) this is just use for true or false base values
print(list(filter(lambda x:x%2==0,l1)))
#map(function,iterator) this is basically use to do a particular operation on all the values in the data structure
print(list(map(lambda x:x+2,list(filter(lambda x:x%2==0,l1)))))
#reduce(function,iterator) use to perform a operation on all the values of the iterator
from functools import reduce
doubles=list(map(lambda x:x+2,list(filter(lambda x:x%2==0,l1))))
print(reduce(lambda x,y:x+y,doubles))
#zip(iterator,iterator) zip is only use to connect two iterator
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(dict(x))
#enumerate function
for x,item in enumerate(l1):
    print ((x+1),item)
#id() returns memory address of python object
print(id(a))
#bin() take int and return binary equivalent
print(bin(4))
#sum(iterable,start) takes iterable and starting digit and add it to all the elements in the list
print(sum(l1,5),)
#min() and max() takes itersble,key and a default as arguements
print(min(l1,key= lambda x:-x,default=0))