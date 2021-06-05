#two brothers
for i in range(int(input())):
    a,b,n=map(int,input().split())
    if(n%2==1):
        a=a*2
    mi=min(a,b)
    ma=max(a,b)
    print(ma//mi)
