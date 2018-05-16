#CSV Reader Program
import csv,os
content=[]
loc=os.path.dirname(__file__)
x=os.path.join(loc,'Book1.csv')
with open(x,'r') as csvfile:
    spamreader=csv.reader(csvfile,delimiter="\n",quoting=csv.QUOTE_NONE)
    for row in spamreader:
        content.append(row)
for i in content:
    content.remove([])
    for j in range(0,len(content)):
        content[j]=content[j][0]

print(content)
print(content[1])
