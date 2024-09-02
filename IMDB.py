import requests
from bs4 import BeautifulSoup



url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"
}

html=requests.get(url,headers=headers).content

 
soup=BeautifulSoup(html,"html.parser")

data=soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=10)


for item in data:
    movie_name=item.find("h3",{"class":"ipc-title__text"}).text
    imdb=item.find("span",{"class":"ipc-rating-star"}).text
 
    print(movie_name, imdb)