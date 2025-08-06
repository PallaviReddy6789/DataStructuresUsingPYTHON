def is_sorted(list1):
    return sorted (list1)
list=input("enter the list")
list=list.split()
y=is_sorted(list)
if (y==list):
    print("true ")
else:
    print("false")