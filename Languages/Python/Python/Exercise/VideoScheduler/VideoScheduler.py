#This program samples enqueuing of Youtube video URLs
import sys
import os
import webbrowser
from time import sleep
"""Aim of the program is to write an HTML file which receives
    an input from the python code in the form of a URL and then
    plays it in an enqueued manner """
class E:
    """Body of the class"""

    def __init__(self):
        self.in_queue=[]
        
    def write_HTML(self,url):
        """Writes HTML to the File"""
        brk='<br/>'
        indent="\n"
        tabspace="\t"
        a=open('test2.html',"w")
        a.truncate()
        a.write('<html>'+'\n'+'<body>')
        a.write(brk+indent)
        a.write('<META HTTP-EQUIV="refresh" CONTENT="5"/>') #Refresh the page
        a.write(brk+indent)
        a.write('<iframe width="560" height="315" src="'+url+'?autoplay=1" frameborder="0" allowfullscreen>')
        a.write(brk+ indent)
        a.write('</iframe>')
        a.write(brk+indent+tabspace)
        a.write('Hello! ^ Your Video Plays Here ^')
        a.write(brk+indent)
        a.write('</body></html>')
        a.write(brk+indent)
        a.close()
        
    def push(self,obj):
        """TO Push Objects into the Queue"""
        self.in_queue.append(obj)

    def push_urls(self):
        """Dumb method Just to Push Urls into the Queue"""
        #self.push('https://play.ericsson.net/embed/secure/iframe/entryId/1_gxxteffl/uiConfId/36253771')
        self.push('https://www.youtube.com/embed/9orjD9xj6z8')
        self.push('https://www.youtube.com/embed/OMJc43wUPLM')
        self.push('https://www.youtube.com/embed/ft-dYaZKxwU')
        self.push('https://www.youtube.com/embed/2fG9-W-OwCs')
        
    def actionBlock(self):
        """For taking actions"""
        location="file:///C:/Users/ESOUSSH/Desktop/Digital Signage/test2.html"
        self.push_urls()
        print(self.in_queue)
        i=0
        while(self.in_queue and i<len(self.in_queue)):
            if(i==0):
                self.write_HTML(self.in_queue[i])
                webbrowser.open(location,new=0) #Open the Page
            else:
                self.write_HTML(self.in_queue[i])
            i=i+1
            print('%d Video Playing'%i)
            #self.in_queue.pop()
            sleep(5)
        print("All Videos Played for the day!")
        
def main():
    l=E()
    l.actionBlock()

main()



#chrome_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
#webbrowser.get(chrome_path).open("file:///C:/Users/ESOUSSH/Desktop/Digital Signage/test2.html")
#webbrowser.get(using='google-chrome')
#webbrowser.get("open -a C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                


    
