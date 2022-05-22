# Write a program to find the sum of first n natural numbers using a while loop.
n=int(input("enter no."))
sum=0
while(n>0):
    sum=sum+n
    n=n-1
print(sum)