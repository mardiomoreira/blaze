from selenium import webdriver
from bs4 import BeautifulSoup


class Blaze():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url ="https://blaze.com/pt/games/crash"
    def Crash(self):
        self.driver.get(self.url)
        self.html= self.driver.execute_script("return document.body.innerHTML")
        self.soup= BeautifulSoup(self.html, "html.parser")
        self.divisoria=self.soup.select_one("div")
        self.data=[d for d in self.divisoria.select("div.entries")]
        self.line=[]
        for d in self.data:
            for t in d.select("span"):
                self.line.append(t.text)
        return self.line

lstresultados=Blaze().Crash()
print(lstresultados)
