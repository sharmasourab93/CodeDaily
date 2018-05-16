import os
import xlrd
from datetime import time,datetime
qlink=[]
qtime=[]
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'VideoList.xlsx')
workbook=xlrd.open_workbook(filename)
sheet=workbook.sheet_by_name("EricssonVideos")
print("The Value is %s"%(format(sheet.cell(1,0).value)))
qlink.append(sheet.cell(1,0))
qlink.append(sheet.cell(2,0))
date = sheet.cell_value(1,1)
datetime_value = datetime(*xlrd.xldate_as_tuple(date, 0))
date1 = sheet.cell_value(1,2)
datetime_value = datetime(*xlrd.xldate_as_tuple(date1, 0))
#qtime.append((sheet.cell(1,1))-(sheet.cell(1,2)))
print(qlink)
print(datetime_value.time())
date2=date1-date
date3=(date2*24*3600)
print(date2)
print(date3)
