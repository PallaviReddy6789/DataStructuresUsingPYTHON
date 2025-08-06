n=int(input("enter a number"))
pt=0
ct=1
count=0
if(n==1):
    print("0")
elif(n==2):
    print("0 1")
else:
    while(count<n):
        print(pt)
        nt=pt+ct
        pt=ct
        ct=nt
        count+=1
    