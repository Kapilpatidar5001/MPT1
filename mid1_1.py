l1=(input("enter list 1 seperated by comma")).split(',')
w=input("enter world to remove")
o=int(input("enter the occurence to remove"))
c=0
r=[]
print(type(w))
print(l1)
for i in l1:
    if (i==w):
        c=c+1
        if (c!=o):
            r.append(i)
    else:
        r.append(i)
print(r)
