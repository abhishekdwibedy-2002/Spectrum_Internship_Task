# Python Program To Print First 'n' Perfect Number

num = int(input("enter number Till which You Want To print the Prefect Number :- "))
count=0
a=6 #First Perfect Number
while(count<=num):
    while(a!=0 and count<=num):
        s=0
        for i in range(1,a):
            if(a%i==0):
                s=s+i
        if(a==s):
            count=count+1
            if(count<=num):
                print(a)
        a+=1