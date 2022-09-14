n=int(input("n="))
m=int(input("m="))
def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
if(n>m):
   print("C=",factorial(n)/(factorial(m)*factorial(n-m)))