from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url ="https://blaze.com/pt/games/crash"

driver.get(url)
html= driver.execute_script("return document.body.innerHTML")
soup= BeautifulSoup(html, "html.parser")
divisoria=soup.select_one("div")
data=[d for d in divisoria.select("div.entries")]
line=[]
for d in data:
    for t in d.select("span"):
        t = str(t)
        res= t.replace("<span class=\"", "")
        res=res.replace("\">", " - ").replace("</span>", "")
        if res.find("bad") >=0:
            print('\033[31m'+f'{res}'+'\033[0;0m')
        else:
            print('\033[32m'+f'{res}'+'\033[0;0m')