# a2oj PDF Downloader

<p align="center">
  <a href="https://github.com/atarax665/a2oj_PDF_downloader">
    <img src="https://www.pdfonline.com/html-to-pdf-api/html-to-pdf-api/htmlpdf10.png" alt="Logo" width="300" height="250">
  </a>


## 📌Introduction:
This python script downloads all the questions from your selected A2OJ ladder in pdf format. Instead of using the original A2OJ website I have used a dynamic version of A2OJ website created by [Subodh Verma](https://github.com/subodhk01/a2oj) because the new static [A2OJ website](https://a2oj.com/) requires you to sign in to access ladders while the other is quite easier to scrap.

## Idea behind:
If you have been into sport programming you must already know about [A2OJ](https://a2oj.com/). Its the best website to practice questions according to your codeforces rating to advance to become a candidate master or maybe a candidate grandmaster gradually.Sometimes college lectures can be boring so, I wrote this script to download all the questions in my current ladder in pdf format so that I can print them and solve them in between boring lectures.

## Requirements:
* Python 3.0 or higher
* [pdfkit](https://pypi.org/project/pdfkit/)
* [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

## Local Setup:
1. Drop a ⭐ on the Github Repository. 
2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
https://github.com/atarax665/a2oj_PDF_downloader.git
```
3. Install the Packages: 
```sh
pip install -r requirements.txt
```
4. Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) and run the setup.
5. Edit a2oj_PDF-downloader.py in any text editor and replace wkhtmltopdf.exe's path with the path on your local machine where you just installed it.

```sh
config= pdfkit.configuration(wkhtmltopdf= "C:/Users/Atarax/Desktop/wkhtmltox/bin/wkhtmltopdf.exe")
```
6. At last, push in the command:
```sh
python a2oj_PDF_downloader.py
```
7. Enter the URL of the ladder you want to download from [A2OJ website](https://a2oj.herokuapp.com/)
8. Sit back and enjoy, all the 100 questions in the ladder will be downloaded, converted and saved in the active folder.

## License:
[MIT](LICENSE.md)
