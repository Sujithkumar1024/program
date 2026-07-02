n = int(input("enter n:"))
arr=list(map(int,input().split()))
prefix=[0]*n
prefix[0]=arr[0]

for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
q = int(input("enter q:"))
for _ in range(q):
    L,R = map(int,input().split())
    if L==0:
        print(prefix[R])
    else:
        print(prefix[R]-prefix[L-1])
