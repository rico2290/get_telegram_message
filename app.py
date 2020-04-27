from bs4 import BeautifulSoup as bs
import urllib
import codecs, os

current_path = os.getcwd()
print(current_path)

for file in os.listdir():
    print(file)

with open('messages.html') as file:
    contents = file.read()
ss = bs(contents, 'html.parser')
#soup = bs(contents, 'lxml')
div_from_text = ss.findAll('div', attrs={'class': 'text'})
div_body = ss.findAll('div', attrs={'class': 'body'})
#print(type(div_body))
for div in div_from_text:
    print(f'\ntamanho: {len(div.text)}',div.text)