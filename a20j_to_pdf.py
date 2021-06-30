"""
@author: Atarax
"""
from bs4 import BeautifulSoup
import urllib.request as ur
import pdfkit
import requests

CODEFORCES_API = "https://codeforces.com/api/user.info?handles="
a20jBaseURL = "https://a2oj.com/Ladder"

# An account should must have a rating to decide the appropriate ladder
username = input("Enter your codeforces username ")

# To fetch user's info using codeforces API and get the user's rating from the JSON response.
def get_rating(name):
    userURL = CODEFORCES_API + name
    data = requests.get(userURL)
    data = data.json()
    if(data['status'] == 'OK'):
        return data['result'][0]['rating']
    else:
        print(data['comment'])
        quit()

# Decide the appropriate ladder according to user's rating
def appropriate_ladder(rating):
    if (rating < 1300):
        ladderNo = "11"
    elif (1300 <= rating <= 1399):
        ladderNo = '12'
    elif (1400 <= rating <= 1499):
        ladderNo = '13'
    elif (1500 <= rating <= 1599):
        ladderNo = '14'
    elif (1600 <= rating <= 1699):
        ladderNo = '15'
    elif (1700 <= rating <= 1799):
        ladderNo = '16'
    elif (1800 <= rating <= 1899):
        ladderNo = '17'
    elif (1900 <= rating <= 1999):
        ladderNo = '18'
    elif (2000 <= rating <= 2099):
        ladderNo = '19'
    elif (2100 <= rating <= 2199):
        ladderNo = '20'
    elif (rating >= 2200):
        ladderNo = '21'
    return ladderNo


rating = get_rating(username)
ladder = appropriate_ladder(rating)

# The ladder URL
URL = a20jBaseURL + ladder + '.html'

html_page = ur.urlopen(URL)
soup = BeautifulSoup(html_page, "html.parser")

# links[] will store the URLs of the problems in the ladder
links = []

# problemName[] will store the problem's name
problemName = []

# Scrapping all the anchor tags (the hyperlinked text and the link)
for link in soup.findAll('a'):
    links.append(link.get('href'))
    problemName.append(link.string)

# Edit accordingly, wkhtmltopdf = "PATH/TO/DOWNLOADED/WKHTMLTOPDF_ZIP/wkhtmltopdf/bin/wkhtmltopdf.exe"
config= pdfkit.configuration(wkhtmltopdf = "C:/wkhtmltox/bin/wkhtmltopdf.exe")

# Path of the output folder where you want your pdfs to be downloaded. e.g outputDir = 'C:/a20jLadder_pdfs/'
outputDir = 'PATH/OF/DESTINATION_FOLDER/'

print('Starting....')
for i in range(len(links)):
    fileName = outputDir + str(i + 1) + '-' + problemName[i] + '.pdf'
    request = requests.get(links[i])
    if request.status_code == 200:
        pdfkit.from_url( links[i], fileName, configuration = config)
        print("Problem", i + 1, "has been downloaded")

print('All the problems of your ladder has been downloaded successfully. Happy Coding!')