# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:22:37 2020

@author: Atarax
"""
import pdfkit
import requests
print("Enter Problem number:\n")
str1=input()
print("Enter problem category(A/B/C/D/E/F):")
str2=input()
fixed="https://codeforces.com/problemset/problem/"
search=fixed+str1+"/"+str2
name=str1+str2+".pdf"
config= pdfkit.configuration(wkhtmltopdf= "C:/Users/Atarax/Desktop/wkhtmltox/bin/wkhtmltopdf.exe")
request = requests.get(search)
if request.status_code == 200:
    pdfkit.from_url( search, name, configuration=config)
    print("Problem has been downloaded")
else:
    print("This problem does not exist")

