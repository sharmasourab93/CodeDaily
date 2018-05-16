import os
loc=os.path.dirname(r"C:\Users\ESOUSSH\Downloads\Ericsson\DigitalSignage\ImageSyncer\\")
Image_loc=os.path.join(r'\Images')
i=0
length=len(os.listdir(Image_loc)
for f in os.listdir(loc):
    while(i>length):
        string='img'+str(i+1)+'.jpg'
        if f.endswith(".jpg" or ".jpeg"):
            os.rename(os.path.join(Image_loc,f),os.path.join(Image_loc,string))
    i+=1
diff=0
newlength=len(os.listdir(Image_loc)
for g in os.listdir(Image_loc):
    if(length>newlength):
        diff=length-newlength
        content=content[:diff]
    elif(length<newlength):
        diff=newlength-length
        for h in os.listdir(Image_loc):
            l=newlength-diff
            if(h.startswith('img')==False and l<newlength):
                  string='img'+str(l+1)+'.jpg'
                  os.rename(os.path.join(Image_loc,h),os.path.join(Image_loc,string))
             l+=1
              
