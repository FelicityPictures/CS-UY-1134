def foo(n,c=-1):
    if n==0:
        return c
    return foo(int(n/2),c+1)


print(foo(250))
