a=int(input())
sum=0
l=[]
for i in range(1,a+1):
  n=int(input())
  l.append(n)
print l 
for i in range(0,len(l)):
  for j in range(i,len(l)):
    if(l[i]>l[j]):
      l[i],l[j]=l[j],l[i]   
print l
