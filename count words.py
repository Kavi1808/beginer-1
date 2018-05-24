import re
line = "i am a super girl"
count = len(re.findall(r'\w+', line))
print (count)
