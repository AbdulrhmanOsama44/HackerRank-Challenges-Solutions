from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f'-> {name} > {value}')
    
parser= myHTMLParser()

for _ in range(int(input())):
    inp= input() 
    parser.feed(inp)