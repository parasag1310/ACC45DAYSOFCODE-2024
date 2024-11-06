# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    b*=2
    if(x<=(a+b)):
        print("Qualify")
    else:
        print("NotQualify")