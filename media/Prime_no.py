num=int(input("enter"))
flag=True
for i in range(2, num):
    if num%i==0:
        flag=False
        break
else: print("Prime")
if flag is False:
    print("not prime")
    