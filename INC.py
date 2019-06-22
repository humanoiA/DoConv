import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://www.cricbuzz.com/cricket-team/india/2/stats'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,'html.parser')
players=page_soup.findAll("tr",{"class":"cb-srs-stats-tr"})
for i in range(1,len(players)):
    k=players[i].findAll("td",{"class":"cb-srs-stats-td"})
    #for j in range(len(k)):
    print("Name-"+k[0].text+"  /Matches-"+k[1].text+"   /Innings-"+k[2].text+"   /Runs-"+k[3].text+"   /Average-"+k[4].text)
#tendulkar=players[1]
#p=tendulkar.findAll("td",{"class":"cb-srs-stats-td"})
#print(p[1].text)
