# cook your dish here
# cook your dish here
import math
T=int(input())
for i in range(T):
    X,Y,R=map(int,input().split())
    a=R//30
    b=math.ceil((X+a)/Y)
    print(b)