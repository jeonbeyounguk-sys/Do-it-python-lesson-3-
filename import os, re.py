import os, re
os.chdir(r'C:\Users\jeonb\OneDrive\Desktop\python_sample\git-practice-text')

f = open('friends101.txt', 'r', encoding = 'utf8')
script101 = f.read()

print(script101[:100])

Line = re.findall(r'Monica:.+', script101)
print(Line[:3])

for item in Line[:3]:
    print(item)

f.close()

f = open('monica.txt', 'w', encoding='utf8')
monica = ''
for i in Line:
    monica += i + '\n'
monica[:100]

f.write(monica)
