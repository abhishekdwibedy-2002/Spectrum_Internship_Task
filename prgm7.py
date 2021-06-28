
# Python Program To Find The Triplet

arr = []
count=0
n = int(input("Enter number of elements : "))
print("enter",n ,"elements")
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
s=int(input("enter the sum to be found "))
for a in range(0,n-2):
    if(count>=1):
        break
    for b in range(0,n-1):
        if(count>=1):
            break
        for c in range(0,n):
            if(arr[a]+arr[b]+arr[c]==s):
                if(arr[a]!=arr[b]!=arr[c]):
                    print("Triplet Is :- ", arr[a], arr[b], arr[c])
                    count = count + 1
                    break
if(count==0):
    print("no triplets found")