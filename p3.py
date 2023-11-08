def myfun(var):
    return lambda a:a*var
fun1=myfun(2)
print(fun1(21))