n = int(input("Enter number of elements : \n"))
lst=[]
print("Enter",n ,"Elements")
for i in range(0, n):
    element = int(input())
    lst.append(element)
idx=int(input("Enter the value To Find The Smallest no. :- \n"))
lst.sort()
print("Your " ,idx,"th smallest no. is: ",lst[idx-1])