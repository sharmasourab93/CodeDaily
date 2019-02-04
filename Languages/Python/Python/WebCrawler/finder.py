from html.parser import HTMLParser

from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
    
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            for(attrbute, value) in attrs:
                if attrbute=="href":
                
        print(tag)
    
    def error(self,message):
        pass
    
finder=LinkFinder()
finder.feed()