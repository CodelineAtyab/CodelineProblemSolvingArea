n=int(input("enter no. : "))
s=""
while(n>0):
     r=n%2
     s=str(r)+s
     print(s)
     n=n//2
     print(int(s))

