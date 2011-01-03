from html.parser import HTMLParser
from remotetext import *

class ExtractPageInfoParser(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.author = ''
        self.title = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs) # from tupple to dictionary
        
        if tag == "meta":
            if 'name' in attrs and attrs['name'] == 'author':
                self.author = attrs['content']
    
    def handle_data(self, data):
        if self.title == '' and self.get_starttag_text() == '<title>':
            self.title = data

def extract_htmlelements(url):
    htmlobj = RemoteText(url, from_encoding='utf-8', to_encoding='utf-8')
    parser = ExtractPageInfoParser(url)
    parser.feed(htmlobj.read())
    parser.close()
    return {'url':parser.url, 'title':parser.title, 'author':parser.author}
