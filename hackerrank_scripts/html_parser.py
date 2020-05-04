# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for item in attrs:
            print(f"-> {item[0]} > {item[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for item in attrs:
            print(f"-> {item[0]} > {item[1]}")

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())