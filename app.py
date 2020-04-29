from bs4 import BeautifulSoup as bs
import urllib
import codecs, os, csv, errno

current_path = os.getcwd()
try:
    if not os.mkdir(f'{current_path}/temp'):
        os.mkdir('temp')
except OSError as e:
    if e.errno == errno.EEXIST:
        pass
        #print('folder not created')
    else:
        raise

for file in os.listdir():
    if file[-4:] in ['html', 'HTML']:
        #print(file[:-5])
        with open(file) as html_file:
            contents = html_file.read()
        ss = bs(contents, 'html.parser')
        #soup = bs(contents, 'lxml')
        div_from_text = ss.findAll('div', attrs={'class': 'text'})
        div_body = ss.findAll('div', attrs={'class': 'body'})
        #print(type(div_body))
        
        list_message = []
        for div in div_from_text:
            list_message.append(div.text.replace('"','').strip())
            #print(f'\ntamanho: {len(div.text)}',div.text)
        with open(r'temp/{}.csv'.format(file[:-5]), 'w', newline='',) as csv_file:
            writer_file = csv.writer(csv_file, delimiter=',', escapechar="'", quoting=csv.QUOTE_NONE)
            #print(list_message)
              
            #writer_file.writerow(['message'])
            writer_file.writerow([message+'\n' for message in list_message])
     
                
            
            