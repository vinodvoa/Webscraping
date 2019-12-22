import os
import requests
import smtplib
import pandas as pd

from bs4 import BeautifulSoup
from email.message import EmailMessage

try:
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # print(os.environ)
    print(EMAIL_ADDRESS)

except Exception as e:
    print(e)
    quit()

if EMAIL_ADDRESS == None:
    print('EMAIL_ADDRESS fetch error')
    quit()

try:
    EMAIL_PASS = os.environ.get('EMAIL_PWD')

except Exception as e:
    print(e)
    quit()

if EMAIL_PASS == None:
    print('EMAIL_PASS fetch error')
    quit()

def append_csv(datain):
    # print('Append')
    with open('news.csv', 'a') as f:
        datain.to_csv(f, header=False)

# Barrons
def barrons():
    print('Barrons')
    news = []    

    page = requests.get('https://www.barrons.com/')

    soup = BeautifulSoup(page.content,'lxml')

    articles = soup.find_all('article', class_='BarronsTheme--story--3Z0LVZ5M BarronsTheme--DayArticle--1S_xRQst BarronsTheme--inline-timetoread--32E7f2DK BarronsTheme--slimPaddingBottom--1Ygnkutl')

    for article in articles:
        try:
            story = article.find('h3',class_='BarronsTheme--DayArticle--3GZd7oug BarronsTheme--headline--1y73iK8c BarronsTheme--heading-serif-14--2PdxURsk BarronsTheme--barrons-endmark--1SVRuT98')
        
        except Exception as e:
            print(e)
            continue

        try:
            link = story.find('a')

        except Exception as e:
            print(e)
            continue
        
        news.append(story.text + ' : ' + link.get('href'))

    df = pd.DataFrame(news)
    # print(df)
    append_csv(df)

# NYT
# news = []    

# page = requests.get('https://www.nytimes.com/')

# soup = BeautifulSoup(page.content,'lxml')

# articles = soup.find_all('article', class_='BarronsTheme--story--3Z0LVZ5M BarronsTheme--DayArticle--1S_xRQst BarronsTheme--inline-timetoread--32E7f2DK BarronsTheme--slimPaddingBottom--1Ygnkutl')

# for article in articles:
#     try:
#         story = article.find('h3',class_='BarronsTheme--DayArticle--3GZd7oug BarronsTheme--headline--1y73iK8c BarronsTheme--heading-serif-14--2PdxURsk BarronsTheme--barrons-endmark--1SVRuT98')
    
#     except Exception as e:
#         print(e)
#         continue

#     try:
#         link = story.find('a')
    
#     except Exception as e:
#         print(e)
#         continue

#     news.append(story.text + ' : ' + link.get('href'))

# df = pd.DataFrame(news)
# append_csv(df)

# FT
def ft():
    print('FT')
    news = []    

    page = requests.get('https://www.ft.com/')

    soup = BeautifulSoup(page.content,'lxml')

    articles = soup.find_all('div', class_='o-teaser__heading')

    i = 0

    for article in articles:
        try:
            story = article.find('a', class_='js-teaser-heading-link')

        except Exception as e:
            print(e)
            continue

        news.append(story.text + ' : ' + 'https://www.ft.com' + story.get('href'))

        i += 1

        if i > 9:
            break

    df = pd.DataFrame(news)
    # print(df)
    append_csv(df)

# Guardian
def guardian():
    print('Guardian')
    news = []    

    page = requests.get('https://www.theguardian.com/international')

    soup = BeautifulSoup(page.content,'lxml')

    articles = soup.find_all('li', class_='fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link')

    i = 0

    for article in articles:
        try:
            story = article.find('a', class_='u-faux-block-link__overlay js-headline-text')
        
        except Exception as e:
            print(e)
            continue

        try:    
            link = story.get('href')
        
        except Exception as e:
            print(e)
            continue

        news.append(story.text + ' : ' + link)

        i += 1

        if i > 9:
            break

    df = pd.DataFrame(news)
    # print(df)
    append_csv(df)

# SF Chronicle
def sfc():
    print('SF Chronicle')
    news = []    

    page = requests.get('https://www.sfchronicle.com/')

    soup = BeautifulSoup(page.content,'lxml')

    articles = soup.find_all('a', class_='hdn-analytics ')

    for article in articles:
        try:
            story = article.text
        
        except Exception as e:
            print(e)
            continue

        try:
            link = article.get('href')

        except Exception as e:
            print(e)
            continue

        news.append(story + ' : ' + 'https://www.sfchronicle.com' + link)

    df = pd.DataFrame(news)
    print(df)
    append_csv(df)

# TR
def tr():
    print('TR')
    news = []    

    page = requests.get('https://www.technologyreview.com/')

    soup = BeautifulSoup(page.content,'lxml')

    articles = soup.find_all('h2', class_='jsx-860405766 head')

    for article in articles:
        try:
            story = article.find('a', class_='headLink')
        
        except Exception as e:
            print(e)
            continue

        try:    
            link = story.get('href')

        except Exception as e:
            print(e)
            continue

        news.append(story.text + ' : ' + 'https://www.technologyreview.com' + link)

    df = pd.DataFrame(news)
    # print(df)
    append_csv(df)

# Economist
def economist():
    print('Economist')
    news = []    

    page = requests.get('https://www.economist.com/')

    soup = BeautifulSoup(page.content,'lxml')

    articles = soup.find_all('article', class_='teaser teaser--with-more-callout')

    for article in articles:
        try:
            story = article.find('span', class_='flytitle-and-title__title')
        
        except Exception as e:
            print(e)
            continue

        try:    
            link = article.find('a')
        
        except Exception as e:
            print(e)
            continue

        news.append(story.text + ' : ' + 'https://www.economist.com' + link.get('href'))

    df = pd.DataFrame(news)
    # print(df)
    append_csv(df)

def newsmail():
    print('newsmail')
    msg = EmailMessage()

    msg['subject'] = 'Todays News from various websites'
    msg['From'] = 'vinodvoa@gmail.com'
    msg['To'] = 'vinodvoa@gmail.com'

    newsdf = pd.read_csv('news.csv')
    # print(newsdf)
    newsdf.to_csv('news.txt', header=None, index=None, sep=' ', mode='a')

    with open('news.txt', 'r') as fp:
        msg.set_content(fp.read(), 'str')
        print(msg)

    # with smtplib.SMTP('localhost', 1025) as smtp:
        # smtp.sendmail('vinodvoa@gmail.com','vinodvoa@gmail.com','test')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        
        except Exception as e:
            print(e)
            quit()

        try:
            smtp.send_message(EMAIL_ADDRESS,'vinodvoa@gmail.com',msg)

        except Exception as e:
            print(e)
            quit()

if __name__ == "__main__":
    # barrons()
    # nyt()
    # guardian()
    # sfc()
    tr()
    # economist()

    newsmail()