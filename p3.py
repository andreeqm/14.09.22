print("a)Adunarea a doua fractii:")
x,y=int(input("prima fractie: ")),int(input("supra "))
a,m=int(input("a doua fractie: ")),int(input("supra "))
def adunare(x,y,z,w):
    s=((x*w)+(z*y))/(y*w)
    return (s)
print(x,'/',y,'+',a,'/',m,'=',adunare(x,y,a,m))

print("b)Inmultirea a doua fractii:")
a,b=int(input("prima fractie: ")),int(input("supra "))
c,d=int(input("a doua fractie: ")),int(input("supra "))
def inmultire(x,y,z,w):
    p=(x*z)/(y*w)
    return (p)
print(a,'/',b,'*',c,'/',d,'=',inmultire(a,b,c,d))    

