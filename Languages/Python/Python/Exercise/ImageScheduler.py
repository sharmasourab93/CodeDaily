import os,csv
content=[]
x=r"C:\Users\ESOUSSH\Downloads\Ericsson\Digital Signage\Live Code\\"
for file in os.listdir(x):
    if file.endswith(".html"):
        print(file)
        content.append(file)
f=open(x+"Book1.csv")
for i in range(0,(len(content)-1),1):
    writer=csv.writer(x+'Book1.csv','wb')
    writer.writerows(content[i])
f.close()
