

def decorate(fx):
    def modified(*args,**kwargs):
        print("Welcome to our function ")
        c=fx(*args,**kwargs)
        print(c)
        print("Thanks for using This function")
    return modified
@decorate
def add(a,b):
    return a+b
# if __name__ == '__main__':
#     decorate(add)(5,6)
if __name__ == '__main__':
    add(5,6)