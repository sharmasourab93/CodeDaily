import os
import xlrd
from datetime import datetime, time
def Read4mFile():
    qlink=[]
    qtime=[]
    scriptpath=os.path.dirname(__file__)
    filename=os.path.join(scriptpath,'VideoList.xlsx')
    book=xlrd.open_workbook(filename)
    sheet=book.sheet_by_name("EricssonVideos")
    for a in range(1,10):
        qlink.append(sheet.cell_value(a,0))
    for i in range(1,10):
        j=1
        time1=(sheet.cell_value(i,j))
        time2=(sheet.cell_value(i,(j+1)))
        time3=((time2-time1)*24*3600)
        qtime.append(time3)
    print(qlink)
    print(qtime)

Read4mFile()
    
