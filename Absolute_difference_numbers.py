n,m=map(int,input().split())
if n>=2*m:
    y=int(str(n)[0:m])
    z=int(str(n)[-m:])
    a=abs(y-z)
    print(a)