# cook your dish here
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    sm=b*3
    mp=a-b
    km=sm-mp
    if km>=c:
        print('PASS')
    else :
        print('FAIL')