import requests
from bs4 import BeautifulSoup


def get_info(lnk): # link of the wiki article 
    o = requests.get(lnk).content
    soup = BeautifulSoup(o, 'lxml')
    a = soup.find('div', id='bodyContent')
    output = ""
    for i in a.find_all('p'):
        
        
        
        output += i.text
    
    output = output.replace("\n",'')
    return output


    

