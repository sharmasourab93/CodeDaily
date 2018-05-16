import sys
import os
import webbrowser
import xlrd
import urllib
from datetime import datetime, time
from time import sleep
"""Aim of the program is to write an HTML file which receives
    an input from the python code in the form of a URL and then
    play it in an enqueued manner """
class E:
    """Body of the class"""
    def __init__(self):
        self.in_queue=[]
        self.in_queue_time=[]
        
    def write_HTML(self,url):
        """Writes HTML to the File"""
        #input('#Seek and pass Video Duration')
        reload=str(30)  
        brk='<br/>'
        indent="\n"
        tabspace="\t"
        a=open('test2.html',"w")
        a.truncate()
        a.write('<html>'+'\n'+'<body>')
        a.write(brk+indent)
        #Refreshes the page
        a.write('<META HTTP-EQUIV="refresh" CONTENT="')
        #Video length/Duration Value (in seconds) is given to CONTENT
        a.write(reload)
        a.write('"/>')
        a.write(indent)
        #Change the ConfId in the code
        a.write('<iframe width="800" height="450" src="https://play.ericsson.net/embed/secure/iframe/entryId/'+url+'/uiConfId/22936291" frameborder="0" style="position:absolute">')
        a.write(indent)
        a.write('</iframe>')
        a.write(indent)
        a.write('</body>'+'\n'+'</html>')
        a.close()
        
    def push(self,obj):
        """To Push Objects into the Queue"""
        self.in_queue.append(obj)

    def push_time(self,obj):
        """Pushing Time in the Time Queue"""
        self.in_queue_time.append(obj)

    def Read4mFile(self):
        """To Read from the Excel File"""
        qlink=[]
        qtime=[]
        scriptpath=os.path.dirname(__file__)
        filename=os.path.join(scriptpath,'VideoList.xlsx')
        book=xlrd.open_workbook(filename)
        sheet=book.sheet_by_name("EricssonVideos")
        #Further Improve on adding YouTube, Vimeo or any other type of Videos
        #Meant only for Ericsson Videos
        for a in range(1,10):
            b=urllib.parse.urlparse(sheet.cell_value(a,0))
            c=b.path
            if(len(c)<20):
                x=c.split('/media/t/')
                y=x[1]
                qlink.append(y)
            else:
                x=c.split('/')
                y=x[5]
                qlink.append(y)
            
        for i in range(1,10):
            j=1
            time1=(sheet.cell_value(i,j))
            time2=(sheet.cell_value(i,(j+1)))
            time3=round((time2-time1)*24*3600)
            qtime.append(time3)
        self.in_queue=qlink
        self.in_queue_time=qtime
        print(self.in_queue)
        print(self.in_queue_time)
		
    def actionBlock(self):
        """For taking actions"""
        lc=os.path.dirname(__file__)
        location=os.path.join(lc,'digisig1.html')
        self.Read4mFile()
        webbrowser.open(location, new=0)
        i=0
        for i in range(len(self.in_queue)):
            
            if(i<len(self.in_queue)):
                self.write_HTML(self.in_queue[i])
                
            if(i==(len(self.in_queue)-1)):
                i=0
            print('%d Video Playing'%(i+1))
            sleep(int(self.in_queue_time[i]))
        print("All Videos Played for the day!")
def main():
    """Main Function Calls the Class E"""
    l=E()
    l.actionBlock()
main()
