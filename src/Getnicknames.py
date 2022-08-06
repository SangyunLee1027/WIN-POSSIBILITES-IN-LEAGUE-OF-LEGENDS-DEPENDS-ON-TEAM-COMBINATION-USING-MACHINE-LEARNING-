from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_nicknames(link):
    req = Request(link, headers ={'User-Agent' : 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage,"lxml") 

    nicknames = []
    nicknames.append("Nickname")

    temp = soup.find("tr", attrs={"class":"css-1kk0pwf e1g3wlsd9"})
    nicknames.append(temp.find("strong", attrs = {"summoner-name"}).text)
    for i in range(50):
        temp = temp.find_next_sibling("tr")
        nicknames.append(temp.find("strong", attrs = {"summoner-name"}).text)
    df = pd.DataFrame(nicknames)
    df.to_csv('./Data/Nicknames.csv', mode='w', index=False, header= False)

