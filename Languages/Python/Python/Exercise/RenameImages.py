#Program to rename the contents of the folder.
import os
from os import rename
loc=os.path.dirname(r"C:\Users\ESOUSSH\Downloads\Ericsson\ImageSyncer\\")
Image_loc=os.path.join(loc,'Images\\')
count=0
content=[]
for file in os.listdir(Image_loc):
    if file.endswith(".jpg" or ".jpeg"):
        string='img'+str(count+1)+'.jpg'
        count+=1
        os.rename(os.path.join(Image_loc,file),os.path.join(Image_loc,string))
    content.append(file)
print(content)
