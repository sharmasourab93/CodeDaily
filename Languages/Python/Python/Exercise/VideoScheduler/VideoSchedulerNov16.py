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
        self.flag=[]
        
    def write_HTML(self,off,url):
        """Writes HTML to the File"""
        #input('#Seek and pass Video Duration')
        reload=str(900)  
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
        a.write(reload+'"/>')
        a.write(indent)
        if(off==0):
            self.write_kaltura(a,url)
        else:
            self.write_youtube(a,url)
        a.write(indent)
        a.write('</iframe>')
        a.write(indent)
        a.write('</body>'+'\n'+'</html>')
        a.close()
        
    def write_youtube(self,a,url):
        """Write YouTube Videos to the HTML File"""
        a.write('<iframe width="800" height="500" src="https://youtube.com/embed/'+url+'?autoplay=1&loop=1&version=3&playlist='+url+'&showinfo=0&rel=0&autohide=1&controls=2&" frameborder="0" style="position:absolute">')

    def write_kaltura(self,a,url):
        """Write Kaltura Videos to the HTML Files"""
        #Change the ConfId in the code
        a.write('<iframe width="800" height="500" src="https://play.ericsson.net/embed/secure/iframe/entryId/'+url+'/uiConfId/36909991" frameborder="0" style="position:absolute">')

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
        for a in range(1,10):
            b=urllib.parse.urlparse(sheet.cell_value(a,0))
            if(("ericsson" in b.netloc)!=0):
                c=b.path
                self.flag.append(0)
                if(len(c)<20):
                    x=c.split('/media/t/')
                    y=x[1]
                    qlink.append(y)
                else:
                    x=c.split('/')
                    y=x[5]
                    qlink.append(y)
            elif(("youtube" in b.netloc)!=0):
                self.flag.append(1)
                if(("watch" in b.path)==1):
                    x=b.query[2:]
                    y=x
                    qlink.append(y)
                elif(("embed" in b.path)==1):
                    x=b.path[7:]
                    y=x
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
        print(self.flag)
		
    def actionBlock(self):
        """For taking actions"""
        lc=os.path.dirname(__file__)
        #location=os.path.join(lc,'digiM.html')
        self.Read4mFile()
        location=r"C:\Users\ESOUSSH\Downloads\Ericsson\Digital Signage\Live Code\digiM.html"
        webbrowser.open(location, new=0)
        i=0
        while(True):
            i=0
            for i in range(len(self.in_queue)):
                if(i<len(self.in_queue)):
                    off=self.flag[i]
                    self.write_HTML(off,self.in_queue[i])
                print('%d Video Playing'%(i+1))
                sleep(int(self.in_queue_time[i]))
        print("All Videos Played for the day!")
def main():
    """Main Function Calls the Class E"""
    l=E()
    l.actionBlock()
main()
