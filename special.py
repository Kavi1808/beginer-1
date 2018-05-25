import re
y=input()
new=re.sub('[\w]+' ,'', y)
print(len(new))
