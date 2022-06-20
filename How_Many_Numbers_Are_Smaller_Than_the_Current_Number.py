n=int(input())
arr=list(map(int,input().split()))
r=0
k=0
count=0
k=0
m=0
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if(arr[j]<arr[i]):
            count+=1
    print(count,end=' ')