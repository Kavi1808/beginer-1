a=int(input("enter the num:"))
b=int(input("enter the num:"))
for i in range(a,b+1):
    if(i>1):
        for c in range(2,i):
            if(i%c)==0:
                break
            else:
              print (i)
