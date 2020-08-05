"""
Created on Wed Aug  5 11:19:47 2020

@author: Atarax
"""
from bs4 import BeautifulSoup
import urllib.request as ur
import pdfkit
import requests
import re

url=input('Enter the URL: ') #https://a2oj.herokuapp.com/?handle=&div=1
html_page = ur.urlopen(url)
soup = BeautifulSoup(html_page, "html.parser")
links = []

for link in soup.findAll('a'): #scrapping all the anchor tags
    links.append(link.get('href'))

subs="codeforces.com/problemset" # A substring declaration to filter out all irerelevant links
res = [i for i in links if subs in i] #Filters all the links to select only questions urls.

config= pdfkit.configuration(wkhtmltopdf= "C:/Users/Atarax/Desktop/wkhtmltox/bin/wkhtmltopdf.exe") #set the path of wkhtmltopdf.exe
for i in range (len(res)):
    p_num= re.findall(r'[0-9]+', res[i])
    name= "Problem" + str(i + 1) + "_" + p_num[0] + res[i][-1] + ".pdf"
    request = requests.get(res[i])
    if request.status_code == 200:
        pdfkit.from_url( res[i], name, configuration=config)
        print("Problem",i+1, "has been downloaded") #This msg will be shown after each problem is downloaded
        
